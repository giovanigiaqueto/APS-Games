#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ..especial
from ..narracao import narrador
from ..base import Opcao, Escolhas

def inicio():

    narrador(\
    """
    Prólogo – Uma noite inesperada

    Eram duas da manhã, noite de lua cheia.
    Eu, Mary e Edy fomos a uma festa de um conhecido nosso, que morava na cidade vizinha.
    Como já estava ficando tarde, decidimos ir embora para casa.
    Estávamos de carro, porém, Mary e Edy estavam bêbados. Eu tive que dirigir.
    """,
    """
    Na metade do caminho, várias viaturas policiais e ambulâncias passaram por nós,
    no mesmo sentido que estávamos indo, a cidade. Todos nós começamos a suspeitar de algo.
    Minutos depois, conseguíamos ver a cidade de longe, porém, algo não parecia estar certo.
    """,
    """
    Conforme a gente se aproximava, presenciávamos vários acidentes que provavelmente
    ocorreram recentemente. Carros pegando fogo, pessoas desesperadas por algum motivo.
    """,
    identacao=2)

    op1 = Opcao("Presta atenção na estrada", lambda: rota_cidade)
    op2 = Opcao("Sintonizar na rádio da região", lambda: rota_floresta)

    return Escolhas(op1, op2, introducao="você:")

def rota_cidade():

    narrador(\
    """
    Capítulo 1 – Um novo dia

    Ao chegar na cidade, você repara que há muita destruição no caminho,
    pessoas correndo para todos os lados, saqueando mercados e farmácias.
    """,
    """
    Confuso com tudo que está acontecendo, você finalmente chega em sua casa.
    A casa toda estava apagada, seus pais não estavam presentes.
    Após olhar em todos os quartos, seus amigos te chamam na sala de estar.
    """,
    """
    Ao chegar lá, percebe que foi deixado um bilhete com um revólver acima.
    Provavelmente do seu pai. No bilhete, estava escrito:

    -Meu filho, eu espero que esteja tudo bem contigo.
    Você provavelmente deve estar confuso com o que está acontecendo,
    e infelizmente, é verdade. Tem monstros andando pelas ruas devorando as pessoas!
    Estão chamando-os de zumbis, no começo eu não acreditei,
    mas depois de ver as notícias, fiquei em choque.
    O exército mandou todo mundo se dirigir ao refúgio do outro lado da cidade.
    Então, pegue esse revólver para se proteger no caminho, estaremos te esperando lá.
    Tenha cuidado meu filho. – Pai

    +revólver adquirido!

    Edy e Mary não acreditavam no que havia acontecido na cidade.
    Decidimos partir o mais rápido possível.
    """,
    """
    Vocês entram no carro e vão em direção ao refúgio, porém,
    as ruas estão bloqueadas, impossibilitando a travessia com o carro.
    Não temos outra opção, vamos ter que abandonar o carro e ir andando.
    """,
    """
    Após andar alguns quarteirões,
    vocês dão de cara com uma horda de zumbis no centro da cidade.

    Edy sugere passar pela horda pelo esgoto,
    enquanto Mary, recomenda irmos pelo telhado dos prédios.
    """,
    identacao=2)

    op1 = Opcao("Ir pelo esgoto", lambda: especial.cidade_1a_inicio)
    op2 = Opcao("Ir pelos prédios", lambda: especial.cidade_1b_inicio)

    return Escolhas(op1, op2, introducao="Você quer continuar por onde?")

def rota_floresta():

    narrador(\
    """
    Curioso pra saber o que está acontecendo, você se distrai tentando ligar a rádio.
    Ao voltar os olhos para a estrada, uma pessoa no meio da estrada aparece.
    """,
    """
    Ao tentar desviar dessa pessoa, perdi o controle do carro e acabamos capotando,
    até que o carro bateu pela última vez, na floresta ao lado da estrada.
    E foi nesse último impacto, que acabei perdendo a consciência.
    """,
    """
    Capítulo 1 – Um novo dia

    Você finalmente acorda, com uma grande dor de cabeça, em cima do volante do carro.
    Após alguns minutos você percebe a situação que está, e vê que,
    além do carro quebrado, seus amigos não se encontram no local.
    A única informação que você tem é que ambas as portas estão abertas e que há muito sangue espalhado.
    """,
    """
    Ao sair do carro, você se depara com uma densa floresta.
    Desesperado, você pega o celular no seu bolso.
    Logo após você ligar o celular, você escuta um *beep*!
    Esse seria um sinal que a bateria do celular está acabando.
    """,
    """
    Sabendo que você estava perdido na floresta,
    você decidiu dar uma olhada no mapa da região para ter uma noção de onde estava na mata,
    e para talvez, encontrar algum caminho melhor.

    +conhecimento da área!

    Seu celular desligou por falta de bateria.
    """,
    """
    Após olhar o mapa, você segue o caminho mais apropriado para chegar na cidade.
    Não tão longe do seu ponto de partida, você encontra algumas frutinhas,
    nos arbustos ao lado da trilha. Sua barriga está roncando.
    """) # rota do Antônio, vou para aqui
