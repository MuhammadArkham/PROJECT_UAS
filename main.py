from Data.data import Data
from View.view import View
from Process.process import Process
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
            print("\nError: Pilihan tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()