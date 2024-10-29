#Password is Duranta

import ctypes
import os
import tkinter as tk
from tkinter import filedialog, messagebox

PASSWORD = "Duranta"

def change_wallpaper(image_path):
    if not os.path.isfile(image_path):
        messagebox.showerror("Error", "The specified image file does not exist.")
        return
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        messagebox.showinfo("Success", f"Wallpaper changed to:\n{image_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_image():
    password = password_entry.get()
    if password != PASSWORD:
        messagebox.showerror("Error", "Incorrect password!")
        return
    file_path = filedialog.askopenfilename(title="Select Wallpaper", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        change_wallpaper(file_path)

def reset_password():
    global PASSWORD
    current_password = password_entry.get()
    if current_password != PASSWORD:
        messagebox.showerror("Error", "Incorrect current password!")
        return
    new_password = tk.simpledialog.askstring("Reset Password", "Enter new password:", show="*")
    confirm_password = tk.simpledialog.askstring("Confirm Password", "Re-enter new password:", show="*")
    if new_password and confirm_password:
        if new_password == confirm_password:
            PASSWORD = new_password
            messagebox.showinfo("Success", "Password successfully changed!")
        else:
            messagebox.showerror("Error", "Passwords do not match!")

root = tk.Tk()
root.title("CanvasSwitch")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#34495E")

title_label = tk.Label(root, text="CanvasSwitch", font=("Arial", 24, "bold"), fg="#ECF0F1", bg="#34495E")
title_label.pack(pady=(20, 10))

password_label = tk.Label(root, text="Enter Password:", font=("Arial", 12), fg="#ECF0F1", bg="#34495E")
password_label.pack(pady=(10, 5))
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=(0, 20))

select_button = tk.Button(root, text="Select Wallpaper", command=select_image, font=("Arial", 14), bg="#2980B9", fg="#FFFFFF", padx=20, pady=10, relief="raised")
select_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Password", command=reset_password, font=("Arial", 12), bg="#E74C3C", fg="#FFFFFF", padx=10, pady=5, relief="raised")
reset_button.pack(pady=10)

footer_label = tk.Label(root, text="Choose an image to set as your wallpaper", font=("Arial", 12), fg="#BDC3C7", bg="#34495E")
footer_label.pack(side=tk.BOTTOM, pady=20)

for widget in root.winfo_children():
    widget.pack_configure(padx=10)

root.mainloop()
