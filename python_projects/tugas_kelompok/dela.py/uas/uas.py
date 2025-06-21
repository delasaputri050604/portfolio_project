from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QLineEdit, QMessageBox, QPixmap
from PySide6.QtGui import QFont, QPixmap

produk = {
    "Powder": [45000, "powder.png"],
    "Cushion": [53000, "cushion.png"],
    "Lipstik": [23000, "lipstik.png"]
}

class KasirUnik(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kasir Unik Dela")
        self.setFixedSize(400, 450)

        self.layout = QVBoxLayout()

        self.label_judul = QLabel("🛍️ Kasir Cantik by Dela")
        self.label_judul.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.label_judul)

        self.combo_produk = QComboBox()
        self.combo_produk.addItems(produk.keys())
        self.combo_produk.currentTextChanged.connect(self.tampilkan_gambar)
        self.layout.addWidget(self.combo_produk)

        self.gambar = QLabel()
        self.layout.addWidget(self.gambar)
        self.tampilkan_gambar(self.combo_produk.currentText())

        self.input_jumlah = QLineEdit()
        self.input_jumlah.setPlaceholderText("Masukkan jumlah")
        self.layout.addWidget(self.input_jumlah)

        self.btn_hitung = QPushButton("Hitung Total 🧮")
        self.btn_hitung.clicked.connect(self.hitung_total)
        self.layout.addWidget(self.btn_hitung)

        self.label_total = QLabel("Total: Rp 0")
        self.label_total.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.label_total)

        self.setLayout(self.layout)

    def tampilkan_gambar(self, nama_produk):
        gambar_path = produk[nama_produk][1]
        pixmap = QPixmap(gambar_path)
        self.gambar.setPixmap(pixmap.scaledToWidth(200))

    def hitung_total(self):
        try:
            nama = self.combo_produk.currentText()
            jumlah = int(self.input_jumlah.text())
            harga = produk[nama][0]
            total = harga * jumlah
            self.label_total.setText(f"Total: Rp {total}")
        except:
            QMessageBox.warning(self, "Oops!", "Masukkan jumlah yang valid ya!")

app = QApplication([])
window = KasirUnik()
window.show()
app.exec()
