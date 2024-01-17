import datetime
import time
import pygame
import threading

class Clock:
    @staticmethod
    def play_sound(audiofile):
        pygame.mixer.init()
        pygame.mixer.music.load(audiofile)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    def set_alarm(self, command):
        for i in command:
            if ord(i) >= 48 and ord(i) <= 57:
                index = command.find(i)
                break

        p = command[index:-5]
        f = p.split(':')
        minute = int(f[1])
        indicator = command[-4:]
        hour = int(f[0])

        if indicator.lower() == "p.m." and hour != 12:
            hour, minute = str((str(hour + 12) + p[2:-5] + f":{minute}")).split(":")
            hour,minute = int(hour), int(minute)

        elif indicator.lower() == "a.m." and hour == 12:
            hour, minute = str("00" + p[2:-5] + f":{minute}").split(':')
            hour,minute = int(hour), int(minute)

        else:
            hour, minute = str(str(hour).zfill(2) + p[2:-5] + f":{minute}").split(":")
            hour,minute = int(hour), int(minute)

        alarm_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)

        # Start a new thread for alarm
        threading.Thread(target=self._wait_for_alarm, args=(alarm_time,)).start()
        return f"Alarm set at {hour} hours and {minute} minutes, boss, anything else?"

    def set_timer(self, command):
        num1 = command.find("for")
        if "minutes" in command:
            num2 = command.find("minutes")
        else:
            num2 = command.find("minute")
        minutes = int(command[num1 + 3:num2])
        seconds = minutes * 60
        threading.Thread(target=self._wait_for_timer, args=(seconds,)).start()
        return f"Timer set for {minutes} minutes boss, is there anything else!?"

    def _wait_for_alarm(self, alarm_time):
        current_time = datetime.datetime.now()

        while current_time < alarm_time:
            time.sleep(1)
            current_time = datetime.datetime.now()

        Clock.play_sound("Sounds/alarmtone.mp3")

    def _wait_for_timer(self, seconds):
        time.sleep(seconds)

        Clock.play_sound("Sounds/timer.mp3")

if __name__ == "__main__":
    clock = Clock()
    clock.set_alarm("set alarm for 10:11 p.m.")
    clock.set_timer("set timer for 1 minute")