# Hand Gesture Recognition Project

## Description
This project detects hand gestures using real-time webcam video.  
It counts the number of fingers and identifies basic gestures like **Fist**, **One**, **Two**, **Three**, **Four**, and **Five**.  
The project uses the **MediaPipe** library for hand landmark detection and **OpenCV** for video processing.

## Source Code
- `hand_gesture.py` : Main Python script that starts the webcam, detects hands, counts fingers, and displays the gesture on the screen.

## Required Libraries
- `opencv-python`
- `mediapipe`

## Installation
1. Install Python 3.11.9 on your system.
2. Open a terminal or command prompt in the project folder.
3. Run the command:


pip install opencv-python mediapipe



## How to Run
1. Open Terminal/Command Prompt and navigate to the project folder.
2. Run the command:


python hand\_gesture.py


3. The webcam will turn on, and the screen will show the finger count and gesture.
4. To exit the program, press the **`q`** key on your keyboard.

## Dataset
No external dataset is required for this project.  
The input source is the **live feed from the webcam**.

## Notes
- Ensure your webcam is properly connected.
- Run the code on a **local machine** only.
- Webcam window may not work in **online IDEs**.

---

**Happy Coding! 🎉**
