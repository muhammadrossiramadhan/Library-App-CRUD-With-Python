# Program Perpustakaan Sederhana 

# Kumpulan perintah input data peminjaman buku.
def kumpulan_input():

    # Masukkan judul buku yang ingin dipinjam.
    Judul_buku = input("Masukkan judul buku : ")

    # Masukkan nama peminjam buku.
    Nama_Peminjam = input("Masukkan nama peminjam ( Sesuai KTM ) : ")

    # Masukkan Jumlah Hari dengnan validasi yang benar dan sesuai kriteria dengan mengguunakan fungsi validasi_jumlah_hari().
    Jumlah_hari = masukkan_jumlah_hari()

    # Masukkan Jumlah tetap biaya peminjaman per hari jika suatu hari perngguna terkena denda akibat telat tidak mengembalikan buku. 
    biaya_peminjaman_hari = 2000

    # Perhitungan total buku
    Denda_total = Jumlah_hari * biaya_peminjaman_hari

    # Mengembalikan parameter Judul_buku, Nama_ Peminjam, Jumlah_hari, Biaya_Peminjaman_hari, Denda_total 
    return Judul_buku, Nama_Peminjam, Jumlah_hari, biaya_peminjaman_hari, Denda_total

# Kumpulan perintah input data peminjaman buku tambahan.
def kumpulan_input_tambahan():

    # Masukkan judul buku yang ingin dipinjam.
    Judul_buku = input("Masukkan judul buku : ")
    
    # Masukkan Jumlah Hari dengnan validasi yang benar dan sesuai kriteria dengan mengguunakan fungsi validasi_jumlah_hari().
    Jumlah_hari = masukkan_jumlah_hari()

    # Masukkan Jumlah tetap biaya peminjaman per hari jika suatu hari perngguna terkena denda akibat telat tidak mengembalikan buku.
    biaya_peminjaman_hari = 2000

    # Perhitungan total buku
    Denda_total = Jumlah_hari * biaya_peminjaman_hari

    # Mengembalikan parameter Judul_buku, Nama_ Peminjam, Jumlah_hari, Biaya_Peminjaman_hari, Denda_total 
    return Judul_buku, Jumlah_hari, biaya_peminjaman_hari, Denda_total

''' fungsi khusus yang digunakan ketika kondisi input pengguna memiliki jumlah hari peminjaman yang lebih dari 30 hari 
atau terdapat kesalahan input data pada 'Jumlah hari peminjam seperti angka negatif' 
guna memastikan input data jumlah hari peminjaman ini valid.'''
def masukkan_jumlah_hari():
        while True:
            #mnenginisialisasi variable Jumlah_hari
            Jumlah_hari = 0
            #input tidak boleh kosong
            if Jumlah_hari == "":
                print("Input tidak boleh kosong. Silakan masukkan angka yang benar.")
                continue
            # Untuk menangani input yang bukan integer (misal: huruf, simbol), kami memakai try dan except.
            try:
                # Masukkan jumlah hari peminjaman yang benar.
                Jumlah_hari = int(input("Masukkan jumlah hari peminjaman (maksimal 30 hari): "))
                # kondisi jika terdapat angka negatif atau lebih dari 30 hari pada 'Jumlah hari peminjam'.
                if Jumlah_hari < 0 and Jumlah_hari >= 30:
                    print("Peringatan anda tidak boleh memakai angka negatif pada jumlah hari peminjaman.")
                    print("Peringatan anda tidak boleh memakai angka negatif pada jumlah hari peminjaman.")
                    print("Silakan hubungi perpustakaan untuk informasi lebih lanjut.")
                    continue
                # kondisi sebaliknya jika mereka berhasil memasukkan data input yang benar.
                else:
                    print("Jumlah hari peminjaman yang benar telah dimasukkan.")
                # Mengembalikan parameter Judul_buku, Nama_ Peminjam, Jumlah_hari, Biaya_Peminjaman_hari, Denda_total 
                return Jumlah_hari

            # jika pengguna memasukkan nilai yang bukan angka seperti huruf atau simbol.
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka yang benar.")

# Memastikan jika input pengguna itu sesuai syarat dan kriteria tertentu pada sistem manajemen perpustakaan sederhana kami
Status_valid = True

