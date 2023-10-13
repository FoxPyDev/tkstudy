
def say_hello():
    print("hello")

import tkinter as tk
win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title("Test GUI3")

btn1 = tk.Button(win, text='Hello',
                 command=say_hello
                 )


btn1.pack()

tk.mainloop()
