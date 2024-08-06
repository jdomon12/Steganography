from PIL import Image

def encode_message(image_path, message, output_path):
    image = Image.open(image_path)
    encoded = image.copy()
    width, height = image.size
    message += chr(0)  # Add a null character to signify the end of the message
    message_bits = ''.join([f'{ord(c):08b}' for c in message])
    bit_index = 0

    for row in range(height):
        for col in range(width):
            if bit_index >= len(message_bits):
                break
            pixel = list(image.getpixel((col, row)))
            for n in range(3):
                if bit_index < len(message_bits):
                    pixel[n] = pixel[n] & ~1 | int(message_bits[bit_index])
                    bit_index += 1
            encoded.putpixel((col, row), tuple(pixel))
        if bit_index >= len(message_bits):
            break

    encoded.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def decode_message(image_path):
    image = Image.open(image_path)
    width, height = image.size
    message_bits = ''
    message = ''

    for row in range(height):
        for col in range(width):
            pixel = image.getpixel((col, row))
            for n in range(3):
                message_bits += str(pixel[n] & 1)
                if len(message_bits) % 8 == 0:
                    char = chr(int(message_bits[-8:], 2))
                    if char == chr(0):
                        print(f"Decoded bits: {message_bits}")
                        return message
                    message += char

    print(f"Decoded bits: {message_bits}")
    return message

if __name__ == "__main__":
    choice = input("Encode (e) or Decode (d) a message? ")
    if choice.lower() == 'e':
        image_path = input("Enter the path to the image: ")
        message = input("Enter the message to encode: ")
        output_path = input("Enter the output image path: ")
        encode_message(image_path, message, output_path)
    elif choice.lower() == 'd':
        image_path = input("Enter the path to the image: ")
        decoded_message = decode_message(image_path)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice.")
