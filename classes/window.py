import tkinter


class Window:
    """Class used to generate windows in the application's graphical interface"""

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("may the force be in book")
        self.window.geometry("800x600")
        # Configuring the window resize option
        self.window.resizable(width=True, height=True)

    def run(self):
        self.window.mainloop()

    def stop_app(self):
        self.window.quit()
