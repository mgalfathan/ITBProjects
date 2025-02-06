#~~~AUTO GATE TOL~~~#
''' 
Deskripsi : Sistem tol yang digunakan adalah sistem tol tertutup. Pengguna tidak perlu membayar ketika
tap e-Toll di gerbang masuk. Pengguna membayar tol di gerbang keluar, dengan tarif yang dihitung per kilometer 
dan golongan kendaraan yang dimiliki. 

Algoritma ini dibuat semirip mungkin dengan gerbang tol yang sebenarnya, yang bisa dilalui oleh banyak kendaraan.
Sehingga algoritma ini bisa menginput sebanyak mungkin data kendaraan yang masuk, dan menyimpan data tersebut 
agar kendaraan bisa keluar di gerbang keluar
'''

#~~~~~~~KAMUS~~~~~~~#
'''
*~~~Variabel Simpan~~~*
data_id_eToll : array Integer -> menyimpan data id eToll yang telah digunakan untuk tap masuk
save_masuk : array string -> menyimpan data gerbang masuk dari kendaraan, indeks disesuaikan dengan data_id_eToll
data_gerbang : array string -> ada gerbang 'A', 'B', 'C', 'D', 'E'
km_gerbang : array integer -> letak kilometer dari setiap gerbang, indeks disesuaikan dengan data_gerbang
tarif_golongan : array float -> perbandingan harga tiap golongan, dengan golongan 1 menjadi acuan
tarif_per_km : integer -> harga per kilometer

*~~Variabel Sementara~~*
(variabel yang nilainya terus berganti ketika ada input baru)
id_eToll : integer, 5 digit
km_masuk : integer
km_keluar : integer
golongan : string
gerbang_masuk : string
gerbang_keluar : string
saldo : integer
total_harga : integer
count : integer -> menghitung indeks array data_id_eToll, karena array tersebut dapat bertambah indeksnya
status : string -> input : "masuk" atau "keluar"
tanya : string -> input : "lanjut" atau "tidak"
lanjut : boolean -> menentukan kapan program akan berhenti

*~~Variabel Bantu~~*
cek : boolean -> mengecek array yang kosong
i : integer -> untuk while loop
'''

#~~~~~DATABASE~~~~~#
'''membuat data yang akan dijadikan acuan untuk perhitungan'''

data_gerbang = [ '0' for i in range (5) ]
km_gerbang = [ '0' for i in range (5) ]
tarif_golongan = [ 0 for i in range (6) ]

data_gerbang[0] = 'A'
data_gerbang[1] = 'B'
data_gerbang[2] = 'C'
data_gerbang[3] = 'D'
data_gerbang[4] = 'E'

km_gerbang[0] = 0
km_gerbang[1] = 70
km_gerbang[2] = 150
km_gerbang[3] = 200
km_gerbang[4] = 300

tarif_golongan[1] = 1
tarif_golongan[2] = 1.2
tarif_golongan[3] = 1.5
tarif_golongan[4] = 1.7
tarif_golongan[5] = 2

tarif_per_km = 700

#~~~~INITIALIZE~~~~#
'''inisialisasi variabel yang akan digunakan'''

data_id_eToll = [0]
save_masuk = ['0']
saldo = 0
golongan = 0
total_harga = 0
count = 0
lanjut = True

#~~~~~ALGORITHM~~~~~#
while (lanjut == True):
    status = input("Mau masuk/keluar tol? ")

    if(status == 'masuk'):
        #~~~Gerbang Masuk~~~#
        '''pengendara akan tap kartu eToll, mesin akan menyimpan data id eToll tersebut, 
        dan di gerbang mana kartu tersebut ditap'''
        id_eToll = int(input("Masukkan 5 digit ID e-Toll : "))
        gerbang_masuk = input("Dari gerbang mana? : ")
        cek = False
        i = 0

        while (i<=count and cek == False): 
            if(data_id_eToll[i]== 0): #mengecek indeks yang kosong untuk menyimpan data baru
                data_id_eToll[i] = id_eToll
                save_masuk[i] = gerbang_masuk
                cek = True
            i += 1
        if(cek == False): #jika semua indeks terisi, maka indeks bertambah 1, data disimpan di indeks paling akhir
            data_id_eToll.append(id_eToll)
            save_masuk.append(gerbang_masuk)
            count += 1 #count bertambah untuk menyimpan jumlah indeks yang baru
            
        tanya = str(input("Mau lanjut/tidak? "))
        if(tanya == "tidak"):
            lanjut = False
            
    elif(status == 'keluar'):
        #~~~Gerbang Keluar~~~#
        id_eToll = int(input("Masukkan 5 digit ID e-Toll : "))
        i = 0
        cek = False
        while (i<=count and cek == False):
            # cek data id eToll, apakah kartu tersebut digunakan untuk tap masuk?
            if(data_id_eToll[i] == id_eToll):
                saldo = int(input("Masukkan nominal saldo anda : "))
                gerbang_keluar = input("Keluar di gerbang mana? : ")
                golongan = int(input("Masukkan golongan kendaraan : "))
                for j in range(5):
                    if(data_gerbang[j] == save_masuk[i]):
                        km_masuk = km_gerbang[j]
                        break
                for j in range(5):
                    if(data_gerbang[j] == gerbang_keluar):
                        km_keluar = km_gerbang[j]
                        break
                cek = True
            i += 1    
            if(i>count and cek == False): #kartu yang bisa digunakan hanyalah kartu yang telah digunakan untuk tap masuk
                print("Kartu tidak bisa digunakan")
                id_eToll = int(input("Masukkan 5 digit ID e-Toll : "))            
                i = 0 #pengendara harus menggunakan kartu lain, i kembali menjadi 0, loop untuk cek id eToll akan diulang kembali
        total_harga = int(tarif_per_km * abs(km_keluar-km_masuk) * tarif_golongan[golongan])
        # untuk menghitung harga yang harus dibayar digunakan absolut karena diasumsikan di setiap tempat ada gerbang masuk dan keluar

        if(saldo < total_harga):
            while(saldo < total_harga): 
                #jika saldo tidak mencukupi, pengendara harus top up saldo terlebih dahulu, sehingga akan diinput saldo baru
                print("Saldo tidak mencukupi")
                print("Harga yang harus dibayar adalah: Rp" + str(total_harga))
                saldo = int(input("Masukkan nominal saldo baru: "))
        if(saldo >= total_harga):
            print("Silakan melanjutkan perjalanan :D")
            print("Sisa saldo anda Rp" + str(saldo - total_harga))
            
            # hapus data id dan gerbang yang tersimpan
            data_id_eToll[i-1] = 0
            save_masuk[i-1] = '0'
        
        tanya = str(input("Mau lanjut/tidak? "))
        if(tanya == "tidak"):
            lanjut = False
