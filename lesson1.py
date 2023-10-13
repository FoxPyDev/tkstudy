import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file="image.png")
win.iconphoto(False, photo)
win.config(bg='grey')
win.title("Test GUI")
win.geometry("500x600+50+50")
win.minsize(250, 300)
win.maxsize(1000, 1200)
win.resizable(True, True)

win.mainloop()
