import tkinter


class Window:
    """Class used to generate windows in the application's graphical interface"""

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("bibliotheque des 4 rives")
        self.window.geometry("1500x800")
        self.window.wm_minsize(1600, 800)

    def run(self):
        self.window.mainloop()

    def stop_app(self):
        self.window.quit()
