# QR Code Generator

This Python project generates QR codes from URLs using the `qrcode` library. The generated QR codes are saved as PNG files.

## Features

- Generate a QR code from any URL.
- Customize the output file name.
- Simple command-line interface.

## Requirements

- Python 3.x
- `qrcode` library (install via pip)

## Installation

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/AmrasYavetil/QRtoWebpage.git
    ```

2. Install the required Python package:

    ```bash
    pip install qrcode
    ```

## Usage

1. Run the script:

    ```bash
    python qrcode_generator.py
    ```

2. Enter the URL when prompted:

    ```
    Enter the URL to encode in the QR code: https://example.com
    ```

3. Enter a name for your QR code image:

    ```
    Enter the name for your QR Code PNG (file extension .png will be added for you): my_qrcode
    ```

4. The QR code will be generated and saved as `my_qrcode.png` in the current directory.

## Example

Running the script and entering `https://example.com` as the URL with `my_qrcode` as the file name will produce a file named `my_qrcode.png` in the same directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or ideas!
