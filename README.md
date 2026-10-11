# Computer Vision with OpenCV

A beginner-friendly collection of small Python scripts that teach the basics of
**Computer Vision** using [OpenCV](https://opencv.org/). Each file focuses on a
single idea, from opening an image to detecting a face in a live webcam feed.

If you have never used OpenCV before, start at the top of the list below and work
your way down. Each example builds on the previous one.

---

## What is Computer Vision?

Computer Vision is the field of teaching computers to "see" — to read, process,
and understand images and video. OpenCV is the most popular library for this in
Python, and every example here uses it.

---

## What You Need Before Starting

- **Python 3.8 or newer** — check with `python --version`
- **pip** (comes with Python) — check with `pip --version`
- A code editor such as [PyCharm](https://www.jetbrains.com/pycharm/) or VS Code
- A **webcam** (only needed for the face-detection example)

---

## Installation

1. **Clone or download this project**

   ```bash
   git clone https://github.com/paiiDev/computer-vision.git
   cd computer-vision
   ```

2. **Create a virtual environment** (keeps your packages tidy)

   ```bash
   python -m venv .venv
   ```

3. **Activate it**

   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (cmd): `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`

4. **Install the required packages**

   ```bash
   pip install opencv-python numpy matplotlib
   ```

   | Package             | What it does                                  |
   | ------------------- | --------------------------------------------- |
   | `opencv-python`     | Image and video processing (the star of the show) |
   | `numpy`             | Fast number/matrix math that powers images    |
   | `matplotlib`        | Displays images in a plot window              |

---

## The Scripts (Start Here)

Run any script from the project folder with:

```bash
python <script_name>.py
```

### 1. `reading_image.py` — Open and show an image

The "Hello World" of computer vision. Loads an image and displays it.

- `cv2.imread('images/atomic-habits-dots.png', 1)` → loads the image in color
  (use `0` for grayscale, `-1` to keep transparency).
- `cv2.imshow(...)` opens a window.
- `cv2.waitKey(0)` waits until you press a key.
- `cv2.destroyAllWindows()` closes the window.

**Try it:** press any key to close the window.

### 2. `using_matplot.py` — Show an image with Matplotlib

Same idea, but displays the image using Matplotlib instead of OpenCV.

> Heads up: OpenCV stores colors as **BGR** (Blue-Green-Red) while Matplotlib
> expects **RGB**. So colors may look wrong here — a great lesson in why the
> order matters!

### 3. `writing_image.py` — Save an image

Loads an image as grayscale, shows it, and **saves a copy** when you press `s`.

- `cv2.imwrite("images/xss.png", img)` writes the image to disk.

**Try it:** run it, press `s`, then look for `images/xss.png`.

### 4. `writing_image_test.py` — Save then read it back

Proves the saved file actually works: press `s` to save, and it immediately
re-opens the saved image in a second window.

### 5. `Bitwise_image.py` — Bitwise operations on pixels

Demonstrates how to combine two images pixel-by-pixel using **AND**, **OR**,
**XOR**, and **NOT**. Press `Esc` to close the windows.

- `cv2.bitwise_and` — keeps pixels where both images have brightness.
- `cv2.bitwise_or` — keeps pixels where either image has brightness.
- `cv2.bitwise_xor` — keeps pixels where only one image has brightness.
- `cv2.bitwise_not` — inverts each pixel.

> Note: this script expects `images/x.png`. If that file is missing, add it to
> the `images/` folder or change the filename in the code.

### 6. `bitwise_and.py` — Put a logo on a photo (image masking)

A classic technique: paste one image (a logo) onto another using **masks** and a
**region of interest (ROI)**. This is how image editing apps blend layers.

It uses two images: the background (`atomic-habits-dots.png`) and the logo
(`pupl.png`). The mask tells OpenCV exactly which pixels to copy.

### 7. `lab_test.py` — Real-time face detection (webcam)

The finale! Opens your webcam and draws a box around every face it sees, live.

- It loads a pre-trained model: `haarcascade_frontalface_default.xml`.
- Each video frame is converted to grayscale, scanned for faces, and annotated
  with a blue rectangle and the label "Human Face".

**Try it:** run it, look at the camera, and press `q` to quit.

---

## Project Structure

```
PythonProject/
├── images/                          # Sample images used by the scripts
│   ├── atomic-habits-dots.png       # Background image
│   ├── pupl.png                     # Logo image
│   └── xss.png                      # Output saved by writing_image.py
├── reading_image.py                 # 1. Read & display an image
├── using_matplot.py                 # 2. Display with Matplotlib
├── writing_image.py                 # 3. Save an image
├── writing_image_test.py            # 4. Save then re-read an image
├── Bitwise_image.py                 # 5. Bitwise AND/OR/XOR/NOT
├── bitwise_and.py                   # 6. Image masking / overlay a logo
├── lab_test.py                      # 7. Webcam face detection
├── haarcascade_frontalface_default.xml  # Pre-trained face model
├── main.py                          # Default PyCharm starter file (ignore)
└── README.md                        # You are here
```

---

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `ModuleNotFoundError: No module named 'cv2'` | Run `pip install opencv-python` (make sure your virtual environment is active). |
| Image window opens and freezes | That's expected — press any key. The window is waiting for you. |
| Colors look wrong in `using_matplot.py` | Normal! OpenCV uses BGR, Matplotlib uses RGB. |
| `error: (-215:Assertion failed)` on `imread` | The image path is wrong. Run the script from the project folder so `images/...` resolves correctly. |
| Webcam doesn't open in `lab_test.py` | Close other apps using the camera, and check your OS camera permissions. |
| Face not detected | Use good lighting and face the camera directly. Haar cascades are not perfect. |

---

## Key Concepts You'll Learn

- Loading, displaying, and saving images
- Color spaces (grayscale vs. BGR vs. RGB)
- Handling keyboard input in OpenCV windows
- Bitwise pixel operations and masks
- Overlaying / compositing images
- Reading a live webcam feed frame by frame
- Using a pre-trained model for face detection

---

## License

This project is for learning purposes. Feel free to use and modify it.
