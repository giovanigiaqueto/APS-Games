#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ..especial
from ..narracao import narrador
from ..base import Opcao, Escolhas

def cidade_esgoto():

    narrador(\
    """
    Com o pensamento de que poderiam passar despercebidos pelos zumbis,
    você decide ir com a ideia de ir pelos esgotos.
    """,
    """
    Já dentro do esgoto, alguns metros distantes de onde desceram,
    vocês encontram uma bifurcação.
    Mary comenta “Vamos pela esquerda, esquerda sempre é o caminho certo!”
    Já Edy, contesta “Isso é apenas uma possibilidade! Vamos continuar pela direita.”
    """, identacao=2)

    op = Opcao("Esquerda!", lambda: esgoto_esquerda)
    op = Opcao("Direita!",  lambda: esgoto_direita)

    return Escolhas(op1, op2, introducao="Mais uma vez, a decisão é sua")

def esgoto_esquerda():

    narrador(\
    """
    Você decide confiar na Mary e escolhe seguir pela esquerda.
    """,
    """
    Tudo parece tranquilo, até que vocês percebem que esse caminho não levaria a lugar nenhum.
    E pra piorar, havia vários zumbis por lá, que perceberam sua presença.
    """,
    """
    Ao dar meia volta, zumbis surgem do buraco que havia no esgoto,
    bloqueando a sua única saída.
    Você tenta matar os zumbis que haviam no caminho,
    porém você não imaginava que iriam aparecer tantos assim.
    """,
    """
    *click* *click*
    Sua munição acabou. Não tendo mais como se defender,
    você e seus amigos são encurralados, e suas vidas são tomadas.
    """, identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def esgoto_direita():
    pass
