import tkinter as tk

class Windows:
    def __init__(self):
        super().__init__()

        # Calling splash root
        self.splash_root()

    def splash_root(self):
        self.splash = tk.Tk()
        self.splash.configure(background="#0F5")

        # it will call the login root after 3 miliseconds (3 seconds)
        self.splash.after(3000, self.login_root)

        self.splash.mainloop()

    

    def login_root(self):
        # it will create the login root and close the splash root 
        self.splash.destroy()

        # window
        self.login = tk.Tk()
        self.login.configure(background="#000")
        self.login.mainloop()


    """I just comment the main login to you build the login root, after you pass for a button 
    as I explain in Readme file."""

    # def main_root(self):
    #     self.main = tk.Tk()
    #     self.main.mainloop()

