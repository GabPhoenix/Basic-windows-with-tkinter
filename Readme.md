# Basic windows with tkinter <br>
## This project is just what you need to create windows, to see project acess on my github "login windows tkinter" and the real projects <br><br>

> Splash root <br>
> Login root <br>
> Main root <br>

#### It's the basics tou need to create a simple project using Tkinter. I used concepts from OOP but you can delete this part from the code deleting the class, deleting the function "splash root" and the "self.". <br>

#### Starting with a Splash Root (I put a color just to see it), after 3 seconds the window call a login root <br>

#### Login root will close the splash root <br>

#### Main root: I create the main window but don't call it cause when you build the login root you can call using a button <br><br>
~~~ python
button = tk.button(window)
button.configure(command=action)

def action(self):
    if entry_password = "admin": 
        #call main root
        self.main_root()
~~~ 
#### In main root you need close the login root using<br><br>
~~~ python
self.login.destroy()
~~~ 

#### Also, you can organize it better, with a class for every window but my purpose is help you with a simple project 
