import random



# Classe que vai servir de modelo para os times.
class Time():
    # Atributos do time.
    def __init__(self, nome):
        
        self.nome = nome
        self.ponto_ofensivo = 0
        self.ponto_defensivo = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.pontos = 0
        self.saldo_gols = 0

    
    # Método para randomizar os valores de atributo ofensivo e defensivo de cada time.
    def pontosDisoputa(self):

        # Valor do ponto ofensivo pode ser dentre 1 até 5. 
        self.ponto_ofensivo = random.randint(1, 5)

        # valor do ponto defensivo pode ser dentre 1 até 5.
        self.ponto_defensivo = random.randint(1, 5)