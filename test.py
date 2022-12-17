import tkinter as tk
from tkinter import ttk
root = tk.Tk()
# root.geometry('200x200')

table = ttk.Treeview(root)
table.grid(row=1,column=1)

table['columns'] = ('1','2','3')
table.column("#0", width=0,  stretch=tk.NO)
table.column("1",anchor=tk.CENTER, width=80)
table.column("2",anchor=tk.CENTER, width=80)
table.column("3",anchor=tk.CENTER, width=80)

table.heading("#0",text="",anchor=tk.CENTER)
table.heading("1",text="P_Name",anchor=tk.CENTER)
table.heading("2",text="P_Gender",anchor=tk.CENTER)
table.heading("3",text="P_Title",anchor=tk.CENTER)

table.insert(parent='',index='end',iid=1,text='',
values=('Todd S Core','Male','Mr'))
table.insert(parent='',index='end',iid=0,text='',
values=('Todd wakwaw','Male','Mr'))
root.mainloop()
