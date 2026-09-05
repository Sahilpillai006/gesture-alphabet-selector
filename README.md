# Gesture Alphabet Selector

A computer vision hobby project that uses hand tracking to create a gesture controlled circular A to Z alphabet selector.

The project uses a webcam to track the index finger and determines which letter of the circular alphabet the user is pointing toward. Hand gestures are then used to enter letters, add spaces, or clear the current word.

## How It Works

The webcam captures the user's hand.

MediaPipe Hands detects the hand landmarks.

The position of the index finger is used to calculate an angle around the circular alphabet selector.

That angle determines the currently highlighted letter.

Gestures are used to interact with the selector:

| Gesture | Action |
|---|---|
| Index finger | Add the selected letter |
| Index + middle finger | Add a space |
| Closed fist | Clear the current word |

The selected letters are displayed on screen to form a word in real time.

## Features

- Real time hand tracking
- Circular A to Z alphabet interface
- Gesture based letter selection
- Space gesture
- Clear word gesture
- Live webcam visualization
- Hand landmark visualization

## Technologies

- Python
- OpenCV
- MediaPipe
- NumPy

## Requirements

- Python 3
- Webcam
- OpenCV
- MediaPipe
- NumPy

## Installation

Clone the repository and install the required Python packages:

```bash
pip install opencv-python mediapipe numpy