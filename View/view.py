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