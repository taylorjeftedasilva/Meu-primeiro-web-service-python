class cliente:
    def __init__(self, nome):
        self.nome=nome
        self.__idade=10
    @property
    def retorno(self):
        lista=[self.nome,self.__idade]
        return lista
