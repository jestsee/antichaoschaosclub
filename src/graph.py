#graph5.py
import os
acyclic = False

class Graph:

	# Constructor
    # edges itu list of tuple yang bersisian
    # contoh [(2,1),(3,1)] berarti 1 ngarah ke 2, 1 ngarah ke 3
	def __init__(self, edges, N):

		# list dari node yang bertetanggaan
		self.adjList = [[] for _ in range(N)]

		#i inisialisasi derajat masuk dengan 0
		self.indegree = [0] * N
		
		# mengkonversi edges menjadi array daftar dari node yang ditunjuk oleh suatu node
		for (src,dest) in edges: 
			self.adjList[dest].append(src)
			self.indegree[src] = self.indegree[src] + 1


# untuk mencetak angka romawi
# sumber : https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


# mengembalikan array key yang merupakan simpul dengan derajat = 0
def noIndegree(graph):
    no = []
    N = len(graph.adjList)
    for i in range(1,N):
        if graph.indegree[i]==0:
            no.append(i)
            graph.indegree[i] = -99
    return no


# mengembalikan nested array yang berisi
# [[key matkul smt 1],[key matkul smt 2],[key matkul smt ..]]
# topological sort terjadi di sini
def pleaseWork(graph, key):
    global acyclic
    graphnya = graph
    arrkey = key
    level = []
    perlevel = []
    
    # selama arrkey belom kosong
    while len(arrkey)>1 and not acyclic:
        perlevel = noIndegree(graphnya)

        # jika tidak ditemukan yang derajatnya 0 maka dia acyclic
        # proses berhenti
        if len(perlevel) < 1:
            acyclic = True
            level = []
            break
        
        # jika DAG maka dilanjutkan
        else:
            # kurangi semua derajat adjacent dari lv dengan 1
            for lv in perlevel:
                for u in graphnya.adjList[lv]:
                    graphnya.indegree[u] = graphnya.indegree[u] - 1

                # menghapus nilai lv dari arrkey
                arrkey.remove(lv)

            # memasukan array perlevel ke level (nested array)
            level.append(perlevel)
    return(level)


# membaca file txt x dan membuat array of matkul y
def readWords(x,y):
    with open(x,'r') as f:
        for line in f:
            # hapus spasi disekitar koma
            cleanedline = line.replace(' ,', ',') 
            cleanedline2 = cleanedline.replace(', ',',')
            # hapus titik
            cleanedline3 = cleanedline2.replace('.','')
            y += cleanedline3.rstrip().split(',')


## MEMPEROLEH KEY DARI DICT MATKUL
def getKey(val, my_dict):
    for key, value in my_dict.items():
         if (val == value):
             return key
             break


######## CREATE LIST OF EDGES ########
def readToMakeEdges(filename, edge, map):
    filepath = filename
    with open(filepath) as fp:
        line = fp.readline()
        countcomma = 0
        pertama = 0
        kedua = 0
        while line: #selama di suatu baris

            # hapus spasi disekitar koma
            cleanedline = line.replace(' ,', ',') 
            cleanedline2 = cleanedline.replace(', ',',')
            # hapus titik
            cleanedline3 = cleanedline2.replace('.','')
            # menghitung jumlah koma
            countcomma = cleanedline.count(",")
            if(countcomma>0):
                # 1 koma berarti ada 2 matkul
                # 2 koma berarti ada 3 matkul
                # n matkul = n koma + 1

                # buat ambil matkul pertama dan kedua = [0] & [1]
                # buat ambil matkul pertama dan ketiga = [0] & [2]
                for i in range(1,countcomma+1):
                    pertama = getKey(cleanedline3.split(",")[0].strip(),map)
                    kedua = getKey(cleanedline3.split(",")[i].strip(),map)
                    edge.append((pertama,kedua))
            line = fp.readline()


def printResult(graphnya, key, map):
    hasil = pleaseWork(graphnya,key)
    jumlahsemester = len(hasil)

    # jika array tidak kosong
    if len(hasil)!=0:
        for i in range(jumlahsemester):
            print('     Semester {:<4s} : '.format(py_solution().int_to_Roman(i+1)),end="")
            for j in range(len(hasil[i])-1):
                print('{},'.format(map[hasil[i][j]]),end="")
            print('{}'.format(map[hasil[i][len(hasil[i])-1]]))
    else: #array kosong
        print("     Tidak ada, graf yang terbentuk bukan DAG")


# print ascii
def printAC3():
    width = os.get_terminal_size().columns
    s="""                                          
                            .--,-``-.     
   ,---,         ,----..   /   /     '.   
  '  .' \       /   /   \ / ../        ;  
 /  ;    '.    |   :     :\ ``\  .`-    ' 
:  :       \   .   |  ;. / \___\/   \   : 
:  |   /\   \  .   ; /--`       \   :   | 
|  :  ' ;.   : ;   | ;          /  /   /  
|  |  ;/  \   \|   : |          \  \   \  
'  :  | \  \ ,'.   | '___   ___ /   :   | 
|  |  '  '--'  '   ; : .'| /   /\   /   : 
|  :  :        '   | '/  :/ ,,/  ',-    . 
|  | ,'        |   :    / \ ''\        ;  
`--''           \   \ .'   \   \     .'   
                 `---`      `--`-,,-'     
 
"""
    print('\n'.join(l.center(width-1) for l in s.splitlines()))
    print("a n t i   c h a o s".center(width-1))
    print("c h a o s   c l u b".center(width-1))
# ya sebenernya chaos juga sih