import tkinter as tk
from tkinter import ttk

paragraph_elements = []
class ScrollableFrame():
    def __init__(self, container, height, width, *args, **kwargs):
        canvas = tk.Canvas(container, highlightbackground="white")
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        paragraph_elements.append(self.scrollable_frame)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        paragraph_elements.append(canvas)
        scrollbar.pack(side="right", fill="y")
        paragraph_elements.append(scrollbar)