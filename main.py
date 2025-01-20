import tkinter as tk
import time
from tkinter.constants import DISABLED, NORMAL, LEFT
from PIL import ImageTk, Image
from data import *
import random
from scrollFrame import ScrollableFrame, paragraph_elements

INDIGO = (0, 0, 20)
BLUE = (0, 0, 60)
WHITE = (255, 255, 255)
HEX_DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

def blank():
    pass

def center(win): #center a window
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
    win.update()

def rgbToHex(values):
    s = "#"
    for num in values:
        digit1 = num//16
        digit2 = num-digit1*16
        s += HEX_DIGITS[digit1] + HEX_DIGITS[digit2]
    return s

def hexTorgb(string):
    string = string[1:]
    values = [0, 0, 0]
    for i in range(3):
        values[i] += HEX_DIGITS.index(string[0]) * 16 + HEX_DIGITS.index(string[1])
        string = string[2:]
    return values

def transitionOut(pause):
    global scr, c, buttons, canvas_elements, labels
    step = 20
    new_button = list(BLUE)
    new_label = list(WHITE)
    for i in range(step):
        for i in range(3):
            new_label[i] -= (WHITE[i] - INDIGO[i]) // step
        for label in labels:
            c.itemconfig(label, fill=rgbToHex(new_label))
        for i in range(3):
            new_button[i] -= (BLUE[i] - INDIGO[i]) // step
        for button in buttons:
            button.config(bg=rgbToHex(new_button), fg=rgbToHex(new_label))
        scr.update()
        updateAnimation(pause)
    if new_label != INDIGO:
        for label in labels:
            c.itemconfig(label, fill=rgbToHex(INDIGO))
        for button in buttons:
            button.config(fg=rgbToHex(INDIGO))
    if new_button != INDIGO:
        for button in buttons:
            button.config(bg=rgbToHex(INDIGO))

def transitionIn(pause):
    global scr, c, buttons, canvas_elements, labels
    step = 20
    new_button = list(INDIGO)
    new_label = list(INDIGO)
    for i in range(step):
        for i in range(3):
            new_label[i] += (WHITE[i] - INDIGO[i]) // step
        for label in labels:
            c.itemconfig(label, fill=rgbToHex(new_label))
        for thing in canvas_elements:
            c.itemconfig(thing, fill=rgbToHex(new_label))
        for i in range(3):
            new_button[i] += (BLUE[i] - INDIGO[i]) // step
        for button in buttons:
            button.config(bg=rgbToHex(new_button), fg=rgbToHex(new_label))
        scr.update()
        updateAnimation(pause)
    if new_label != WHITE:
        for label in labels:
            c.itemconfig(label, fill=rgbToHex(WHITE))
        for button in buttons:
            button.config(fg=rgbToHex(WHITE))
    if new_button != BLUE:
        for button in buttons:
            button.config(bg=rgbToHex(BLUE))
    scr.update()


def message(message):
    global scr, c
    l = c.create_text(c.winfo_width()/2, c.winfo_height()/2, fill=rgbToHex(INDIGO), text=message, font="optima 15 bold", tags="element")
    labels.append(l)
    transitionIn(0.1)
    transitionOut(0.1)
    labels.remove(l)
    c.delete(l)

def displayIntro():
    global scr, c, buttons, labels
    message("Life is full of changes")
    message("some big, some small")
    message("but changes nonetheless")
    message("and there are some things that change with us")
    message("whether in a day, or in a millennia.")
    updateAnimation(1.5)
    message("This is the story of one of them.")
    updateAnimation(2)
    title1 = c.create_text(c.winfo_width()/2, 150, fill=rgbToHex(INDIGO), text="Mathematical", font="georgia 100 bold", tags="element")
    labels.append(title1)
    title2 = c.create_text(c.winfo_width()/2, 250, fill=rgbToHex(INDIGO), text="Identity", font="{snell roundhand} 100 bold", tags="element")
    labels.append(title2)
    enter = tk.Button(scr, text="Begin", font="{snell roundhand} 40", bg=rgbToHex(INDIGO), fg=rgbToHex(INDIGO), highlightbackground=rgbToHex(INDIGO))
    enter.pack()
    buttons.append(enter)
    scr.update()
    enter.place(x=400-enter.winfo_width()/2, y=400)
    enter.config(command=lambda x=enter: displayMain(x))
    transitionIn(0.1)

