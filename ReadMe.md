**_ Training Timer Application _**

## Overview

The Training Timer is a simple yet effective Python application built with Pygame that helps athletes and fitness enthusiasts track their workout intervals. The application features:

- Countdown and count-up timer functionality
- Pre-timer options for preparation time
- Visual feedback with different button states
- Overtime tracking when countdown completes

## Features

# Timer Controls

- Time Selection Buttons: Choose between 2-5 minutes (in 1-minute increments) or 5-35 minutes (in 5-minute increments)
- Pre-Timer Options: Set preparation time in 10-second increments (0s, 10s, 20s, 30s)
- Start/Stop Buttons: Control the timer with dedicated green (start) and red (stop) buttons

## Visual Feedback

- Button hover effects
- "Get Ready" display during pre-timer countdown
- "Overtime" indicator when timer switches to count-up mode
- Real-time FPS display in window title

## Requirements

- Python 3.x
- Pygame library

## Installation

- Ensure you have Python 3 installed
- Install Pygame using pip:
  pip install pygame
- Download or clone the repository containing trainings_timer.py and button.py

## Usage

- Run the application by executing:
  python trainings_timer.py
- Select your desired workout duration using the number buttons
- Optionally set a pre-timer duration
- Click START to begin the timer
- The timer will automatically switch to overtime mode (counting up) when the countdown completes
- Click STOP at any time to pause the timer

## Customization

- You can easily modify the application by editing the source files:
  button.py: Change button colors, sizes, or styles
  trainings_timer.py: Adjust timer ranges, fonts, or screen dimensions

## License

# This project is open-source and available for personal use. For commercial use, please contact the developer.
