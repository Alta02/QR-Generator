# QR Generator
A simple QR Code Generator built with Python and Tkinter. It allows users to input a message and generate a QR Code, which is automatically saved in the `image` folder with a unique filename.

## Features
- User-friendly GUI for generating QR Codes.
- Automatically saves QR Codes with iterated filenames (e.g., `qrcode_1.png`, `qrcode_2.png`).
- Lightweight and easy to use.

## Requirements
- Python 3.x
- Libraries:
  - `qrcode`
  - `Pillow`

## Installation
1. Clone the Repository 
```bash
  git clone https://github.com/Alta02/QR-Generator.git
```
2. Move to the directory
```bash
  cd QR-Generator
```
3. Install the requirement
```bash
pip install -r requirement.txt
```
4. Ensure the image folder exists in the project directory.

## Usage
1. Run the application:
```bash
python src/qr_generator.py
```
2. Enter a message in the input field.
3. Click the "Generate QR Code" button.
4. The QR Code will be saved in the image folder.