def displayMain(enter_button):
    global scr, c, buttons, labels, canvas_elements
    enter_button.config(command=blank)
    transitionOut(0.1)
    for l in labels:
        c.delete(l)
    labels.clear()
    for b in buttons:
        b.destroy()
    buttons.clear()
    for i in range(5):
        b = tk.Button(scr, text=years[i], font="optima 15 bold", bg=rgbToHex(INDIGO), fg=rgbToHex(INDIGO), highlightbackground=rgbToHex(INDIGO), height=2, width=5)
        b.place(x=156 * i + 47.5, y=276)
        scr.update()
        buttons.append(b)
        r = c.create_rectangle(156 * (i) + 125, 295, 156 * (i) + 2003, 305, fill=rgbToHex(INDIGO), width=0, tags="element")
        canvas_elements.append(r)

    transitionIn(0.1)
    for i in range(5):
        buttons[i].config(command=lambda x=i: displayParagraph(x))

def displayParagraph(stage):
    global scr, buttons, labels, canvas_elements, paragraph_elements, images
    new_indigo = []
    new_white = []
    new_blue = []
    for i in range(3):
        new_indigo.append(INDIGO[i] // 2)
        new_white.append(WHITE[i] // 2)
        new_blue.append(BLUE[i] // 2)
    scr.config(bg=rgbToHex(new_indigo))
    for b in buttons:
        b.config(fg=rgbToHex(new_white), bg=rgbToHex(new_blue), highlightbackground=rgbToHex(new_indigo), state=DISABLED)
    display = tk.Frame(scr, bg="white", height=500, width=400)
    display.place(x=200, y=50)
    display.pack_propagate(False)
    paragraph_elements.append(display)
    content = ScrollableFrame(display, height=500, width=400)
    img = tk.Label(content.scrollable_frame, image=images[stage], bd=0)
    img.place(x=0, y=0)
    scr.update()
    #incorporate title into image (custom)
    paragraph = tk.Label(content.scrollable_frame, text=paragraphs[stage], font="optima 15", bg="white", fg="black", anchor="e", justify=LEFT, wraplength=380)
    paragraph.place(x=0, y=img.winfo_height())
    scr.update()
    content.scrollable_frame.config(height=img.winfo_height()+paragraph.winfo_height(), width=400)
    exit_button = tk.Button(display, text="✕", bg="white", fg="black", highlightbackground="white", width=1, height=1, command=exitParagraph)
    exit_button.place(x=355, y=0)
    scr.update()

def updateAnimation(seconds):
    global scr, c, animation_elements
    step = 3
    frequency = 1
    speed = 0.01
    for i in range(int(seconds*100)):
        if random.randint(1, frequency) == 1:
            x_variant =  random.randint(-20, 20)
            y_variant =  random.randint(-20, 20)
            r = c.create_rectangle(400 + x_variant, 300 + y_variant, 401 + x_variant, 301 + y_variant, outline=rgbToHex(INDIGO), tags='0')
            animation_elements.append(r)
        for particle in animation_elements:
            coords = c.bbox(particle)
            if coords[0] > 800 or coords[1] < 0 or coords[2] < 0 or coords[3] > 600:
                c.delete(particle)
                animation_elements.remove(particle)
                continue
            x_increment = (coords[0] + coords[2])/2 - 400
            y_increment = (coords[1] + coords[3]) / 2 - 300
            c.move(particle, x_increment*speed, y_increment*speed)
            if int(c.itemcget(particle, "tags")[0]) % 5 == 0:
                outline = c.itemcget(particle, "outline")
                outline = hexTorgb(outline)
                for i in range(3):
                    if outline[i] < 255:
                        if outline[i] + step > 255:
                            outline[i] = 255
                        else:
                            outline[i] += step
                c.itemconfig(particle, outline=rgbToHex(outline))
            new_tag = int(c.itemcget(particle, "tags")[0]) + 1
            c.itemconfig(particle, tags=str(new_tag))
        c.tag_raise("element")
        scr.update()
        scr.after(1)


def exitParagraph():
    global scr, buttons, labels, canvas_elements, paragraph_elements
    for widget in paragraph_elements:
        widget.destroy()
    scr.config(bg=rgbToHex(INDIGO))
    for b in buttons:
        b.config(fg=rgbToHex(WHITE), bg=rgbToHex(BLUE), highlightbackground=rgbToHex(INDIGO), state=NORMAL)


buttons = []
canvas_array = []
canvas_elements = []
labels = []
scr = tk.Tk()
scr.geometry('800x600')
scr.title("Mathematical Identity")
scr.config(bg=rgbToHex(INDIGO))
center(scr)
c = tk.Canvas(scr, height=600, width=800, bg=rgbToHex(INDIGO), highlightbackground=rgbToHex(INDIGO))
c.place(x=0, y=0)
animation_elements = []

def imgSizing(w, h):
    scale = max(w, h) / 400
    return round(w / scale), round(h / scale)

images = []

for path in image_paths:
    img = Image.open(rf'{path}')
    img = img.resize(imgSizing(img.width, img.height))
    img = ImageTk.PhotoImage(img)
    images.append(img)

scr.update()

displayIntro()
while True:
    updateAnimation(0.01)