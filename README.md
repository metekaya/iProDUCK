<h1 align="center">
    <img height="120" alt="iProDUCK" src="assets/iProDUCK.ico" />
    <br>
    iProDUCK - Personal Productivity Assistant
</h1>

Welcome to iProDUCK! This application is designed to assist users in improving their productivity by providing various helpful features.

## Features

- **VS Code Usage Tracker**: Monitors the time spent using VS Code and reminds users to take breaks if usage exceeds a certain threshold.
- **Automated File Organizer**: Automatically categorizes and moves downloaded files to designated folders based on file types.
- ~~**Chrome Screen Time Tracker**: Tracks the time spent on specific websites and prompts users to take breaks if the time limit is exceeded.~~ (not done yet)

## Prerequisites

Before you begin, ensure that you have met the following requirements:

- You have installed Python 3.x. If not, you can download it from [here](https://www.python.org/).

## Installation

1. Clone the repository using the following command:\
   `git clone https://github.com/metekaya/iProDUCK.git`
2. Navigate to the project directory and install the necessary dependencies:\
   `cd iProDUCK`\
   `pip install -r requirements.txt`
   **Small Note:** `pyinstaller` may give you an error about the path, make sure you added your python to your os' `PATH`

## Usage

- Copy the `.env.example` file and rename it to `.env` and enter your desired path.
- After installing the necessary dependencies, run the main script to start the iProDUCK productivity assistant.
  `python main.py`
- The application will run in the background and track your vs code time and organize your provided path in `.env` file.
- If you prefer to run the application from the executable file, follow the steps below:
  - Create the executable file using the following command: `pyinstaller --onefile main.py` or if you want to run without the cmd you can add `--noconsole` option.
  - Locate the generated executable file in the `dist` directory.
  - Run the executable file to start the iProDUCK productivity assistant.
  
  **For Windows:** You can run the script on the background whenever you start your system.
    1. Open the "Run" dialog by pressing `Windows key + R`.
    2. Type `shell:startup` and press Enter.
    3. This will open the `Startup` directory.
    4. Copy the executable file (`iProDUCK.exe`) into this directory (also you can copy the shortcut of it).
    5. The application will now start automatically every time you log in to your computer.

Please note that I have no idea how it works on macOS, as I don't own a Mac because I'm not getting paid enough to buy one.. Actually I'm not getting paid at all. HEADHUNTERS pls hire me! If you're using a Mac, you're on your own! (Dont' you dare to tell me to install Linux!!)

## Contact

If you have any questions, suggestions, or feedback, please feel free to reach out to me at [metekaya55@gmail.com](mailto:metekaya55@gmail.com)

---

iProDUCK(I don't know why I named it like that) is built purely to try out my capabilities, it does not hold any copyrights or any kind of permission. Or does it 😈
