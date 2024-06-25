import pyqrcode
from datetime import datetime

class QrCode():
    '''
    Classe reponsavel por gerar o QR Code, e salvar as imagens
    '''
    def __init__(self,url,name) -> None:
        '''
        Inicializando o Objeto
        '''
        self.url = url
        self.name = name
        self.__background_color = [255,255,255,255]
        self.__module_color = [0,0,0,255]

    def create_image(self):
        '''
        Cria a Imagem
        '''
        self.__qr_code = pyqrcode.create(self.url)
        self.save_png(temp=True)

    def save_svg(self):
        '''
        Salva a imagem no formato .svg
        '''
        self.__qr_code.svg(
            file= f"Images/svg/{self.name}.svg",
            scale=6,
            # module_color=self.__module_color,
            # background= self.__background_color
        )

    def save_png(self, temp=False):
        '''
        Salva a imagem no formato .png
        '''
        file_name = f"temp/img/{self.name}.png" if temp else f"Images/png/{self.name}.png"
        self.__qr_code.png(
            file= file_name,
            scale=6,
            module_color=self.__module_color,
            background= self.__background_color
        )

    def change_color(self, bg_color, m_color):
        '''
        Altera a cor do QR Code
        '''
        self.__background_color = bg_color
        self.__module_color = m_color

    def get_name(self):
        '''
        Retorna o nome criado na imagem
        '''
        return self.name



