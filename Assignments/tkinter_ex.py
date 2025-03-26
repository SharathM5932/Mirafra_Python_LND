import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Single-Line Text Box")

# Create a single-line text box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Function to display the entered text
def show_text():
    entered_text = entry.get()
    print("Entered Text:", entered_text)

# Button to trigger the display of the text
submit_button = tk.Button(root, text="Submit", command=show_text)
submit_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
