import tkinter as tk

win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title("Test GUI2")

label_1 = tk.Label(win, text='Hello!\nWorld!',
                   bg='red',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=40,
                   width=20,
                   height=10,
                   anchor='sw',
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.CENTER
                   )
label_1.pack()

win.mainloop()