""" Tampilan program perpustakaan sederhana dengan perulangan (while) agar program terus berjalan ketika memenuhi pensyaratan,
dan memberikan kesempatan pengguna dalam menggunakan program perpustakaan sederhana dengan lebih baik saat terjadi kesalahan. """
while Status_valid == True:

    print("===================================")
    print("\n----- Perpustakaan Sederhana -----\n")
    print("===================================")

    print("\nSelamat datang di perpustakaan kami 😊\n")

    
    # Pengguna diminta untuk memasukkan beberapa input data terkait peminjaman buku pada program perpustakaan sederhana.
    Input_Pengguna = kumpulan_input()
    # Pengguna diminta memasukkan judul buku yang mereka pinjam.
    Judul_buku = Input_Pengguna[0]
    # Pengguna diminta untuk memasukkan nama mereka.
    Nama_Peminjam = Input_Pengguna[1]
    # Pengguna diminta untuk memasukkan jumlah hari yang ditentukan
    Jumlah_hari = Input_Pengguna[2]
    # Dua variable berikut digunakan untuk perhitungan total buku jika pengguna melanggar
    biaya_peminjaman_hari = Input_Pengguna[3]
    Denda_total = Input_Pengguna[4]


    # Konfirmasi terkait peminjaman buku yang telah pengguna input guna mereka tahu untuk buku apa yang mereka pinjam. 
    print("\n=================================")
    print("\n----- Konfirmasi data buku -----\n")
    print("===================================\n")
    print("Buku yang dipinjam               :", Judul_buku.ljust(30))
    print("Nama peminjam                    :", Nama_Peminjam.ljust(30))
    print("Jumlah hari peminjaman           :", str(Jumlah_hari).ljust(30))
    print("Denda total yang harus dibayar   :", str(Denda_total).ljust(30))

    # Pengguna diminta untuk menambahkan buku lain atau tidak.
    Tambah_Buku = input("\nApakah anda ingin menambahkan buku lain ? jawablah dengan (ya/tidak): ")

    """ Kondisi jika pengguna ingin menambahkan buku lain mereka dan mentotalkan biaya denda yang harus dibayar jika
    pengguna tidak mengembalikannya dengan tepat waktu. """
    if Tambah_Buku.lower() == "ya" or Tambah_Buku.upper() == "YA":

        # Pengguna diminta untuk memasukkan beberapa input data kembali terkait peminjaman buku tambahan.
        Input_Pengguna_baru = kumpulan_input_tambahan()
        # Pengguna diminta untuk memasukkan judul buku tambahan mereka.
        Judul_buku_baru = Input_Pengguna_baru[0]
        # Pengguna diminta untuk memasukkan jumlah hari yang ditentukan.
        Jumlah_hari_baru = Input_Pengguna_baru[1]  
        # Perhitungan denda total baru
        Denda_total_baru = Input_Pengguna[4] # Input_Pengguna[4] adalah 'biaya_peminjaman_hari'
        Denda_total += Denda_total_baru
                
        # Konfirmasi data buku tambahan mereka
        print("\n=================================")
        print("\n----- Konfirmasi data buku -----\n")
        print("===================================\n")
        print("Buku yang dipinjam               :", Judul_buku, ",", Judul_buku_baru.ljust(30))     # ljust(30) digunakan guna 
        print("Nama peminjam                    :", Nama_Peminjam.ljust(30))                        # memberikan kerapian pada peletakan 
        print("Jumlah hari peminjaman           :", str(Jumlah_hari + Jumlah_hari_baru).ljust(30))  # tulisan.
        print("Denda total yang harus dibayar   :", str(Denda_total).ljust(30))

        print("\nTerima kasih telah menggunakan layanan perpustakaan kami.")
        # break ini digunakan untuk memberhentikan program Perpustakaan Sederhana.
        break

    # Kembali ke menu utama jika pengunna telah menginput data buku mereka pada program perpustakaan sederhana ini.
    Beranda = input("\nAnda ingin kembali ke menu utama ? jawablah dengan (ya/tidak): ")
    # Kondisi jika ingin kembali ke menu utama
    if Beranda.lower() == "ya" or Beranda.upper() == "YA":
        # Pengguna dapat kembali ke halaman utama program perpustakaan sederhana.
        continue
    # Kondisi pengguna jika tidak ingin menambahkan buku lain
    elif Tambah_Buku.lower() == "tidak" or Tambah_Buku.upper() == "TIDAK":
        print("\nTerima kasih telah menggunakan layanan perpustakaan kami.")
    else:
        # break ini digunakan untuk memberhentikan program Perpustakaan Sederhana.
        break
