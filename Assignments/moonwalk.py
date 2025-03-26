import tkinter as tk
from PIL import Image, ImageTk

# Create the Tkinter window
root = tk.Tk()
root.title("Running Dog GIF on Moonwalk GIF")

# Set the window size
root.geometry("800x600")

# Set the background color to RGB(248, 210, 74)
root.configure(bg='#F8D94A')

# Load the Moonwalk GIF (Michael Jackson's Moonwalk)
moonwalk_gif = Image.open('moonwalk.gif')
moonwalk_frames = []
for frame in range(0, moonwalk_gif.n_frames):
    moonwalk_gif.seek(frame)
    moonwalk_frame = ImageTk.PhotoImage(moonwalk_gif.copy())  # Convert each frame to Tkinter-compatible format
    moonwalk_frames.append(moonwalk_frame)

# Load the Dog GIF
dog_gif = Image.open('dog.gif')  # Replace with your dog GIF file path
dog_frames = []
for frame in range(0, dog_gif.n_frames):
    dog_gif.seek(frame)
    dog_frame = ImageTk.PhotoImage(dog_gif.copy())  # Convert each frame to Tkinter-compatible format
    dog_frames.append(dog_frame)

# Create a canvas to display the images
canvas = tk.Canvas(root, width=800, height=600, bg='#F8D94A')
canvas.pack()

# Create a label widget to display the Moonwalk GIF frames as background
moonwalk_label = tk.Label(root)
moonwalk_label.place(x=0, y=0)

# Function to update the Moonwalk GIF animation in the background
def play_moonwalk_gif(frame_index=0):
    moonwalk_label.config(image=moonwalk_frames[frame_index])  # Update the label with the current Moonwalk frame
    next_frame_index = (frame_index + 1) % len(moonwalk_frames)  # Loop through frames
    root.after(100, play_moonwalk_gif, next_frame_index)

# Start the Moonwalk GIF animation in the background
play_moonwalk_gif()

# Function to animate the dog running on the Moonwalk GIF
def move_dog(x=50, dog_frame_index=0):
    canvas.delete("dog")  # Clear previous dog position

    # Draw the dog at the new position
    canvas.create_image(x, 250, image=dog_frames[dog_frame_index], tags="dog")

    # Update the dog's GIF frame
    next_dog_frame_index = (dog_frame_index + 1) % len(dog_frames)  # Loop through the dog's frames
    root.after(100, move_dog, x + 5, next_dog_frame_index)  # Move the dog after 50ms

    # Stop the dog when it reaches the end of the screen
    if x < 750:
        root.after(50, move_dog, x + 5, next_dog_frame_index)  # Continue moving the dog
    else:
        canvas.delete("dog")  # Clear the dog after it reaches the end

# Start the dog movement
move_dog()

# Run the Tkinter main loop
root.mainloop()
