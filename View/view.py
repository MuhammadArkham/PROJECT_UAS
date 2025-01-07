class View:
    def tampilkan_menu(self):
        print("\n=== TIKET INDONESIA VS BAHRAIN ===")
        print("1. Lihat Tiket")
        print("2. Beli Tiket")
        print("3. Cek Pemesanan")
        print("4. Keluar")
    
    def tampilkan_tiket(self, tiket):
        print("\n=== DAFTAR TIKET ===")
        print("Kategori  |    Harga    | Stok")
        print("-" * 40)
        for kategori, info in tiket.items():
            print(f"{kategori:<9} | Rp {info['harga']:>9,} | {info['stok']:>4}")
    
    def tampilkan_etiket(self, id_pesan, detail):
        print("\n=== E-TIKET ===")
        print(f"ID Pemesanan : {id_pesan}")
        print(f"Jenis Tiket  : {detail['jenis']}")
        print(f"Jumlah Tiket : {detail['jumlah']}")
        print(f"Total Bayar  : Rp {detail['total']:,}")