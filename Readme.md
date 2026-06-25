# Simple Color Detection and Tracking

A real-time color detection and tracking application built using Python, OpenCV, and Pillow (PIL). The project captures video from a webcam, dynamically calculates HSV color boundaries for a target color, isolates the color using image masking, and draws a bounding box around the detected object in real-time.

---

## Features

* **Live Webcam Feed:** Captures and processes real-time frames using OpenCV.
* **Automatic Mirror Correction:** Inverts the Y-axis (`cv2.flip`) so the camera feed feels like a natural mirror.
* **Dynamic HSV Color Mapping:** Uses a helper utility (`get_limits`) to convert standard color spaces into safe HSV ranges, filtering out shadows and background noise.
* **Object Bounding Boxes:** Converts pixel masks into precise coordinates using `Pillow`'s bounding box calculation (`getbbox()`) to draw sharp tracking outlines.

---

## Project Structure

```text
Color Detection/
│
├── main.py          # Main application loop and frame rendering
├── utils.py         # Dynamic HSV threshold calculations
└── requirements.txt # Python package dependencies
```

## Requirements and Usage

Make sure your virtual environment is active before installing dependencies.

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

Run the program from your terminal:

```bash
python main.py
```

#### Exit: Press the 'q' key on your keyboard to stop the webcam feed and close all windows safely
