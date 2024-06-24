import pyqrcode
from datetime import datetime

class QrCode():
    def __init__(self,url,name) -> None:
        self.url = url
        self.name = name
        self.__background_color = [255,255,255,255]
        self.__module_color = [0,0,0,255]

    def create_image(self):
        self.__qr_code = pyqrcode.create(self.url)
        self.name = str(datetime.now().timestamp())
        self.save_png(temp=True)

    def save_svg(self):
        self.__qr_code.svg(
            file= f"Images/svg/{self.name}.svg",
            scale=6,
            # module_color=self.__module_color,
            # background= self.__background_color
        )

    def save_png(self, temp=False):
        file_name = f"temp/img/{self.name}.png" if temp else f"Images/png/{self.name}.png"
        self.__qr_code.png(
            file= file_name,
            scale=6,
            module_color=self.__module_color,
            background= self.__background_color
        )

    def change_color(self, bg_color, m_color):
        self.__background_color = bg_color
        self.__module_color = m_color



