# PROJECT_UAS
Nama : Muhammad Arkhamullah Rifai Asshidiq

Mata kuliah :Bahasa pemrograman

NIM : 312410545




## **Penjelasan Program**:


### **1. class `data.py`**  
**Fungsi:** Menyimpan data tiket dan pemesanan.  

```python
class Data:
    def __init__(self):
        self.tiket = {
            'REGULER': {'harga': 250000, 'stok': 100},
            'VIP': {'harga': 500000, 'stok': 50},
            'VVIP': {'harga': 1000000, 'stok': 25}
        }
        self.pemesanan = {}
```

**Penjelasan:**  
- `tiket`: Menyimpan data harga dan stok tiket untuk tiga kategori (REGULER, VIP, VVIP).  
- `pemesanan`: Dictionary kosong yang akan diisi dengan data pemesanan tiket.  

---

### **2.  class `view.py`**  
**Fungsi:** Menampilkan menu, daftar tiket, dan e-tiket kepada pengguna.  

```python
class View:
    def tampilkan_menu(self):
        print("""
=== TIKET INDONESIA VS BAHRAIN ===
1. Lihat Tiket
2. Beli Tiket
3. Cek Pemesanan
4. Keluar""")
    
    def tampilkan_tiket(self, tiket):
        print("\n=== DAFTAR TIKET ===")
        print("Kategori  |    Harga    | Stok")
        print("-" * 35)
        for kategori, info in tiket.items():
            print(f"{kategori:<9} | Rp {info['harga']:,} | {info['stok']}")
    
    def tampilkan_etiket(self, id_pesan, detail):
        print(f"""
=== E-TIKET ===
ID Pemesanan : {id_pesan}
Jenis Tiket  : {detail['jenis']}
Jumlah Tiket : {detail['jumlah']}
Total Bayar  : Rp {detail['total']:,}""")
```

**Penjelasan:**  
- `tampilkan_menu()`: Menampilkan menu utama kepada pengguna.  
- `tampilkan_tiket()`: Menampilkan daftar tiket yang tersedia dengan harga dan stok.  
- `tampilkan_etiket()`: Menampilkan detail pemesanan berupa e-tiket setelah pemesanan berhasil dilakukan.  

---

### **3.  class `process.py`**  
**Fungsi:** Melakukan validasi input, proses pemesanan tiket, dan pengecekan status pemesanan.  

```python
class Process:
    def __init__(self, data, view):
        self.data = data
        self.view = view
    
    def validasi_input(self, prompt, jenis="angka"):
        while True:
            try:
                nilai = input(prompt)
                if jenis == "angka":
                    nilai = int(nilai)
                    if nilai <= 0:
                        print("Error: Nilai harus lebih dari 0!")
                        continue
                elif jenis == "jenis_tiket":
                    nilai = nilai.upper()
                    if nilai not in self.data.tiket:
                        print(f"Error: Pilih {'/'.join(self.data.tiket.keys())}!")
                        continue
                return nilai
            except ValueError:
                print("Error: Input tidak valid!")
    
    def pesan_tiket(self):
        jenis = self.validasi_input("Masukkan jenis tiket: ", "jenis_tiket")
        jumlah = self.validasi_input("Masukkan jumlah tiket: ", "angka")
        
        if jumlah > self.data.tiket[jenis]['stok']:
            print(f"Error: Stok tidak cukup! (Tersedia: {self.data.tiket[jenis]['stok']})")
            return
            
        total = self.data.tiket[jenis]['harga'] * jumlah
        print(f"\nTotal Bayar: Rp {total:,}")
        
        if input("Lanjutkan pemesanan (y/t)? ").lower() == 'y':
            id_pesan = f"P{len(self.data.pemesanan) + 1:03d}"
            self.data.pemesanan[id_pesan] = {
                'jenis': jenis,
                'jumlah': jumlah,
                'total': total
            }
            self.data.tiket[jenis]['stok'] -= jumlah
            self.view.tampilkan_etiket(id_pesan, self.data.pemesanan[id_pesan])
        else:
            print("Pemesanan dibatalkan.")
    
    def cek_pemesanan(self):
        id_pesan = input("Masukkan ID pemesanan: ").strip().upper()
        if id_pesan in self.data.pemesanan:
            self.view.tampilkan_etiket(id_pesan, self.data.pemesanan[id_pesan])
        else:
            print("Error: Pemesanan tidak ditemukan!")
```

**Penjelasan:**  
- `validasi_input()`: Memvalidasi input pengguna. Mendukung validasi angka dan jenis tiket.  
- `pesan_tiket()`: Memproses pemesanan tiket, menghitung total harga, dan menampilkan e-tiket jika pengguna mengonfirmasi pembelian.  
- `cek_pemesanan()`: Memeriksa status pemesanan berdasarkan ID pemesanan yang dimasukkan pengguna.  

---

### **4. `main.py`**  
**Fungsi:** Mengatur jalannya program dan navigasi antar menu.  

```python
from data import Data
from view import View
from process import Process

def main():
    data = Data()
    view = View()
    process = Process(data, view)

    while True:
        view.tampilkan_menu()
        pilihan = input("\nPilih menu (1-4): ")

        if pilihan == '1':
            view.tampilkan_tiket(data.tiket)
        elif pilihan == '2':
            process.pesan_tiket()
        elif pilihan == '3':
            process.cek_pemesanan()
        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan layanan kami!")
            break
        else:
            print("Error: Pilihan tidak valid!")
            
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
```

**Penjelasan:**  
- **`main()`**:  
  - Menginisialisasi objek dari kelas `Data`, `View`, dan `Process`.  
  - Menjalankan loop yang menampilkan menu dan memproses input pengguna hingga pengguna memilih keluar (`4`).  
  - Opsi 1: Menampilkan tiket.  
  - Opsi 2: Proses pembelian tiket.  
  - Opsi 3: Cek status pemesanan.  

---

### **Cara Kerja Program:**  
1. Pengguna menjalankan program dan disajikan menu utama.  
2. Jika memilih "1", daftar tiket akan ditampilkan.  
3. Jika memilih "2", pengguna bisa memesan tiket dengan memilih kategori dan jumlah tiket yang diinginkan.  
4. Setelah berhasil memesan, pengguna mendapatkan e-tiket dengan ID pemesanan.  
5. Opsi "3" memungkinkan pengguna untuk memeriksa pemesanan berdasarkan ID.  
6. Program berakhir saat pengguna memilih "4".  

Program ini modular, sehingga mudah diperluas untuk menambah fitur seperti pembayaran atau kategori tiket tambahan.



