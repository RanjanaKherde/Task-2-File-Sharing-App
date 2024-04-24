#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

class FileSharingApp:
    def __init__(self, master):
        self.master = master
        master.title("File Sharing App")

       
        self.username = "admin"
        self.password = "password"
        self.logged_in = False

       
        self.upload_button = ttk.Button(master, text="Upload File", command=self.upload_file)
        self.upload_button.grid(row=0, column=0, padx=5, pady=5)

        self.download_button = ttk.Button(master, text="Download File", command=self.download_file)
        self.download_button.grid(row=0, column=1, padx=5, pady=5)

        self.authenticate_button = ttk.Button(master, text="Login", command=self.authenticate)
        self.authenticate_button.grid(row=0, column=2, padx=5, pady=5)

       
        self.uploaded_files = []

       
        self.auth_window = tk.Toplevel(master)
        self.auth_window.title("Login")
        self.auth_window.geometry("200x100")

        self.username_label = ttk.Label(self.auth_window, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(self.auth_window)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = ttk.Label(self.auth_window, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(self.auth_window, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.login_button = ttk.Button(self.auth_window, text="Login", command=self.check_credentials)
        self.login_button.grid(row=2, columnspan=2, padx=5, pady=5)

    def authenticate(self):
        self.auth_window.deiconify()

    def check_credentials(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username == self.username and entered_password == self.password:
            self.logged_in = True
            messagebox.showinfo("Login", "Login successful")
            self.auth_window.withdraw()
        else:
            messagebox.showerror("Login", "Invalid username or password")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

    def upload_file(self):
        if self.logged_in:
            file_path = filedialog.askopenfilename()
            if file_path:
                file_name = os.path.basename(file_path)
                self.uploaded_files.append(file_name)
                messagebox.showinfo("Upload", f"File '{file_name}' uploaded successfully")
        else:
            messagebox.showerror("Authentication", "Please log in to upload files")

    def download_file(self):
        if self.logged_in:
            if self.uploaded_files:
                file_name = filedialog.askchoice("Download", "Choose a file to download", choices=self.uploaded_files)
                if file_name:
                    messagebox.showinfo("Download", f"File '{file_name}' downloaded successfully")
            else:
                messagebox.showerror("Download", "No files available for download")
        else:
            messagebox.showerror("Authentication", "Please log in to download files")
    def main():
        root = tk.Tk()
        app = FileSharingApp(root)
        root.mainloop()

    if __name__ == "__main__":
            main()


# In[ ]:




