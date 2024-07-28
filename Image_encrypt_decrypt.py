import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def open_image_encrypt():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        global original_img
        original_img = Image.open(file_path)
        display_image(original_img, original_image_label)

def open_image_decrypt():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        global encrypted_img
        encrypted_img = Image.open(file_path)
        display_image(encrypted_img, selected_encrypted_image_label)

def save_image(image, title):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")], title=title)
    if file_path:
        image.save(file_path)
        messagebox.showinfo("Saved Encrypted Image", f"Image saved as {file_path}")

def display_image(image, label):
    img = image.copy()
    img.thumbnail((500, 500))
    img_tk = ImageTk.PhotoImage(img)
    label.configure(image=img_tk)
    label.image = img_tk

def encrypt_image():
    if original_img is None:
        messagebox.showerror("Error", "Please select an image first.")
        return
    try:
        shift = int(encrypt_shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")
        return

    encrypted_img = original_img.copy()
    width, height = encrypted_img.size
    for x in range(width):
        for y in range(height):
            r, g, b = encrypted_img.getpixel((x, y))
            r = (r + shift) % 256
            g = (g + shift) % 256
            b = (b + shift) % 256
            encrypted_img.putpixel((x, y), (r, g, b))
    display_image(encrypted_img, encrypted_image_label)
    global encrypted_image
    encrypted_image = encrypted_img

def decrypt_image():
    if encrypted_img is None:
        messagebox.showerror("Error", "Please select an encrypted image first.")
        return
    try:
        shift = int(decrypt_shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")
        return

    decrypted_img = encrypted_img.copy()
    width, height = decrypted_img.size
    for x in range(width):
        for y in range(height):
            r, g, b = decrypted_img.getpixel((x, y))
            r = (r - shift) % 256
            g = (g - shift) % 256
            b = (b - shift) % 256
            decrypted_img.putpixel((x, y), (r, g, b))
    display_image(decrypted_img, decrypted_image_label)


#GUI using Tkinter
root = tk.Tk()
root.title("Image Encryption Decryption")
root.configure(bg="#f0f0f0")

original_img = None
encrypted_img = None

header_label = tk.Label(root, text="Image Encryption and Decryption", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# Encryption 
encrypt_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
encrypt_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")
encrypt_title = tk.Label(encrypt_frame, text="Encryption", font=("Helvetica", 14, "bold"), bg="white")
encrypt_title.grid(row=0, column=0, columnspan=2, pady=10)
tk.Button(encrypt_frame, text="Open Image to Encrypt", command=open_image_encrypt, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5)
original_image_label = tk.Label(encrypt_frame, bg="white", bd=2, relief="groove")
original_image_label.grid(row=2, column=0, columnspan=2, padx=2, pady=5)
tk.Label(encrypt_frame, text="Shift Value", font=("Helvetica", 12), bg="white").grid(row=3, column=0, padx=10, pady=5)
encrypt_shift_entry = tk.Entry(encrypt_frame, font=("Helvetica", 12))
encrypt_shift_entry.grid(row=3, column=1, padx=10, pady=5)
tk.Button(encrypt_frame, text="Encrypt Image", command=encrypt_image, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
encrypted_image_label = tk.Label(encrypt_frame, bg="white", bd=2, relief="groove")
encrypted_image_label.grid(row=5, column=0, columnspan=2, padx=2, pady=5)
tk.Button(encrypt_frame, text="Save Encrypted Image", command=lambda: save_image(encrypted_image, 'Save Encrypted Image'), bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Decryption 
decrypt_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
decrypt_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")
decrypt_title = tk.Label(decrypt_frame, text="Decryption", font=("Helvetica", 14, "bold"), bg="white")
decrypt_title.grid(row=0, column=0, columnspan=2, pady=10)
tk.Button(decrypt_frame, text="Open Image to Decrypt", command=open_image_decrypt, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5)
selected_encrypted_image_label = tk.Label(decrypt_frame, bg="white", bd=2, relief="groove")
selected_encrypted_image_label.grid(row=2, column=0, columnspan=2, padx=2, pady=5)
tk.Label(decrypt_frame, text="Shift Value", font=("Helvetica", 12), bg="white").grid(row=3, column=0, padx=10, pady=5)
decrypt_shift_entry = tk.Entry(decrypt_frame, font=("Helvetica", 12))
decrypt_shift_entry.grid(row=3, column=1, padx=10, pady=5)
tk.Button(decrypt_frame, text="Decrypt Image", command=decrypt_image, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
decrypted_image_label = tk.Label(decrypt_frame, bg="white", bd=2, relief="groove")
decrypted_image_label.grid(row=5, column=0, columnspan=2, padx=2, pady=5)
root.mainloop()
