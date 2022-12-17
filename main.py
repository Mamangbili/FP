import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import io as IO
from function import * 

class MyApp:
    header : list
    data : list
    path : str
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Analisis Cepat Distirbusi Frekuensi")

        self.frame1 = tk.Frame(self.root)
        self.frame1_label = tk.LabelFrame(self.frame1, text='Pilih File')
        self.frame1.pack(fill='both',expand=1)

        self.text_pilih = tk.Label(self.frame1,text="Pilih File CSV :")
        self.btnPilih = tk.Button(self.frame1,text="Browse",command=self.btn_Pilih)
        self.text_path = tk.Label(self.frame1)
        
        self.text_pilih.pack(padx=150)
        self.btnPilih.pack()
        self.text_path.pack()
        
        self.btn = tk.Button(self.frame1,text='Analisis Kolom', command=self.on_tabel_buttom)
        self.comboBox = ttk.Combobox(self.frame1,values='')
        self.table = ttk.Treeview(self.root)

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.rata2_tx = tk.Label(self.frame2)
        self.std_tx = tk.Label(self.frame2)

        self.comboBoxVal = ''
        self.tx = tk.Label(self.frame1, text='Kolom dipilih:')
        self.root.mainloop()
    
    def new_table(self,kolom: int):

        for item in self.table.get_children():
            self.table.delete(item)
        
        self.data = extract_kolom(self.file[1:], kolom) #diambil setelah header
        
        mean = rata_rata(self.data)
        std = standar_deviasi(self.data, mean)

        tabelDistribusi = kelas_dan_frequensi(
                kelas(self.data
                    ,rentang_kelas(self.data)
                    ,banyak_kelas(self.data)),
                self.data)

        self.table['columns'] = ('Kelas','Frekuensi')
        self.table.column('#0',stretch=tk.NO, width=0)
        self.table.column('Kelas',anchor=tk.CENTER, width=300)
        self.table.column('Frekuensi',anchor=tk.CENTER, width=100)

        self.table.heading('#0', text='',anchor=tk.CENTER)
        self.table.heading('Kelas', text='Kelas',anchor=tk.CENTER)
        self.table.heading('Frekuensi', text='Frekuensi',anchor=tk.CENTER)
        
        for i,(k,v) in enumerate(tabelDistribusi.items()):
            print(k,'dan', v)
            self.table.insert(parent='',index='end',iid=i,text='', values =(f'({k[0]}, {k[1]})',v))
        
        self.rata2_tx.configure(text=f'Rata-rata : {mean}')
        self.std_tx.configure(text=f'Standar Deviasi: {std}')
        self.table.pack()
        self.rata2_tx.grid(row=0,column=0)
        self.std_tx.grid(row=0,column=1)
 
    def on_tabel_buttom(self):
        self.comboBoxVal = self.comboBox.get()
        self.index = self.header.index(self.comboBoxVal)
        self.tx.pack()
        self.new_table(self.index)

    def btn_Pilih(self):
        filedialog = fd.askopenfilename(filetypes=(('CSV Files','.csv',),))
        self.file = load_csv(filedialog)
        self.header :list = self.file[0]
        self.tx.pack()
        self.comboBox.configure(values=self.header)
        self.comboBox.pack()
             
        self.btn.pack()
        

if __name__ == '__main__':
    MyApp()
