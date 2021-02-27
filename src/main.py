#main2.py

# INPUT DARI FILE
import graph5 as g

namafile = input("Masukkan nama file : ")
## BACA FILE - BIKIN ARRAY DAFTAR MATKUL
''' benerin buat kasus 1 nama matkul yang terdiri dari 2 kata 
dipisahin spasi (SOLVED)'''
def readWords(x,y):
    with open(x,'r') as f:
        for line in f:
            # hapus spasi disekitar koma
            cleanedline = line.replace(' ,', ',') 
            cleanedline2 = cleanedline.replace(', ',',')
            # hapus titik
            cleanedline3 = cleanedline2.replace('.','')
            y += cleanedline3.rstrip().split(',')


def getKey(val, my_dict):
    for key, value in my_dict.items():
         if (val == value):
             return key
             break

arr = []
arr2 = []
readWords(namafile,arr)
#print(arr)

arrmatkul = [""]
for c in arr:
    if c not in arrmatkul:
        arrmatkul.append(c)
print(arrmatkul)

jum = len(arrmatkul)
## MEMBUAT ARRAY DARI [0...JUM]
key = [0 for i in range(jum+1)]
for i in range(jum+1):
    key[i] = i

## MEMBUAT DICTIONARY
# CONTOH : {1 : "Kalkulus", 2 : "Basdat"}
map = {} #dictionary
for nomor, matkul in zip(key,arrmatkul): 
    map[nomor] = matkul
print(map)
#print(map[1])
#print(getKey("Basis data",map))

######## CREATE EDGE LIST ########
def readToMakeEdges(filename, edge, map):
    filepath = filename
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        countcomma = 0
        countword = 0
        pertama = 0
        kedua = 0
        while line: #selama di suatu baris

            # hapus spasi disekitar koma
            cleanedline = line.replace(' ,', ',') 
            cleanedline2 = cleanedline.replace(', ',',')
            # hapus titik
            cleanedline3 = cleanedline2.replace('.','')
            countcomma = cleanedline.count(",")
            #countword = len(cleanedline.split())
            if(countcomma>0):
                print("jumlah koma = "+ str(countcomma))
                print("Baris {}: {}".format(cnt, cleanedline3.strip()))
                cnt += 1

                # klo koma 1 berarti 2 matkul
                # koma 2 ada 3 matkul
                # n matkul = n koma + 1

                # buat ambil kata pertama dan kedua = [0] & [1]
                # buat ambil kata pertama dan ketiga = [0] & [2]
                for i in range(1,countcomma+1):
                    pertama = getKey(cleanedline3.split(",")[0].strip(),map)
                    kedua = getKey(cleanedline3.split(",")[i].strip(),map)
                    edge.append((pertama,kedua))
                print(cleanedline3.split(",")[0].strip())
            line = fp.readline()

pinggir = []
readToMakeEdges(namafile, pinggir, map)
print(pinggir)

graphnya = g.Graph(pinggir,len(arrmatkul))
g.printAllTopologicalOrders(graphnya, map)