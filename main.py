import sys
from QrCode.QrCode import QrCode
from OsTratative.OsTratative import OsTratative
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton
from PyQt5.QtGui import QCloseEvent, QPixmap
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.url = None
        self.os_operation = OsTratative()
        
    def initUI(self):
        # Configurações da janela
        self.setWindowTitle('Tela com Campos de Texto e Imagem')
        self.setGeometry(100, 100, 800, 700)
        self.center()
        
        # Layout principal
        vbox = QVBoxLayout()
        
        # Campo de texto para URL
        hbox_url = QHBoxLayout()
        lbl_url = QLabel('URL:', self)
        self.txt_url = QLineEdit(self)
        hbox_url.addWidget(lbl_url)
        hbox_url.addWidget(self.txt_url)
        
        # Campo de texto para Nome
        hbox_nome = QHBoxLayout()
        lbl_nome = QLabel('Nome:', self)
        self.txt_nome = QLineEdit(self)
        hbox_nome.addWidget(lbl_nome)
        hbox_nome.addWidget(self.txt_nome)
        
        # Campo de imagem
        self.lbl_imagem = QLabel(self)
        self.lbl_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Botão para carregar a imagem
        btn_load_image = QPushButton('Criar Qr Code', self)
        btn_load_image.clicked.connect(self.loadImage)

        # Botões para salvar os QrCodes
        hbox_choices = QHBoxLayout()
        btn_save_png = QPushButton('Salvar .png', self)
        btn_save_png.clicked.connect(self.url.save_png())
        btn_save_svg = QPushButton('Salvar .svg', self)
        btn_save_svg.clicked.connect(self.url.save_svg())
        hbox_choices.addWidget(btn_save_png)
        hbox_choices.addWidget(btn_save_svg)
        
        # Adiciona os layouts ao layout principal
        vbox.addLayout(hbox_url)
        vbox.addLayout(hbox_nome)
        vbox.addWidget(self.lbl_imagem)
        vbox.addWidget(btn_load_image)
        
        self.setLayout(vbox)
        
    def center(self):
        # Centraliza a janela na tela
        qr = self.frameGeometry()
        cp = QApplication.desktop().screen().rect().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def loadImage(self):
        # Carrega uma imagem .png (caminho da imagem)
        self.url = QrCode(self.txt_url.text(),self.txt_nome.text())
        self.url.create_image()
        pixmap = QPixmap(f'temp/img/{self.url.get_name()}.png')
        self.lbl_imagem.setPixmap(pixmap.scaled(self.lbl_imagem.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))
        
    def closeEvent(self, event):
        # Função para executar antes de fechar a aplicação
        self.os_operation.clear_dir()
        event.accept()  # Aceita o evento de fechamento

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

