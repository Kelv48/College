import tkinter as tk

class MsPint(object):

    def __init__(self):
        self._root = tk.Tk()
        self._root.title("MS Pint")
        self._current_shape = "line"
        self._p1 = None
        self._p2 = None
        self._color = "red"

        self._right_frame = tk.Frame(self._root, width=1000, height=800, bg="black")
        self._canvas = tk.Canvas(self._right_frame, bg="white", width=1200, height=800)
        self._right_frame.grid(row=0, column=1, padx=5, pady=5)
        self._canvas.grid(row=0, column=0, padx=5, pady=5)


        self._left_frame = tk.Frame(self._root, width=150, height=1000, bg="black")
        self._left_frame.grid(row=0, column=0, padx=5, pady=5)
        self._left_frame.grid_propagate(False)

        self.create_menu()
        self._canvas.bind("<Button-1>", self.mouse_click)

        self._root.mainloop()

    def create_menu(self):
        self.destroy_widgets()


        width = 15
        fontSize = 15
        col = 0
        paddingY = 10

        colorsButton = tk.Button(self._left_frame, text="Colors", font=("arial", fontSize), width=width, bg="white", command=self.display_colors)
        colorsButton.grid(row=0, column=col, pady=paddingY)

        shapesButton = tk.Button(self._left_frame, text="Shapes", font=("arial", fontSize), width=width, bg="white", command=self.displayShapes)
        shapesButton.grid(row=1, column=col, pady=paddingY)

        clearButton = tk.Button(self._left_frame, text="Clear", font=("arial", fontSize), width=width, bg="white", command=self.clearCanvas)
        clearButton.grid(row=2, column=col, pady=paddingY)

        current_shape = tk.Label(self._left_frame, text="Current Shape: " + self._current_shape)
        current_shape.grid(row=3, column=col, pady=paddingY)

        currentColor = tk.Label(self._left_frame, text="Current Color: " + self._color)
        currentColor.grid(row=4, column=col, pady=paddingY)

    def display_colors(self):
        self.destroy_widgets()
        
        width = 15
        fontSize = 15
        col = 0
        paddingY = 10
        height = 3

        back_button = tk.Button(self._left_frame, text="Back", font=("arial", fontSize), width=width, bg="white", command=self.create_menu)
        back_button.grid(row=0, column=col, pady=paddingY)
        red_button = tk.Button(self._left_frame, text="Red", height=height, width=width, bg="white", command=self.set_red)
        red_button.grid(row=1, column=col, pady=paddingY)
        blue_button = tk.Button(self._left_frame, text="Blue", height=height, width=width, bg="white", command=self.set_blue)
        blue_button.grid(row=2, column=col, pady=paddingY)
        yellow_button = tk.Button(self._left_frame, text="Yellow", height=height, width=width, bg="white", command=self.set_yellow)
        yellow_button.grid(row=3, column=col, pady=paddingY)
        green_button = tk.Button(self._left_frame, text="Green", height=height, width=width, bg="white", command=self.set_green)
        green_button.grid(row=4, column=col, pady=paddingY)
        black_button = tk.Button(self._left_frame, text="Black", height=height, width=width, bg="white", command=self.set_black)
        black_button.grid(row=5, column=col, pady=paddingY)

    def displayShapes(self):
        #display shapes, line, rectangle, oval
        self.destroy_widgets()
        col = 0
        paddingY = 10
        fontSize = 15
        width = 18

        back_button = tk.Button(self._left_frame, text="Back", font=("arial", fontSize), width=width, bg="white", command=self.create_menu)
        back_button.grid(row=0, column=col, pady=paddingY)
        line_button = tk.Button(self._left_frame, text="Line", font=("arial", fontSize), width=width, bg="white", command=self.set_line)
        line_button.grid(row=1, column=col, pady=paddingY)
        rectangle_button = tk.Button(self._left_frame, text="Rectangle", font=("arial", fontSize), width=width, bg="white", command=self.set_rectangle)
        rectangle_button.grid(row=2, column=col, pady=paddingY)
        oval_button = tk.Button(self._left_frame, text="Oval", font=("arial", fontSize), width=18, bg="white", command=self.set_oval)
        oval_button.grid(row=3, column=col, pady=paddingY)

    def set_red(self):
        self.destroy_widgets()
        self._color = "red"
        self.create_menu()
    def set_blue(self):
        self.destroy_widgets()
        self._color = "blue"
        self.create_menu()
    def set_yellow(self):
        self.destroy_widgets()
        self._color = "yellow"
        self.create_menu()
    def set_green(self):
        self.destroy_widgets()
        self._color = "green"
        self.create_menu()
    def set_black(self):
        self.destroy_widgets()
        self._color = "black"
        self.create_menu()

    def set_line(self):
        self.destroy_widgets()
        self._current_shape = "line"
        self.create_menu()
    def set_rectangle(self):
        self.destroy_widgets()
        self._current_shape = "rectangle"
        self.create_menu()
    def set_oval(self):
        self.destroy_widgets()
        self._current_shape = "oval"
        self.create_menu()
    
    def mouse_click(self, event):
        if not self._p1: 
            self._p1 = (event.x, event.y)
        elif self._p1 and not self._p2:
            self._p2 = (event.x, event.y)

        if self._p1 and self._p2:
            if self._current_shape == "line":
                self._canvas.create_line(self._p1[0], self._p1[1], self._p2[0], self._p2[1], fill=self._color)
            elif self._current_shape == "rectangle":
                self._canvas.create_rectangle(self._p1[0], self._p1[1], self._p2[0], self._p2[1], fill=self._color)
            elif self._current_shape == "oval":
                self._canvas.create_oval(self._p1[0], self._p1[1], self._p2[0], self._p2[1], fill=self._color)
            self._p1 = None
            self._p2 = None

    def clearCanvas(self):
        self._canvas.create_rectangle(0, 0, 1000, 800, fill="white")

    def destroy_widgets(self):
        for widget in self._left_frame.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    MsPint()