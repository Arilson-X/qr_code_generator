from QrCode.QrCode import QrCode
from OsTratative.OsTratative import OsTratative

url = QrCode("https://www.linkedin.com/in/arilson-xavier-0a581a145/","Teste")
url.create_image()
url.save_png()
url.save_svg()
OsTratative()