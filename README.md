# QR Code Generator

A simple Python script that generates a QR code from any URL and saves it as a PNG image.

## Features

* Generate a QR code from a URL
* Save the result as a PNG image
* Customize the QR code and background colors
* High error-correction level for reliable scanning

## Requirements

* Python 3
* `qrcode` library
* Pillow image library

## Installation

Clone the repository:

```bash
git clone https://github.com/A0KAMI1/QR_Code_Generator.git
cd QR_Code_Generator
```

Install the required package:

```bash
pip install "qrcode[pil]"
```

## Usage

Open the Python file and replace:

```python
URL_TO_ENCODE = "YOUR_URL"
```

with the URL you want to encode:

```python
URL_TO_ENCODE = "https://www.linkedin.com/company/example"
```

You can also change the output filename:

```python
OUTPUT_FILENAME = "SB_LINKEDIN_qr_code.png"
```

Run the script:

```bash
python qr_code_generator.py
```

The generated QR code will be saved in the same directory.

## Customization

To change the QR code colors, edit this line:

```python
img = qr.make_image(
    fill_color="#000000",
    back_color="white"
)
```

Example:

```python
img = qr.make_image(
    fill_color="#00629B",
    back_color="white"
)
```

## Project Structure

```text
QR_Code_Generator/
├── qr_code_generator.py
├── README.md
└── SB_LINKEDIN_qr_code.png
```

## Author

Created by [A0KAMI1](https://github.com/A0KAMI1).
