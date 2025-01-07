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
