# Gesture Alphabet Selector

A computer vision hobby project that uses hand tracking to create a gesture controlled circular A to Z alphabet selector.

The project uses a webcam to track the user’s hand and determines which letter they are pointing toward. Simple hand gestures are then used to enter letters, add spaces, or clear the current word.

---

## Features

* Real time hand tracking
* Circular A to Z alphabet interface
* Gesture based letter selection
* Real time word construction
* Gesture based space insertion
* Gesture based word clearing
* Hand landmark visualization

---

## How It Works

The system uses the webcam to detect a hand using MediaPipe Hands.

The position of the index finger is used to calculate its angle relative to the center of the circular interface. That angle is mapped to one of the 26 letters.

The selected letter is highlighted on screen.

A gesture then determines what happens to the selected letter.

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hands
   ↓
Hand Landmark Detection
   ↓
Index Finger Position
   ↓
Angle Calculation
   ↓
Circular A–Z Selector
   ↓
Gesture Detection
   ↓
Word Output


---

Gesture Controls

Gesture	Action

☝️ Index finger	Add the currently selected letter
✌️ Index + middle finger	Add a space
✊ Closed fist	Clear the current word


The project uses simple gesture states rather than a machine learning model specifically trained for alphabet recognition.


---

Technologies Used

Python

OpenCV

MediaPipe

NumPy

Math



---

Project Structure

gesture-alphabet-selector/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE


---

Requirements

Python 3

Webcam

Working internet connection for installing the required Python packages


Python Libraries

OpenCV

MediaPipe

NumPy



---

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/gesture-alphabet-selector.git

Move into the project directory:

cd gesture-alphabet-selector

Install the required libraries:

pip install -r requirements.txt


---

Usage

Run the program:

python main.py

Allow the application to access your webcam.

Point your index finger around the circular alphabet to select a letter.

Use the supported gestures to construct a word.

Press Esc to exit the application.


---

Limitations

This project is an experimental hobby project and has some limitations:

Letter selection depends on the position of the index finger relative to the circular interface.

Hand detection can be affected by lighting and camera quality.

Only one hand is processed at a time.

The gesture recognition uses simple landmark position checks.

The system is not intended to replace a conventional keyboard or text input system.



---

Future Upgrades

Possible improvements include:

Improve gesture recognition reliability.

Add configurable gesture controls.

Add word suggestions and autocomplete.

Support more advanced text input.

Improve the visual interface.

Add configurable alphabet layouts.

Add support for multiple languages.

Reduce accidental letter selection through gesture stabilization.



---

Project Background

This project was created as a personal hobby experiment to explore computer vision, hand tracking, and alternative methods of human computer interaction.

The main idea was to investigate whether hand position and simple gestures could be combined to create a completely touchless alphabet input interface.


---

Author

Sahil B Pillai

Engineer | Robotics & AI Enthusiast


---

License

This project is open source and available under the MIT License.