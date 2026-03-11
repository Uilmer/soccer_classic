import random
# itertools para criar a combinação onde cada time se enfrenta.
import itertools



# Class que vai servir de modelo para os times.
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
    def pontosDisputa(self):

        # Valor do ponto ofensivo pode ser dentre 1 até 5. 
        self.ponto_ofensivo = random.randint(1, 5)

        # valor do ponto defensivo pode ser dentre 1 até 5.
        self.ponto_defensivo = random.randint(1, 5)

# Classe para gerenciar o campeonato e guardar a lista de times.
class Campeonato():

    def __init__(self,):
    
        self.nome_campeonato = "Copa Das Nações"
        self.rodada = 0
        # Lista de partidas.
        self.disputas = []
        # Lista para armazenar os times que vão jogar nessa rodada.
        self.rodada_atual = []
        # Lista para armazenar os times que vão jogar na proxima rodada.
        self.proxima_rodada = []

        self.times = [
            Time("Brasil"), Time("Argentina"), Time("Espanha"),
            Time("França"), Time("Uruguai"), Time("Inglaterra"),
            Time("Italia"), Time("Alemanha"),
        ]
        
    # Método para criar as combinações onde cada time se enfrenta.
    def jogosCampeonato(self):

        # Cria um nova lista combinando os valores da lista self.times.
        lista_jogos = list(itertools.combinations(self.times, 2))

        # Define o atributo disputas da class para armazenar todos os jogos da competição.
        self.disputas = lista_jogos

    # Método para iniciar rodadas e gerenciar as disputas.
    def iniciarRodada(self,):

        # Separa os jogos em rodada_atual e proxima_rodada.
        for jogo_atual in self.disputas:

            # Criação do time_a e time_b baseado em jogo_atual[0] e jogo_atual[1].
            time_a, time_b = jogo_atual

            # Verifica se o time_a e time_b não estão na lista da rodada atual.
            if time_a not in self.rodada_atual and time_b not in self.rodada_atual:
                
                # Adiciona o time_a e time_b na lista da rodada_atual.
                self.rodada_atual.append(time_a)
                self.rodada_atual.append(time_b)
                
                # Chama o método que vai iniciar de fato a partida.
                self.iniciarPartida(time_a, time_b)
            
            else:

                # Adiciona a disputa atual na lista proxima_rodada.
                self.proxima_rodada.append(jogo_atual)
        
        # Limpa a lista rodada atual.
        self.rodada_atual = []
        
        # Atualiza a lista de disputas com os times que entraram na lista de proxima rodada.
        self.disputas = self.proxima_rodada

        # Limpa a lista proxima rodada.
        self.proxima_rodada = []
        
    # Método para trocar a posse de bola.
    def trocaPosseDeBola(self, posse_de_bola):

        # Verificando qual time tem a  posse de bola atual.
    
        if posse_de_bola == "time_a":

            # Se for o time_a ele passa a posse de bola para o time_b
            return "time_b"
        
        elif posse_de_bola == "time_b":

            # Se for o time_b ele passa a posse de bola para o time_a
            return "time_a"

    # Método para iniciar o jogo atual, recebe como parametros time_a e time_b.
    def iniciarPartida(self, time_a, time_b):

        # Exibi qual é o jogo atual.
        print(f"{time_a.nome} X {time_b.nome}")

        #--- PREPARAÇÕES DA PARTIDA ---#

        # Variavel para armazenar qual time está com a bola.
        posse_da_bola = "time_a"

        # O time atacante é o time que tem a posse da bola.
        time_atacante, time_defensor = time_a, time_b

        # Lista para armazenar o fluxo de disputa.
        zonas_disputas = ["Meio_Campo", "Zaga", "Gol"]

        #--- iNICIANDO A PARTIDA ---#

        # Laço e repetição para representar o tempo de jogo.
        for i in range(10):

            #--- Verificação para definir qual time está no ataque e qual time está defendendo. ---#

            if  posse_da_bola == "time_a":
                # time_a como atacante e time_b como defensor.
                time_atacante, time_defensor = time_a, time_b

            elif posse_da_bola == "time_b":
                # time_b como atacante e time_a como defensor.
                time_atacante, time_defensor = time_b, time_a
            
            #--- iNICIANDO AS DISPUTAS DE BOLA  ---# 
            
            # Laço para realizar todas as disputas.
            for disputa in zonas_disputas:

                # Chamando os métodos de cada time para gerar um valor aleatorio para as disputas.
                time_atacante.pontosDisputa()
                time_defensor.pontosDisputa()

                # Se o ponto ofensivo do atacante for maior que o ponto defensivo do defensor.
                # Aqui eu coloco 
                if time_atacante.ponto_ofensivo > time_defensor.ponto_defensivo and disputa != "Gol":

                    print(f"{time_atacante.nome} vence a disputa de {disputa}")
                
                elif time_defensor.ponto_defensivo >= time_atacante.ponto_ofensivo:

                    print(f"{time_atacante.nome} falha na disputa de {disputa}")
                    
                    posse_da_bola = self.trocaPosseDeBola(posse_da_bola)
                    break
                
                elif time_atacante.ponto_ofensivo > time_defensor.ponto_defensivo and disputa == "Gol":

                    print(f"GOOOOOOOOL! {time_atacante.nome} marca ")
                    
                    posse_da_bola = self.trocaPosseDeBola(posse_da_bola)
                    break
            




#----- PROGRAMA PRINCIPAL -----------#

# Cria a variavel copa que é um objeto da class Campeonato. 
obj_copa = Campeonato()

# Chama o método jogosCampeonato do objeto copa.
obj_copa.jogosCampeonato()
# Chama o método iniciarRodada do objeto copa.
obj_copa.iniciarRodada()