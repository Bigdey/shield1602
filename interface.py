import customtkinter as ctk
from tkinter import messagebox

import main  # Import the main script

class ArduinoInterface(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Arduino Message Sender")
        self.geometry("400x300")

        # COM Port Entry
        self.port_label = ctk.CTkLabel(self, text="Serial Port:")
        self.port_label.pack(pady=5)
        self.port_entry = ctk.CTkEntry(self)
        self.port_entry.pack(pady=5)
        self.port_entry.insert(0, "COM6")  # Default COM port

        # First Line Message Entry
        self.line1_entry = ctk.CTkEntry(self, width=150, validate="key", validatecommand=(self.register(self.validate_input), "%S", "%d"))
        self.line1_entry.pack(pady=5)

        # Second Line Message Entry
        self.line2_entry = ctk.CTkEntry(self, width=150, validate="key", validatecommand=(self.register(self.validate_input), "%S", "%d"))
        self.line2_entry.pack(pady=5)

        # Send Button
        self.send_button = ctk.CTkButton(self, text="Send Message", command=self.send_message)
        self.send_button.pack(pady=20)

    def validate_input(self, char, action):
        """
        Validate input to allow only up to 16 characters and handle deletions.

        :param char: The character to validate.
        :param action: Action type ('1' for insertion, '0' for deletion).
        :return: 'True' if the character is allowed; otherwise 'False'.
        """
        entry = self.focus_get()  # Get the currently focused entry
        current_text = entry.get()
        if action == '1':  # Insertion
            if len(current_text + char) <= 16:
                return True
            return False
        elif action == '0':  # Deletion
            return True
        return False

    def send_message(self):
        port = self.port_entry.get()
        line1_message = self.line1_entry.get()
        line2_message = self.line2_entry.get()

        # Ensure both lines are exactly 16 characters long
        line1_message = line1_message.ljust(16)[:16]
        line2_message = line2_message.ljust(16)[:16]

        # Merge the two lines with a newline character
        message = f'{line1_message}{line2_message}'

        # Initialize serial connection and send the message
        ser = main.initialize_serial_connection(port)
        if ser:
            main.send_message(ser, message)
            main.close_serial_connection(ser)
            messagebox.showinfo("Success", "Message sent successfully.")
        else:
            messagebox.showerror("Error", "Failed to initialize serial connection.")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = ArduinoInterface()
    app.mainloop()
