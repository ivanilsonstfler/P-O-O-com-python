class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = "preto"
        self.altura = "10cm"
        self.profundidade = "2cm"
        self.largura = "2cm"

contrlo_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
contrlo_remoto2 = ControleRemoto("preto", "10cm", "2cm", "2cm")


print(contrlo_remoto.cor)