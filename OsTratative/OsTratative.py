import os

class OsTratative():
    def __init__(self) -> None:
        self.dir = os.getcwd()
        self.__full_dir = f"{self.dir}/temp/img"
        print(self.dir)

    def clear_dir(self):
        for filename in os.listdir(self.__full_dir):
            os.unlink(f"{self.__full_dir}/{filename}")
    
