#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import especial
from ..narracao import narrador
from ..base import Opcao, Escolhas

from . import floresta_part2 as part2

def inicio():

    narrador(\
    """
    Após olhar o mapa, você segue o caminho mais apropriado para chegar na cidade.
    """,
    """
    Não tão longe do seu ponto de partida, você encontra algumas frutinhas, nos arbustos ao lado da trilha. Sua barriga está roncando.
    """,
    identacao =2)

    op1 = Opcao("Comer as frutinhas", lambda: frutinhas)
    op2 = Opcao("Ignorar e continuar andando", lambda: acampamento)
    return Escolhas(op1, op2, introducao="você:")

def frutinhas():

    narrador(\
    """
    Você decide comer várias frutinhas para matar a fome,
    porém não esperava que a única coisa que a frutinha mataria seria você.
    """, identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)
    return Escolhas(op, introducao="Você morreu.")

def acampamento():

    narrador(\
    """
    Mesmo com fome, você decide ignorar as frutinhas. Talvez não fosse uma boa comer elas.
    """,
    """
    Seguindo a trilha que você encontrou pelo mapa, você encontra um acampamento, que parece ter sido utilizado por pessoas recentemente.
    """,
    """
    Após passar pela entrada, você vê um refeitório a sua esquerda e várias barracas em volta de uma fogueira na direita.
    """,
    identacao=2)

    op1 = Opcao("Refeitório", lambda: refeitorio)
    op2 = Opcao("Barracas", lambda: barracas)
    return Escolhas(op1, op2, introducao="Qual lugar você decide investigar primeiro?:")

def refeitorio():

    narrador(\
        """
        Você decide checar o refeitório, em busca de encontrar algo para comer.
        O lugar estava deserto, sem nada nas mesas. Porém um barulho te chama a atenção.
        Um zumbi se encontrava preso na porta da cozinha.
        """,
        """
        Você quer investigar a cozinha pra ver se encontra alguma comida por lá, mas primeiro, você precisa se livrar do zumbi. Ele parece oferecer bastante perigo, mesmo estando preso.
        """,

        identacao=2)

    op1 = Opcao("Atacar o zumbi", lambda: atacar_zumbi)
    op2 = Opcao("Recuar e investigar as barracas", lambda: recuar)
    return Escolhas(op1, op2, introducao="O que você vai fazer?:")

def atacar_zumbi():

    narrador(\
    """
    Desarmado, você tenta ataca-lo. Ao bater no zumbi,
    você acaba fazendo com que ele não esteja mais preso na porta.
    """,
    """
    Você não tem força suficiente para matar um zumbi com seus punhos.
    O zumbi consegue te derrubar e acaba com sua vida, te devorando por completo.
    """, identacao=2)

    op = Opcao("Menu Inicial", especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def recuar():
    narrador(\
        """
        Você percebe que é muito perigoso tentar atacar o zumbi com apenas suas mãos e decide recuar. Sua única opção é investigar as barracas.
        """, identacao=2, continuar_final=True)

    return barracas

def barracas():
    narrador(\
        """
        Chegando nas barracas, você percebe que o lugar está uma bagunça.
        Roupas para todo lado, comidas desperdiçadas no chão, não parece ter nada de útil.
        Você escuta uns ruídos vindo de um rádio amador, e decide ouvir de perto.
        O sinal do rádio melhora e você consegue ouvir o noticiário informando:
        "Cuidado com as ruas, está acontecendo algo que nunca vimos antes, um apocalipse zumbi!! Pra todos que estiverem ouvindo essa notícia, se dirijam urgente ao centro da cidade, lá você encontrará o refúgio! Por favor, estejam seguros!"
        Apocalipse zumbi... É sério isso?? Agora tenho mais um motivo para me apressar.
        """,
        """
        Você encontra uma bola e um taco de beisebol. Parece que as pessoas que acampavam aqui estavam jogando.
        Você decide pegar o taco de beisebol, pois pode ser útil.
        +taco de beisebol adquirido!
        """,
        """
        Agora com o taco de beisebol em mãos, você pode entrar no refeitório ou deixar o acampamento.
        """,

        identacao=2)

    op1 = Opcao("Entrar no refeitório", lambda: entrar_refeitorio)
    op2 = Opcao("Ir embora", lambda: ir_embora)
    return Escolhas(op1, op2, introducao="O que você vai fazer?:")

def entrar_refeitorio():
    narrador(\
    """
    Entrando no refeitório, você dá de cara com o zumbi preso na porta da cozinha.
    Como não havia nada nas mesas do refeitório, a cozinha seria o único lugar a ter algo para comer.
    Você pega o taco de beisebol e acerta em cheio o zumbi. Derrubando-o no chão
    Não confiante que ele esteja morto, você acerta mais uma vez a cabeça do zumbi.
    """,
    """
    Você entra na cozinha e encontra alguns petiscos deixados pelas pessoas que acamparam aqui pela última vez. Não parece estarem vencidos, então você mata sua fome.
    """, identacao=2, continuar_final=True)

    return ir_embora

def ir_embora():
    narrador(\
        """
        Satisfeito com o que encontrou no acampamento, você decide ir embora.
        """,
        """
        Após uma longa caminhada pela floresta, você encontra um grande lago.
        A cidade parece estar próxima, porém terás que atravessar o lago se quiser chegar lá.
        Na beira do lago, há um barco movido a motor e um pequeno depósito.
        Você pensa que o barco pode ser uma boa e rápida opção para atravessar o lago, porém, dar a volta também é uma opção.
        """,
        identacao=2)

    op1 = Opcao("Usar o barco", lambda: part2.usar_barco)
    op2 = Opcao("Dar a volta", lambda: part2.voltar)
    return Escolhas(op1, op2, introducao="O que você vai fazer?:")
