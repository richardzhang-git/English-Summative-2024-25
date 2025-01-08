import tkinter as tk
import tkmacosx as tkm

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

def rgbToHex(values):
    s = "#"
    for num in values:
        digit1 = num//16
        digit2 = num-digit1*16
        s += HEX_DIGITS[digit1] + HEX_DIGITS[digit2]
    return s

def transition(win):
    global scr, buttons, canvas_array


def transitionMain():
    global scr, buttons, canvas_array
    for widget in buttons:
        widget.destroy()
    for canvas in canvas_array:
        canvas.destroy()
    f = tk.Frame(scr, bg=rgbToHex(INDIGO))
    f.pack()
    for i in range(5):
        b = tkm.Button(f, text="325 BC", font="arial 20 bold", bg=rgbToHex(BLUE), fg=rgbToHex(WHITE), height=100, width=100, borderless=True)
        b.grid(row=0, column=i)
        buttons.append(b)

def updateWindow():
    global scr, scr_location, buttons, canvas_array
    if scr_location == "Main":
        for button in buttons:
            button.grid_forget()
        transitionMain()


buttons = []
canvas_array = []
scr_location = "Main"
scr = tk.Tk()
scr.geometry('800x600')
scr.title("Mathematical Identity")
scr.config(bg=rgbToHex(INDIGO))
center(scr)
updateWindow()
while True:
    scr.update()