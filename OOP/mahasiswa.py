# Membuat class
class Mahasiswa:
# menambahkan atribut

    # MEthode
    def __init__(self,nama,nim,rombel):
        self.nama = nama
        self.nim = nim
        self.rombel = rombel

    def lulus(self, nilai):
        if (nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")
    #  Class mahasiswa memiliki 3 atribut dan 1 fungsi

    def cetak(self):
        print('Nama \t:', self.nama)
        print('NIM \t:',self.nim)
        print('Rombel \t:', self.rombel)

m1 = Mahasiswa("ilman Nurkhoiron",'0110222202','TI-05')


m1.cetak()
m1.lulus(95)

# Objek ke 2
m2 = Mahasiswa('jason ranti','0110222022',"TI-05")

print('')
m2.cetak()
m2.lulus(85)