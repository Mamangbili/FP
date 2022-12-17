import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import io as IO
from main import * 

class MyApp:
    filedialog : IO
    header : list
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('300x300')

        self.frame1 = tk.Frame(self.root)
        self.frame1_label = tk.LabelFrame(self.frame1, text='Pilih File')
        self.frame1.pack()

        self.text_pilih = tk.Label(self.frame1,text="Pilih File CSV :",padx=40)
        self.btnPilih = tk.Button(self.frame1,text="File",command=self.btn_Pilih)
        self.text_path = tk.Label(self.frame1)
        self.text_pilih.grid(row=0,column=0)
        self.btnPilih.grid(row=0,column=1)
        self.text_path.grid(row=1,column=0)

        self.comboBox = ttk.Combobox(self.frame1,values='')
        self.root.mainloop()
    
    def btn_tabel(self,column):
        branch = tk.Tk()
        data = extract_kolom(self.filedialog)




    def btn_Pilih(self):
        self.filedialog = fd.askopenfile(filetypes=(('CSV Files','.csv',),))
        self.header :list = next(self.filedialog).split(',')
        self.filedialog.close()
        self.comboBox['value'] = self.header

        cmbColumn = self.comboBox.get()
        indexColumn = self.header.index(cmbColumn)

        btnAnalisis = tk.Button(text='Tampilkan Tabel', command=lambda : self.btn_tabel(indexColumn) )
        self.comboBox.grid(row=2,column=0)
        btnAnalisis.grid(row=3,column=1)




