# Image Steganography Tool (Use PNG)

This project is an image steganography tool that allows you to hide a secret message within an image file. Steganography is the practice of concealing information within another medium to avoid detection. This tool uses image steganography to embed a message within the pixels of an image.

Features

- Encode a message: Hide a secret message within an image.
- Decode a message: Extract the hidden message from an image.

Requirements

- Python 3.x
- PIL (Pillow)

Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/jdomon12/Steganography.git
    cd Steganography
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  
    ```

3. Install the required packages:

    ```sh
    pip install pillow
    ```

Usage

Encode a message:

    ```sh
    python steganography.py
    ```

    When prompted:
    - Enter the path to the image file you want to use for encoding.
    - Enter the secret message you want to hide.
    - Enter the path where the new image with the encoded message should be saved.

    Example:

    ```plaintext
    Encode (e) or Decode (d) a message? e
    Enter the path to the image: /path/to/image.png
    Enter the message to encode: Secret message
    Enter the output image path: /path/to/encoded_image.png
    ```

Decode a message:

    ```sh
    python steganography.py
    ```

    When prompted:
    - Enter the path to the image file that contains the hidden message.

    Example:

    ```plaintext
    Encode (e) or Decode (d) a message? d
    Enter the path to the image: /path/to/encoded_image.png
    ```

