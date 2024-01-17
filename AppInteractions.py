import csv
import os
import time
import webbrowser
import pyautogui
import validators
import tkinter as tk


app_commands = {}
with open('CsvFiles/commands.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        clean_app_name = row['Name'].lower().replace(' ', '').replace(':', '')
        app_commands[clean_app_name] = row['Path']

Link_commands = {}
Link_csv = 'CsvFiles/Links.csv'

with open(Link_csv, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        clean_website_name = row['Name'].lower().replace(' ', '').replace(':', '')
        Link_commands[clean_website_name] = row['Link']

class WhatsappAssistant:
    @staticmethod
    def send_message(command):
        cmdLst = command.split()
        contact_name = cmdLst[1]
        NewCmd = cmdLst[3:]

        message = ''
        for i in NewCmd:
            message += i + ' '
        # Open WhatsApp using the ms-chat protocol
        os.system("start whatsapp:")
        time.sleep(5)  # Adjust the sleep time as needed
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.typewrite(contact_name)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.typewrite(message)
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.press('enter')

        return f"The message {message} was successfully sent to {contact_name} !"

class MediaPlayerAssistant:
    @staticmethod
    def play_on_youtube(song_name):
        keyword_query = "+".join(song_name.split())
        youtube_url = f"https://www.youtube.com/results?search_query={keyword_query}"
        pyautogui.hotkey("win", "d")
        webbrowser.open(youtube_url)
        time.sleep(5)
        pyautogui.hotkey('win', 'up')
        pyautogui.moveTo(x=700, y=500)
        pyautogui.click(x=700, y=500)
        return f"Playing {song_name} on youtube"

    @staticmethod
    def play_on_spotify(command):
       try:
            cmdLst = command.split()
            NewCmd = cmdLst[1:-2]
            songName = ''
            for i in NewCmd:
               songName += i + ' '
            pyautogui.hotkey("win", "d")
            os.startfile("spotify:")
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'k')
            pyautogui.typewrite(songName)
            time.sleep(3)
            pyautogui.hotkey('shift', 'enter')
            time.sleep(1)
            return f"{songName} was successfully played on spotify"
       except:
           webbrowser.open(f"https://open.spotify.com/search/{songName}")
           return f"{songName} was successfully played on spotify"

class apps_websites_opener:
    def open_website(command):
        global Link_commands
        website_name = command.split()[1].lower()
        if website_name in Link_commands:
            website_link = Link_commands[website_name]
            try:
                if validators.url(website_link):
                    webbrowser.open(website_link)
                    return f"{website_name} opened successfully"

                else:
                    return "Invalid website link"

            except Exception as e:
                return f"Error opening website: {e}"
    def open_apps(command):
        global app_commands
        alias_name = command.split('open')[1]
        app_name = command.split()[1]
        if app_name in app_commands:
            app_path = app_commands[app_name]
            try:
                os.startfile(app_path)
                return f"Opening {alias_name}"
            except Exception as e:
                return f"Error opening {alias_name}: {e}"

class UserNameWindow:
    def __init__(self):
        self.user_name = None
        self.root = tk.Tk()

    def save_and_close(self):
        self.user_name = self.entry.get()
        self.root.destroy()

    def move_window(self, event):
        self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    def get_user_name(self):
        self.root.title("Fill to Continue")
        self.root.geometry("400x250")  # Increased window height
        self.root.overrideredirect(True)  # Turns off title bar, geometry

        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width - 400) / 2)
        y_coordinate = int((screen_height - 250) / 2)
        self.root.geometry(f"400x250+{x_coordinate}+{y_coordinate}")

        # Set a custom color scheme
        pale_black = "#303030"
        pale_gray = "#f0f0f0"
        white = "#ffffff"
        black = "#000000"

        self.root.configure(bg=pale_black)
        self.root.tk_setPalette(background=pale_black, foreground=white, activeBackground=white, activeForeground=pale_black)

        # Set the window icon
        self.root.iconbitmap("CYBOT.ico")

        # Create a custom title bar frame with the specified color
        title_bar = tk.Frame(self.root, bg='black', relief='raised', bd=2)
        title_bar.pack(expand=1, fill="x", pady=0)  # Removed extra space above the title bar

        # Create a label on the title bar
        title_label = tk.Label(title_bar, text="Fill to Continue", bg='black', fg=white, font=("Arial", 10))
        title_label.pack(side="left", padx=5)

        # Create a label in the window with increased font size
        window_label = tk.Label(self.root, text="Enter your name!", bg=pale_black, fg=white, font=("Arial", 16))
        window_label.pack(pady=5)

        # Create an entry widget with the specified color
        self.entry = tk.Entry(self.root, width=40, bg=pale_gray, fg=black, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Automatically focus on the entry field when the window opens
        self.entry.focus()

        # Create a save button with increased font size and black text color
        save_button = tk.Button(self.root, text="Save", command=self.save_and_close, bg=pale_gray, fg=black,
                                font=("Arial", 12))
        save_button.pack(pady=10)

        # Bind the Enter key to the save_and_close function
        self.root.bind('<Return>', lambda event=None: self.save_and_close())

        # Disable window resizing
        self.root.resizable(False, False)

        # Bind title bar motion to the move_window function
        title_bar.bind('<B1-Motion>', self.move_window)

        # Only display the exit button on the title bar
        exit_button = tk.Button(title_bar, text='X', command=self.root.destroy, bg='black', fg=white)
        exit_button.pack(side="right")

        # Run the GUI
        self.root.mainloop()

        # After the window is closed, 'user_name' will contain the entered value
        return self.user_name



# Example usage:
if __name__ == "__main__":
    #MediaPlayerAssistant.play_on_spotify("play varaaga nadhikarai on spotify")
    ur = UserNameWindow()
    urn = ur.get_user_name()
    print(urn)
'''
    # YouTube example
    youtube_assistant = MediaPlayerAssistant()
    youtube_assistant.play_on_youtube("Despacito")



    # Spotify example
    spotify_assistant = MediaPlayerAssistant()
    spotify_assistant.play_on_spotify("Shape of You")'''


