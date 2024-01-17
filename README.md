<!-- Project Title -->
# M.A.L.A.R - Model for Adaptive Learning and Automated Responses

M.A.L.A.R is an AI-powered chatbot created using Python with various functionalities. It's designed to make your interaction seamless and efficient by performing a wide range of tasks.

## Project Directory Structure
M.A.L.A.R - Model for Adaptive Learning and Automated Responses
├── venv - root
├── CsvFiles
│ ├── commands.csv - app name and path
│ ├── Links.csv - website name and its links
│ └── tasks.csv
├── GenImages - all the images generated
├── myenv
├── Sounds
│ ├── alarmtone.mp3
│ ├── Listening.mp3
│ ├── Startup.mp3
│ └── timer.mp3
├── text files
│ ├── malarPrompt.txt - prompt of the text gen for malar
│ ├── PrimaryUserName.txt - user name
│ └── userdata.txt - the chats of the user and malar
├── venv
├── AppInteractions
├── Clock
├── CYBOT.ico
├── Greetings
├── ImageGen
├── Malar
├── NewsFeed
├── requirements.txt
├── Response
├── Speaker
├── TaskManager
└── WindowsOpen



## Features

- **Time and Date Extraction:** Ask M.A.L.A.R about the current time, date, or both.
  - Example: `<Hey Malar, what's the time?>`

- **Image Generation:** Generate various images using specific commands.
  - Example: `<Generate an image of an unknown alien>`

- **Text Generation:** Interact with M.A.L.A.R by asking questions or engaging in a conversation.
  - Example: `<Hey, what is your name?>`

- **Websites and Apps Opening:** Open websites or apps using simple commands.
  - Examples: `<Launch Google>` or `<Open WhatsApp>`

- **Media Player Control:** Play music on Spotify or YouTube.
  - Examples: `<Play Rasathi Unnai on Spotify>` or `<Play Rasathi Unnai on YouTube>`

- **WhatsApp Messaging:** Send messages on WhatsApp effortlessly.
  - Example: `<Message Karthi that I am busy right now>`

- **Task Management:** Set tasks and get information about your daily tasks.
  - Examples: `<Set a task on Jan 5 that I want to go to the mall at 10 pm>` or `<Hey Malar, do I have any tasks today?>`

- **Alarm and Timer Setting:** Set alarms and timers for your convenience.
  - Examples: `<Set an alarm at 8 pm>` or `<Set a timer for 5 minutes>`

- **Shutdown Protocol:** Safely shut down your computer with M.A.L.A.R's assistance.
  - Examples: `<Shutdown the computer>` or `<Shutdown the PC>`

- **Weather and News Reports:** Stay informed about the weather and read the latest news.
  - Examples: `<Tell me the weather report>` or `<Read top 5 news of today from India>`

- **Image Authenticity Check:** Verify if an image is real or AI-generated.
  - Examples: `<Can you check if an image is real or fake>` or `<Original or fake image>`

## API Keys

Make sure to obtain API keys for the following services:

- **Image Generation APIs:**
  - [API 1](https://api-inference.huggingface.co/models/goofyai/3d_render_style_xl)
  - [API 2](https://api-inference.huggingface.co/models/goofyai/Leonardo_Ai_Style_Illustration)
  - [API 3](https://api-inference.huggingface.co/models/goofyai/cyborg_style_xl)

- **News API:** [newsapi.org](https://newsapi.org/)

- **Voice API:** [elevenlabs.io](https://elevenlabs.io/)

- **Weather API:** [open-meteo.com](https://open-meteo.com/)

- **Image Authenticity API:** [API](https://api-inference.huggingface.co/models/Nahrawy/AIorNot)

## Installation

1. Clone the repository.
2. Install the required dependencies: `pip install -r requirements.txt`.
3. Add API keys to the appropriate locations.

## Usage

Run the `malar.py` file to start interacting with M.A.L.A.R.

## Contributors

- HARI PRASATH AS

## License

This project is licensed under the MIT License - see the (LICENSE.txt) file for details.

