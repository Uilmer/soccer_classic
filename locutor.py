import random

# Função para sortear uma narração
def sorteioLocutor(zona, jogada):

    # Verifica se a jogada foi um sucesso ou fracasso.
    if jogada == "sucesso":

        # Seleciona a frase que vai servir de fala_locutor.
        fala_locutor = random.choice(sucesso[zona])
        # Retorna fala_locutor.
        return fala_locutor
    
    else:

        fala_locutor = random.choice(fracasso[zona])
        return fala_locutor


# Dicionario para as narrações.


sucesso = {
    "Meio_Campo":[
        "Costurou a marcação e ligou o turbo pelo meio.",
        "Faz um passe milimétrico! Rasgou a linha defensiva.",
        "Visão de raio-x! Achou o espaço que ninguém viu e faz o passe.",
        "Tapa de primeira! Deixou o companheiro livre na intermediária.",
        "Dribla dois no círculo central e acelerou o jogo.",
    ],

    "Zaga":[
        "Ganhou no corpo! O atacante deixou o zagueiro para trás.",
        "Que caneta! Passou pelo último homem com extrema facilidade.",
        "Superou o marcador na velocidade pura.",
        "Antecipou o zagueiro e ficou com o campo aberto.",
        "Pedalou na frente do defensor e saiu com classe.",
    ],

    "Gol":[
        "No ângulo! Onde a coruja dorme e o goleiro não chega.",
        "Cavadinha magistral! A bola encobriu o goleiro com classe.",
        "Soltou a bomba! Um chute seco que estufou a rede.",
        "Chute cruzado e rasteiro; a bola beijou a rede.",
        "Limpou o goleiro e só teve o trabalho de empurrar.",
    ]
}

fracasso = {
    "Meio_Campo":[
        "Errou o passe simples e entregou o contra-ataque.",
         "Prendeu demais e foi desarmado no meio de campo.",
         "Tentou o drible e se enrolou com a própria perna.",
         "Dormiu com a bola e perdeu a posse na pressão.",
         "Errou o domínio e a bola escapou como sabonete.",
    ],

    "Zaga":[
        "Bateu no muro! O zagueiro desarmou sem dificuldades.",
        "Adiantou demais e a bola ficou com o defensor.",
        "Travado na hora H! O zagueiro chegou de carrinho.",
        "Perdeu no ombro a ombro e foi ao chão.",
        "Cercado e engolido pela marcação; perdeu a bola.",
    ],

    "Gol":[
         "Isolou! A bola foi parar na arquibancada.",
         "Pegou mascado; o chute saiu fraco e sem direção.",
         "Tirou demais do gol e a bola saiu raspando a trave.",
         "Mandou na lua! Errou o alvo por muito.",
         "Finalização de canela; a bola saiu pela linha de fundo.",
    ]
}