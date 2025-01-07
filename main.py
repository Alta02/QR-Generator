import os
import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog

def generate_qr_with_iteration(message, base_filename="qrcode", extension="png"):
    iteration = 1

    while True:
        filename = f"image/{base_filename}_{iteration}.{extension}"
        if not os.path.exists(filename):
            break
        iteration += 1

    # Create QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)

    # Save QR Code as an image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename

def on_generate_qr():
    message = entry_message.get()
    if not message:
        messagebox.showerror("Error", "Message can't be empty!")
        return

    try:
        filename = generate_qr_with_iteration(message)
        messagebox.showinfo("Succsess", f"QR Code Saved as {filename}!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to make QR Code: {e}")

# Setup GUI
root = tk.Tk()
root.title("QR Code Generator")

# Entry for message
label_message = tk.Label(root, text="Input Message:")
label_message.pack(pady=5)

entry_message = tk.Entry(root, width=40)
entry_message.pack(pady=5)

# Button to generate QR Code
btn_generate = tk.Button(root, text="Generate", command=on_generate_qr)
btn_generate.pack(pady=10)

# Run the application
root.mainloop()
