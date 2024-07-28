# Image Encryption and Decryption Tool
This project is a Python application that provides a graphical user interface (GUI) for encrypting and decrypting images through basic pixel manipulation. Using Python's powerful libraries such as Tkinter and Pillow, this tool offers an easy-to-use platform for users to secure their image data by modifying pixel values based on a user-defined shift value.

## Features
1. **Image Encryption:** Allows users to load an image and apply a numeric "shift" to encrypt it. The encryption process involves modifying the RGB values of each pixel, which secures the image content against unauthorized access.
2. **Image Decryption:** Facilitates the decryption of previously encrypted images by applying the inverse of the original shift value, restoring the image to its original state.
3. **Interactive File Handling:** Users can open and save images directly through the GUI, providing a seamless experience for encrypting and decrypting images.
4. **User-Friendly Interface:** The application features a simple and intuitive interface that makes it accessible for both technical and non-technical users.

## Technical Details
- **Programming Language:** Python
- **GUI Framework:** Tkinter, used for creating the graphical interface.
- **Image Processing Library:** Pillow (PIL), used for image handling operations like opening, modifying, and saving images.
- **Pixel Manipulation:** Adjusts the RGB values of each pixel by a shift value entered by the user, effectively encrypting and decrypting the image.

## How to Use
**Prerequisites**
Make sure you have Python and the necessary libraries installed:

pip install Pillow
Running the Application
Clone this repository, navigate to the directory containing the project, and run the following command:
python image_encryption_decryption.py

**Getting Started**
**Start the Application:** Run the script to open the GUI.

## Encrypt an Image:
- Click "Open Image to Encrypt" to load your image.
- Enter a shift value.
- Click "Encrypt Image" to apply the encryption.
- Optionally, save the encrypted image using "Save Encrypted Image".

## Decrypt an Image:
- Click "Open Image to Decrypt" to load an encrypted image.
- Enter the correct shift value used during encryption.
- Click "Decrypt Image" to restore the original image.
- View the decrypted image in the GUI.

## Contributions
Contributions are welcome! If you have suggestions or enhancements, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.



