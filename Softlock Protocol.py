# SoftLock Protocol

import tkinter as tk

class PasswordScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("SoftLock Protocol")
        
        # Create the password entry field
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=10)
        
        # Create the submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_password)
        self.submit_button.pack(pady=5)
        
        # Create the status label
        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack(pady=10)
        
    def check_password(self):
        password = self.password_entry.get()
        if password == "S0ftL0ck":
            self.status_label.config(text="The password you have entered is correct.")
            self.master.after(2000, self.close_window)
            self.master.after(2000, self.open_blank_window)
        else:
            self.status_label.config(text="The password that has been entered is incorrect, please try again.")
    
    def close_window(self):
        self.master.destroy()
    
    def open_blank_window(self):
        new_window = tk.Tk()
        new_window.title("Blank Window")
        new_window.geometry("300x200")
        new_window.mainloop()

root = tk.Tk()
password_screen = PasswordScreen(root)
root.geometry("300x200+500+300")
root.mainloop()
