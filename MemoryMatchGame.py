#MemoryMatchGame.py
from tkinter import Tk, messagebox, Button, DISABLED, Frame, Label, OptionMenu, StringVar
from PIL import Image, ImageTk
import random, time


def get_img(full_path):
    image = Image.open(full_path)
    image.thumbnail((150, 150), Image.LANCZOS)
    return ImageTk.PhotoImage(image)
    
root = Tk() # creates a new tkinter window
root.title('Memory Match Game')
root.resizable(width = False, height = False)


# Set the window position
window_x = 300  # X-coordinate of the window position
window_y = 28  # Y-coordinate of the window position
root.geometry(f"+{window_x}+{window_y}")
buttons = {} # dict to store the buttons
first = True # it checks if symbol is the first match

# this two keeps track of the button last pressed
previousX = 0
previousY = 0
moves = 0
pairs = 0

button_dict = {}

all_images = ['attack-titan.png', 'boy.png', 'catgirl.png', 'dragon.png', 'erza.png', 'goku-big.png', 'goku-small.png', 'gungirl.png', 
'hitachi.png', 'hot-bunny.png', 'ken-kanaki.png', 'luffy.png', 'midoriya.png', 'naruto.png', 'nezuko.png', 'redhair.png', 
'sasuke.png', 'sexy-girl.png', 'shy-girl.png', 'sword-girl.png', 'warrior.png', 'zero-two.png', 'zoro.png']

image_list = (random.sample(all_images, 12) * 2)
random.shuffle(image_list)


# x and y tells which button has been pressed as x is column no and y is row no for that particular button
def show_symbol(x, y): 
    global first, previousX, previousY, moves, pairs

    # Show the image
    buttons[x, y].config(image=button_dict[x, y])
    buttons[x, y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
        moves += 1
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY].image_path != buttons[x, y].image_path:
            time.sleep(0.5)
            buttons[previousX, previousY].config(image=default_image)
            buttons[x, y].config(image=default_image)
        else:
            buttons[previousX, previousY].config(state=DISABLED)
            buttons[x, y].config(state=DISABLED)
            pairs += 1
            if pairs == len(buttons) / 2:
                messagebox.showinfo('Matching', f'Number of moves: {str(moves)}')
                root.destroy()
        first = True
        

        

# Preload Images
image_cache = {}
for image_path in image_list:
    full_path = './img/' + image_path
    if full_path not in image_cache:
        photo = get_img(full_path)
        image_cache[full_path] = photo

default_image = get_img('./img/blue-tile.jpg')

frame = Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0)
for x in range(6):
    for y in range(4):
        button = Button(
            frame,
            command=lambda x=x, y=y: show_symbol(x, y),
            width=150,
            height=150,
            image=default_image,
            borderwidth=5,
            relief='ridge'
        )
        button.grid(column=x, row=y)
        buttons[x, y] = button
        image_path = './img/' + image_list.pop()
        button_image = image_cache[image_path]
        button_dict[x, y] = button_image
        button.image_path = image_path

root.iconphoto(False, get_img("./img/memory-icon.png"))

root.mainloop()
