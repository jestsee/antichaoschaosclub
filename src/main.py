# main.py
import graph as g
import os

# directory
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
os.chdir('test')

# inisialisasi boolean
acyclic = False
g.printAC3()
exit = False

# input nama file
namafile = input("\n\n     Masukkan nama file : ")

## arr adalah array yang berisi nama matkul dari file txt (masih ada duplikasi)
arr = []
g.readWords(namafile,arr)

## arrmatkul berisi semua nama matkul (sudah tidak ada duplikasi)
arrmatkul = [""] #indeks 0 diisi dengan ""
for c in arr:
    if c not in arrmatkul:
        arrmatkul.append(c)

jum = len(arrmatkul)
## MEMBUAT ARRAY DARI [0...jum]
key = [0 for i in range(jum)]
for i in range(jum):
    key[i] = i

## MEMBUAT DICTIONARY
# CONTOH : {1 : "Kalkulus", 2 : "Basdat"}
map = {} #dictionary
for nomor, matkul in zip(key,arrmatkul): 
    map[nomor] = matkul
#print(map)

# inisialisasi
edges = []
g.readToMakeEdges(namafile, edges, map)

# generate graph
graphnya = g.Graph(edges,len(arrmatkul))

# mencetak hasil
print("\n     Rencana kuliah yang dihasilkan : ")
#g.printResult(graphnya,key, map)
level = []
perlevel = []
#g.printResult(graphnya, key, map) -- tidak rekursif
g.printResult2(graphnya, key, map) # menggunakan versi rekursif