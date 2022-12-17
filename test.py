import tkinter as tk


root = tk.Tk()
root.geometry('200x200')

def newWindow():
    second = tk.Tk()
    second.geometry('300x300')
    second.mainloop()

btn = tk.Button(root,text='click me', command=newWindow)
btn.pack()

root.mainloop()