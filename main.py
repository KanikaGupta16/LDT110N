import keyboard
import time
import tkinter as tk
from tkinter import PhotoImage

def detect_arrow_keys():
    arrow_keys = ['up', 'down', 'left', 'right']
    held_keys = []

    while True:
        for key in arrow_keys:
            if keyboard.is_pressed(key):
                if key not in held_keys:
                    held_keys.append(key)
            elif key in held_keys:
                held_keys.remove(key)

        if held_keys:
            print(f"Held down keys: {', '.join(held_keys)}")
            held_keys.sort()
            x=run_function_based_on_keys(held_keys)
            print(x)

        time.sleep(0.1) 
        
        
     
def run_function_based_on_keys(held_keys):
    # Implement your logic based on the held keys
    # For example, you can check the order of keys and perform specific actions
    key=['down','right','up']
    if held_keys == key:
        return("Full")
    elif held_keys== ['right','up']:
        return("Level 2")     
    elif held_keys== ['up']:
        return("Level 1")
    elif held_keys == []:
        return("Empty") 
        
# def change_image(path):
#     # Load a new image (change the file path accordingly)
#     new_image_path = path
#     new_image = PhotoImage(file=new_image_path)

#     # Update the image in the label
#     image_label.configure(image=new_image)
#     image_label.image = new_image 
    
    
# root = tk.Tk()
# root.title("Image Display")

# # Load initial image
# current_image = PhotoImage(file="initial_image.png")

# # Create a label to display the image
# image_label = tk.Label(root, image=current_image)
# image_label.pack(pady=10)

# # Create a button to change the image
# change_image_button = tk.Button(root, text="Change Image", command=change_image)
# change_image_button.pack(pady=10)

# # Start the main event loop
# root.mainloop()

while True: 
    detect_arrow_keys() 
    
