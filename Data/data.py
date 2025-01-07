class Data:
    def __init__(self):
        self.tiket = {
            'REGULER': {'harga': 250000, 'stok': 100},
            'VIP': {'harga': 500000, 'stok': 50},
            'VVIP': {'harga': 1000000, 'stok': 25}
        }
        self.pemesanan = {}