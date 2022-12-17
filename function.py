from csv import *
import math
import functools as ft

def isfloat(str):
    try: 
        float(str)
        return True
    except ValueError: return False

def parse_cell_to_float(_str: str):
    return float(_str) if isfloat(_str) else _str 
    #jika angka diparse menjadi numberic

def column_iterate(_list: list):
    return list(map(parse_cell_to_float, _list))

def load_csv(path):
    with open(path) as io:
        file = reader(io)
        return list(map(lambda x : column_iterate(x) , file))

def rata_rata (data: list):
    return sum(data)/len(data)

def standar_deviasi(data: list[float|int],mean):
    return math.sqrt(sum(map(lambda x:math.pow(x-mean,2), data ))/ len(data) )

def extract_kolom(_table: list, kolom: int):
    return list(map(lambda x: x[kolom], _table))

def rentang_kelas(_data: list[float|int]):
    return (max(_data)-min(_data)) / banyak_kelas(_data)

def banyak_kelas(_data: list[float|int]):
    return round(1+ (3.322*math.log10(len(_data))))

def kelas(data: list[float|int], rentang: float, banyak_kelas: int)->list[float|int]:
    batas_bawah = min(data)
    return list(map(lambda x: (batas_bawah+(x*rentang),batas_bawah+((x+1)*rentang)) if x == 0 else(batas_bawah+0.00001+(x*rentang),batas_bawah+((x+1)*rentang)), range(banyak_kelas)))

def kelas_dan_frequensi(_kelas : list, data: list[float|int]):
    baris = {key:0 for key in _kelas }
    for val in data:
        for key in baris.keys():
            if key[0] <= val <= key[1]: baris[key]+=1
    return baris
