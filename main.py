import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import filedialog as fd
from function import * 

class MyApp:
    header : list
    data : list
    path : str
    def __init__(self):
        #--------------------window----------------------------
        self.root = tk.Tk()
        self.root.title("Analisis Cepat Distirbusi Frekuensi")
        #-------------------------------------------------------

        #------------------- frame 1 -----------------------------
        self.frame1 = tk.Frame(self.root)
        self.frame1_label = tk.LabelFrame(self.frame1, text='Pilih File')
        self.frame1.pack(fill='both',expand=1)

        self.text_pilih = tk.Label(self.frame1,text="Pilih File CSV :")
        self.btnPilih = tk.Button(self.frame1,text="Browse",command=self.btn_Pilih)
        self.text_path = tk.Label(self.frame1)
        
        self.text_pilih.pack(padx=150)
        self.btnPilih.pack()
        
        self.btn = tk.Button(self.frame1,text='Analisis Kolom', command=self.on_tabel_buttom)
        
        self.populasi_tx = tk.Label(self.frame1)
        self.comboBox = ttk.Combobox(self.frame1,values='')
        self.table = ttk.Treeview(self.root)
        #------------------------------------------------------------

        #-------------------- frame 2 -------------------------------
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.rata2_tx = tk.Label(self.frame2)
        self.std_tx = tk.Label(self.frame2)

        self.comboBoxVal = ''
        self.tx = tk.Label(self.frame1, text='Kolom dipilih:')
        self.root.mainloop()

    def new_table(self,kolom: int):
        #----------------delete jika ganti kolom analisis-------
        for item in self.table.get_children():
            self.table.delete(item)
        #-------------------------------------------------------

        self.data = extract_kolom(self.file[1:], kolom) #diambil setelah header
        #------------------exception bila column bukan numeric---
        try:
            mean = rata_rata(self.data)
            std = standar_deviasi(self.data, mean)
        except:
            messagebox.showerror( title='Column Error',message='Error: Kolom bukan numeric!')
        #--------------------------------------------------------

        tabelDistribusi = kelas_dan_frequensi(
                kelas(self.data
                    ,rentang_kelas(self.data)
                    ,banyak_kelas(self.data)),
                self.data)
        #-------------------table header--------------------------
        self.table['columns'] = ('Kelas','Frekuensi')
        self.table.column('#0',stretch=tk.NO, width=0)
        self.table.column('Kelas',anchor=tk.CENTER, width=300)
        self.table.column('Frekuensi',anchor=tk.CENTER, width=100)

        self.table.heading('#0', text='',anchor=tk.CENTER)
        self.table.heading('Kelas', text='Kelas',anchor=tk.CENTER)
        self.table.heading('Frekuensi', text='Frekuensi',anchor=tk.CENTER)
        #---------------------------------------------------------

        #------------------table insert---------------------------
        for i,(_kelas,frequensi) in enumerate(tabelDistribusi.items()):
            self.table.insert(parent='',index='end',iid=i,text='', values =(f'({_kelas[0]}, {_kelas[1]})',frequensi))
        #---------------------------------------------------------

        #----------------pack tampilkan widget ke GUI-------------
        self.populasi_tx.configure(text=f'Populasi : {sum(tabelDistribusi.values())}')
        self.rata2_tx.configure(text=f'Rata-rata : {mean}')
        self.std_tx.configure(text=f'Standar Deviasi: {std}')
        self.populasi_tx.pack()
        self.table.pack()
        self.rata2_tx.grid(row=0,column=0)
        self.std_tx.grid(row=0,column=1)
        #---------------------------------------------------------
        

    def btn_Pilih(self):
        #-----------------path file--------------------------------
        filedialog = fd.askopenfilename(filetypes=(('CSV Files','.csv',),))
        #----------------------------------------------------------
        self.file = load_csv(filedialog)
        self.header :list = self.file[0]
        self.text_path.configure(text=filedialog)
        
        #----------------tampilkan GUI comboBox dan text-----------
        self.text_path.pack()
        self.tx.pack()
        self.comboBox.configure(values=self.header)
        self.comboBox.pack()
        self.btn.pack()
        #----------------------------------------------------------
             

    def on_tabel_buttom(self):

        self.populasi_tx.configure(text='')
        self.rata2_tx.configure(text='')
        self.std_tx.configure(text='')
        self.comboBoxVal = self.comboBox.get()
        self.index = self.header.index(self.comboBoxVal)
        self.tx.pack()
        self.new_table(self.index)

    
if __name__ == '__main__':
    MyApp()
