# Devlog

A short log of what I did, what broke and what I learned. Newest entries at the top.

## Stage 2: QR code (done)

- Generated the QR code directly on the board with `adafruit_miniqr` instead of loading an image.
- Copied the QR matrix into a 2-colour `displayio.Bitmap` and scaled it up with a `Group(scale=4)`.
- Learned that a QR code needs a quiet zone (empty border) around it, otherwise phones struggle to scan it.
- Recorded the demo video for the README.

## Stage 1: scrolling text (done)

- Put a `label.Label` on top of the pink background.
- Made it scroll by lowering `text.x` by one pixel per frame and resetting it once the text has left the screen on the left.
- Learned to measure the text width with `bounding_box` and multiply it by `scale`.

## Setup (done)

- Flashed CircuitPython with the web installer (BOOT + RST when the board wasn't found).
- Drew a full-screen pink rectangle with `Bitmap`, `Palette`, `TileGrid` and `Group`.
- Hid the status bar with `supervisor.status_bar.display = False`.

## Up next: Stage 3, buttons

- Find out which pins the two buttons are on and how to read them in CircuitPython.
- Figure out debouncing, so one press doesn't count as several.
