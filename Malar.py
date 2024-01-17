import os
import Clock
import speech_recognition as sr
from AppInteractions import UserNameWindow
from Response import RunMalar
from ImageGen import ImageGenerator
from WindowsOpen import ImageFileChooser
from Greetings import WeatherAnalyzer
from Speaker import TextToSpeechPlayer
from datetime import datetime
import time
import pygame
import TaskManager
import NewsFeed

def speak(text):
    player = TextToSpeechPlayer()
    print('மலர் : ' + text)
    player.play_text(text)
    return text


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, timeout=6)
        command = recognizer.recognize_google(audio_data).lower()
        print(f"User : {command}")
        if "stop" in command:
            speak("Sure {userName}! call me anytime if you need!")
            listenForTrigger()
        else:
            start_malar(command)


def listenForTrigger():

    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for trigger...")
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source, timeout=5)
            trigger_phrase = recognizer.recognize_google(audio_data).lower()
            trigger_phrase = trigger_phrase.lower()
            try:
                if "malar" in trigger_phrase or "mala" in trigger_phrase or "hey" in trigger_phrase or "hello" in trigger_phrase or "hi" in trigger_phrase or "ok" in trigger_phrase or "excuse me" in trigger_phrase:
                    speak(f"Yess {userName}!!")
                    clock.play_sound("Sounds/Listening.mp3")
                    while pygame.mixer.music.get_busy():
                        time.sleep(1)
                    command = listen()


                else:
                    listenForTrigger()
            except:
                listenForTrigger()
    except:
        listenForTrigger()

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=6000)
        text = recognizer.recognize_google(audio)
    return text

def start_malar(command):
    try:
        if any(keyword in command for keyword in ["original", "fake", "ai image", "real"]) and "image" in command:
            speak("Sure, I can say if the image is Real or AI generated. Kindly click and drag the image file you want to verify!")
            app = ImageFileChooser()
            image = app.run()
            speak(image)
            listenForTrigger()
    except Exception as e:
        listen()

    from AppInteractions import apps_websites_opener as awo
    from AppInteractions import MediaPlayerAssistant as Player
    from AppInteractions import WhatsappAssistant as Whatsapp

    if ("time" in command or "date" in command) and "set" not in command:
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime('%d %b %Y')
        if "time" in command and "date" in command:
            speak(f"The date is {current_date} and the time is {current_time}. {userName}, is there anything else ?")
            listen()
        elif "time" in command:
            speak(f"The time is {current_time} {userName}, is there anything else ?")
            listen()

        else:
            speak(f"The date is {current_date} {userName}, is there anything else ?")
            listen()
    elif "set" in command:
           if "task" in command:
               try:
                    task_set = TaskManager.TaskManager()
                    task_set.add_task_to_csv(command)
                    speak(f"Setting {command[7:]}")
                    listen()
               except:
                    listen()

           elif "alarm" in command:
               try:
                   clock = Clock.Clock()
                   speak(clock.set_alarm(command))
                   listenForTrigger()
               except:
                    listen()

           elif "timer" in command:
               clock = Clock.Clock()
               speak(clock.set_timer(command))
               listenForTrigger()


    elif "shutdown" in command and "pc" in command or "computer" in command:
        speak("{userName}, I am really gonna miss you, please dont go, do you really wanna continue?")
        sentance = speech_to_text()
        if "yes" in sentance:
            speak("miss you {userName}!")
            os.system("shutdown /s /t 1")
        else:
            speak("thank god, you didn't go! Tell me what to do {userName}?")
            listen()
    elif "do i have" in command or ("tasks" in command and "today" in command) or ("task" in command and "today" in command):
        tasks = TaskManager.TaskManager()
        speak(tasks.check_tasks_today(command))
        listen()
    elif "news" in command:
        if "news" in command and "more" in command:
            news = NewsFeed.NewsFetcher()
            speak(news.Specific_news(command))
            listen()
        else:
                news_fetcher = NewsFeed.NewsFetcher()
                news_result = news_fetcher.execute_command(command)
                var = " "
                for i in news_result:
                    var+=i+" "
                speak(var)
                speak("thats all for today's new's {userName}, anything else?")
                listen()

    elif "open" in command:
        speak(awo.open_apps(command))
        listen()

    elif 'launch' in command:
        speak(awo.open_website(command))
        listen()
    elif ("generate" in command or "create" in command) and "image" in command:
        image_gen = ImageGenerator()
        speak(image_gen.generate_variations(command))
        listen()
    elif "play" in command:
        if "spotify" in command:
            speak(Player.play_on_spotify(command))
        else:
            speak(Player.play_on_youtube(command))
        listen()
    elif "message" in command:
        speak(Whatsapp.send_message(command))
        listen()

    elif "weather" in command or "how is the day" in command:
        analyzed_report = weather_analyzer.run_analysis()
        num = analyzed_report.find("with") + 8
        analyzed_report = analyzed_report[num:]
        if "cold" in analyzed_report:
            speak("{userName}! " + analyzed_report + " , So use a Rain jacket {userName}!")
        else:
            speak("{userName}! " + analyzed_report + ", Hope its a fine day!")
        listen()
    else:
        alli = RunMalar()
        out = alli.RunBot(command)
        speak(out)
        listen()


if __name__ == "__main__":

    latitude, longitude = 11.038216204495983, 76.92552830366209
    speak("Starting MALAR")
    with open('text files/PrimaryUserName.txt', "r") as file:
        Name = file.read()
        file.close()
    if Name == "None":
            speak("Kindly enter your name in the input box")
            ur = UserNameWindow()
            userName = ur.get_user_name()
            with open("text files/PrimaryUserName.txt", "w") as file:
                file.write(userName)
            speak(f"Hello, {userName} You are now the primary user of MALAR.")
    else:
            userName = Name
    with open("text files/malarPrompt.txt", "r") as file:
        Prompt = file.read()
        Prompt = Prompt.replace("user",userName)
        file.close()
    with open("text files/malarPrompt.txt", "w") as file:
        file.write(Prompt)
        file.close()

    clock = Clock.Clock()
    clock.play_sound("Sounds/Startup.mp3")
    weather_analyzer = WeatherAnalyzer(latitude, longitude)
    speak(weather_analyzer.run_analysis(userName))
    listenForTrigger()

