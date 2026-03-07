



# Classe que vai servir de modelo para os times
class Time():
    # Atributos do time
    def __init__(self, nome):
        
        self.nome = nome
        self.ponto_ofensivo = 0
        self.ponto_defensivo = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.pontos = 0
        self.saldo_gols = 0