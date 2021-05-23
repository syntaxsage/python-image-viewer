# Import required packages
import os
from tkinter import *
from tkinter.font import BOLD, Font
from PIL import ImageTk, Image

# Create root window
root = Tk()
root.iconbitmap('assets/icons/icon.ico')
root.title("Image Viewer")

# Required functions

## Show previous image
def show_previous_image(image_number):
    # Set global variables
    global button_previous
    global label_image
    global label_status
    global button_next

    # Remove older image object from grid
    label_image.grid_forget()

    # Update objects

    label_image = Label(image=image_list[image_number], 
        width=800, height=600)
    
    ## If there is no image available, disable previous button
    ## Else update previous button
    if (image_number == 0):
        button_previous = Button(root, image=icon_previous_arrow, 
            border=0, state=DISABLED)
    else:
        button_previous = Button(root, image=icon_previous_arrow, 
            border=0, command=lambda: show_previous_image(
                image_number - 1))    
    
    label_status = Label(root, text= str(
        image_number + 1) + " of " + str(len(image_list)), 
            font=('sans-serif', 15))
    button_next = Button(root, image=icon_next_arrow, 
        border=0, command=lambda: show_next_image(
            image_number + 1))

    # Align objects
    label_image.grid(row=0, column=0, columnspan=3)
    button_previous.grid(row=1, column=0)  
    label_status.grid(row=1, column=1)   
    button_next.grid(row=1, column=2)

## Show next image
def show_next_image(image_number):
    # Set global variables
    global button_previous
    global label_image
    global label_status
    global button_next

    # Remove older image object from grid
    label_image.grid_forget()

    # Update objects
    label_image = Label(image=image_list[image_number], 
        width=800, height=600)
    button_previous = Button(root, image=icon_previous_arrow, 
        border=0, command=lambda: 
            show_previous_image(image_number - 1))    
    label_status = Label(root, text= str(
        image_number + 1) + " of " + str(len(image_list)), 
            font=('sans-serif', 15))

    ## If there is no image available, disable next button
    ## Else update next button
    if (image_number == (len(image_list) - 1)):
        button_next = Button(root, image=icon_next_arrow, 
            border=0, state=DISABLED)
    else:
        button_next = Button(root, image=icon_next_arrow, 
            border=0, command=lambda: show_next_image(
                image_number + 1))

    # Align objects
    label_image.grid(row=0, column=0, columnspan=3)
    button_previous.grid(row=1, column=0)
    label_status.grid(row=1, column=1)    
    button_next.grid(row=1, column=2)


# Create image objects

## UI icon objects
icon_previous_arrow_image = Image.open(
    "assets/icons/arrow_back.png").resize((64, 64))
icon_previous_arrow = ImageTk.PhotoImage(icon_previous_arrow_image)
icon_next_arrow_image = Image.open(
    "assets/icons/arrow_next.png").resize((64, 64))
icon_next_arrow = ImageTk.PhotoImage(icon_next_arrow_image)

## Add all images in the folder to the list
files = os.listdir('assets/images')
image_list = []

for file in files:
    file_name = 'assets/images/' + file
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_list.append(image)

# Image object
label_image = Label(image=image_list[0], width=800, height=600)

# Create required buttons, labels
button_previous = Button(root, image=icon_previous_arrow, border=0, 
    state=DISABLED)
label_status = Label(root, text="1 of " + str(len(image_list)), 
    font=('sans-serif', 15))
button_next = Button(root, image=icon_next_arrow, border=0, 
    command=lambda: show_next_image(1))

# Align objects in root window

## Align image
label_image.grid(row=0, column=0, columnspan=3)

## Align buttons, labels
button_previous.grid(row=1, column=0)
label_status.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()
