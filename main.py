import tkinter as tk
import time
from pydoc import importfile
from tkinter.constants import DISABLED, NORMAL, LEFT
from PIL import ImageTk, Image
from data import *
from scrollFrame import ScrollableFrame, paragraph_elements

INDIGO = (0, 0, 20)
BLUE = (0, 0, 60)
WHITE = (255, 255, 255)
HEX_DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

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

def transitionOut(pause):
    global scr, buttons, canvas_elements, labels
    step = 20
    new_button = list(BLUE)
    new_label = list(WHITE)
    for i in range(step):
        for i in range(3):
            new_label[i] -= (WHITE[i] - INDIGO[i]) // step
        for label in labels:
            label.config(fg=rgbToHex(new_label))
        for i in range(3):
            new_button[i] -= (BLUE[i] - INDIGO[i]) // step
        for button in buttons:
            button.config(bg=rgbToHex(new_button), fg=rgbToHex(new_label))
        scr.update()
        time.sleep(pause)
    if new_label != INDIGO:
        for label in labels:
            label.config(fg=rgbToHex(INDIGO))
        for button in buttons:
            button.config(fg=rgbToHex(INDIGO))
    if new_button != INDIGO:
        for button in buttons:
            button.config(bg=rgbToHex(INDIGO))

def transitionIn(pause):
    global scr, buttons, canvas_elements, labels
    step = 20
    new_button = list(INDIGO)
    new_label = list(INDIGO)
    for i in range(step):
        for i in range(3):
            new_label[i] += (WHITE[i] - INDIGO[i]) // step
        for label in labels:
            label.config(fg=rgbToHex(new_label))
        for i in range(3):
            new_button[i] += (BLUE[i] - INDIGO[i]) // step
        for button in buttons:
            button.config(bg=rgbToHex(new_button), fg=rgbToHex(new_label))
        scr.update()
        time.sleep(pause)
    if new_label != WHITE:
        for label in labels:
            label.config(fg=rgbToHex(WHITE))
        for button in buttons:
            button.config(fg=rgbToHex(WHITE))
    if new_button != BLUE:
        for button in buttons:
            button.config(bg=rgbToHex(BLUE))
    scr.update()


def message(message):
    global scr
    l = tk.Label(scr, text=message, font="optima 15 bold", bg=rgbToHex(INDIGO), fg=rgbToHex(INDIGO))
    labels.append(l)
    l.pack()
    scr.update()
    l.place(x=400-l.winfo_width()/2, y=300-l.winfo_height()/2)
    transitionIn(0.1)
    time.sleep(3)
    transitionOut(0.1)
    labels.remove(l)
    l.destroy()

def displayIntro():
    global scr, buttons, labels
    message("Life is full of changes")
    message("some big, some small")
    message("but changes nonetheless")
    message("and there are some things that change with us")
    message("whether in a day, or in a millennia.")
    time.sleep(1.5)
    message("This is the story of one of them.")
    time.sleep(2)
    title1 = tk.Label(scr, text="Mathematical", font="georgia 50 bold", bg=rgbToHex(INDIGO), fg=rgbToHex(INDIGO))
    title1.pack()
    labels.append(title1)
    title2 = tk.Label(scr, text="Identity", font="{snell roundhand} 50 bold", bg=rgbToHex(INDIGO), fg=rgbToHex(INDIGO))
    title2.pack()
    labels.append(title2)
    enter = tk.Button(scr, text="Begin", font="{snell roundhand} 15", bg=rgbToHex(INDIGO), fg=rgbToHex(INDIGO), highlightbackground=rgbToHex(INDIGO))
    enter.pack()
    buttons.append(enter)
    scr.update()
    title1.place(x=400-title1.winfo_width()/2, y=150)
    title2.place(x=400-title2.winfo_width()/2, y=200)
    enter.place(x=400-enter.winfo_width()/2, y=300)
    enter.config(command=displayMain)
    transitionIn(0.1)

def displayMain():
    global scr, buttons, labels, canvas_elements
    transitionOut(0.1)
    for b in buttons:
        b.destroy()
        buttons.remove(b)
    for l in labels:
        l.destroy()
        labels.remove(l)
    f = tk.Frame(scr, bg=rgbToHex(WHITE), height=600, width=800)
    f.pack()
    c = tk.Canvas(f, height=600, width=800, bg=rgbToHex(INDIGO), highlightbackground=rgbToHex(INDIGO))
    c.place(x=0, y=0)
    for i in range(5):
        b = tk.Button(f, text=years[i], font="optima 15 bold", bg=rgbToHex(INDIGO), fg=rgbToHex(INDIGO),
                      highlightbackground=rgbToHex(INDIGO), height=2, width=5)
        b.place(x=156 * i + 47.5, y=276)
        scr.update()
        buttons.append(b)
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
    for l in labels:
        l.config(fg=rgbToHex(new_white), bg=rgbToHex(new_indigo))
    display = tk.Frame(scr, bg="white", height=500, width=300)
    display.place(x=250, y=50)
    display.pack_propagate(False)
    paragraph_elements.append(display)
    content = ScrollableFrame(display, height=500, width=300)
    img = tk.Label(content.scrollable_frame, image=images[stage], bd=0)
    img.place(x=0, y=0)
    scr.update()
    #incorporate title into image (custom)
    paragraph = tk.Label(content.scrollable_frame, text=paragraphs[stage], font="optima 15", bg="white", fg="black", anchor="e", justify=LEFT, wraplength=280)
    paragraph.place(x=0, y=img.winfo_height())
    scr.update()
    content.scrollable_frame.config(height=img.winfo_height()+paragraph.winfo_height(), width=300)
    exit_button = tk.Button(display, text="✕", bg="white", fg="black", highlightbackground="white", width=1, height=1, command=exit_paragraph)
    exit_button.place(x=255, y=0)
    scr.update()

def exit_paragraph():
    global scr, buttons, labels, canvas_elements, paragraph_elements
    for widget in paragraph_elements:
        widget.destroy()
    scr.config(bg=rgbToHex(INDIGO))
    for b in buttons:
        b.config(fg=rgbToHex(WHITE), bg=rgbToHex(BLUE), highlightbackground=rgbToHex(INDIGO), state=NORMAL)
    for l in labels:
        l.config(fg=rgbToHex(WHITE), bg=rgbToHex(INDIGO))

buttons = []
canvas_array = []
canvas_elements = []
labels = []
scr = tk.Tk()
scr.geometry('800x600')
scr.title("Mathematical Identity")
scr.config(bg=rgbToHex(INDIGO))
center(scr)

def tokenSizing(w, h):
    scale = max(w, h) / 300
    return round(w / scale), round(h / scale)

images = []

for path in image_paths:
    img = Image.open(rf'{path}')
    img = img.resize(tokenSizing(img.width, img.height))
    img = ImageTk.PhotoImage(img)
    images.append(img)

displayIntro()
while True:
    scr.update()