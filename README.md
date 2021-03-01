# anti chaos chaos club
Sebuah program untuk menyusun rencana kuliah dengan *topological sort* untuk memenuhi tugas kecil 2 IF2211 Strategi Algoritma. Program diimplementasikan dengan menganggap setiap matkul menjadi simpul dari sebuah graf. Program kemudian akan mencari simpul yang tidak memiliki derajat masuk dan menghapus simpul tersebut dari graf. Semua derajat masuk dari simpul lain yang memiliki sisi berarah dari simpul yang dihapus sebelumnya dikurangi dengan 1. Hal tersebut dilakukan secara terus menerus sampai semua simpul dari graf diproses.

## requirement & installation
- [Python 3.5+](https://www.python.org/) and [Pip](https://pypi.org/project/pip/)
- [Os](https://pypi.org/project/os-win/)
  ``` pip install os ```
    
## running
- Open command prompt
- Go to src folder and run the command below
```bash
$ python main_13519011.py
```
## author
13519011 Jesica K01
