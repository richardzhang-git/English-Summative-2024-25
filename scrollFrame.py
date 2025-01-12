import tkinter as tk

paragraph_elements = []
class ScrollableFrame():
    def __init__(self, container, height, width, *args, **kwargs):
        self.canvas = tk.Canvas(container, highlightbackground="white")
        scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, height=height, width=width, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        paragraph_elements.append(self.scrollable_frame)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind_all("<MouseWheel>", self.onMousewheel)
        self.canvas.pack(side="left", fill="both", expand=True)
        paragraph_elements.append(self.canvas)
        scrollbar.pack(side="right", fill="y")
        paragraph_elements.append(scrollbar)

    def onMousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta)), "units")