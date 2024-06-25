import os

class OsTratative():
    '''
    Classe responsavel por fazer as operações cabiveis ao so
    '''
    def __init__(self) -> None:
        '''
        inicializador do objeto
        '''
        self.dir = os.getcwd()
        self.__full_dir = f"{self.dir}/temp/img"
        print(self.dir)

    def clear_dir(self):
        '''
        limpa o repositorio temp/img
        '''
        for filename in os.listdir(self.__full_dir):
            os.unlink(f"{self.__full_dir}/{filename}")
    
