import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        password_label.config(text="Please enter a valid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    
    password_label.config(text="Generated Password: " + generated_password)

# Create a tkinter window
window = tk.Tk()
window.title("Password Generator")

# Label for instructions
instruction_label = tk.Label(window, text="Enter the desired length of the password:")
instruction_label.pack()

# Entry field for password length
length_entry = tk.Entry(window)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
password_label = tk.Label(window, text="")
password_label.pack()

# Start the tkinter main loop
window.mainloop()
