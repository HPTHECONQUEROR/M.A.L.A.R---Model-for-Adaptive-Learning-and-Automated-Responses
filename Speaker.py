import requests
from io import BytesIO
import pygame
import time

class TextToSpeechPlayer:
    def __init__(self):
        self.url = "https://api.elevenlabs.io/v1/text-to-speech/z9fAnlkpzviPz146aGWa"

    def play_text(self, text):
        headers = {
            "Accept": "audio/mpeg",
            "xi-api-key": "1b890c48b99c8b6f4168f623abaeaa7f",
            "Content-Type": "application/json"
        }

        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 1.0,
                "similarity_boost": 0.5
            }
        }

        response = requests.post(self.url, json=data, headers=headers)

        if response.status_code == 200:
            mp3_data = BytesIO(response.content)

            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_data)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
        else:
            print("Error: Unable to fetch audio")

if __name__ == "__main__":
    player = TextToSpeechPlayer()
    print('மலர் : ' + "Boss how are you?")
    player.play_text('''
Once upon a time, in a realm far beyond the veil of ordinary existence, there existed a mystical land bathed in ethereal light and pulsating with magic. This extraordinary world was a canvas of wonder, where fantastical creatures roamed free, enchanted forests whispered secrets, and cities shimmered like jewels against the backdrop of an ever-changing sky.

In the heart of this enchanting realm lived a young girl named Seraphina. With eyes the color of the clearest sapphire and hair that flowed like liquid silver, she was an orphan raised by a community of wise elves in the hidden sanctuary of Eldoria.''')