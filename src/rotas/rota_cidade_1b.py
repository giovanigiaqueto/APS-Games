#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ..especial
from ..narracao import narrador
from ..base import Opcao, Escolhas

def rota_cidade_1b():

    narrador( \
        """
        Não sabendo se o esgoto é uma opção segura, você decide confiar no caminho da Mary e ir pelos prédios.
        Chegando num beco, Mary diz que a gente precisava subir as escadas que ficavam na parte de fora do prédio, para conseguir acesso ao telhado.
        Após alguns segundos você consegue ouvir o que seria uma grande quantidade de zumbis vindo de onde vocês vieram.
        Você ajuda Edy a subir na escada, depois Mary, e por último, você.
        """,

        """
        Ao chegar no telhado do prédio, vocês conseguem ver de longe o refúgio que foi montado, porém, havia uma boa distância entre vocês.
        Indo de prédio em prédio pelo telhado, evitando os zumbis, nós três conseguimos passar por uma boa parte da horda.
        Até que no último prédio, ao tentar pular, Mary se desequilibra e não consegue alcançar o prédio em que eu e Edy estávamos.
        Ao olhar para trás, não vimos a Mary do nosso lado. Só ouvimos um enorme barulho que veio do beco.
        """,

        """
        Só podia ser ela.
        Ao voltar e olhar para baixo, você vê Mary desacordada em cima de uma caçamba de lixo.
        """,

        identacao=2)

    op1 = Opcao("Abandonar Mary", lambda: continuar_mary)
    op2 = Opcao("Descer e salvar Mary", lambda: descer_predio)
    return Escolhas(op1, op2, introducao="Você decide:")


def descer_predio():
    narrador( \
        """
        Você desce as escadas correndo pra tentar socorrer Mary.
        Ao chegar no chão você vê muito sangue.
        Mary não parece desacordada, mas ao ver o corpo dela, você não acredita no que vê.
        Um metal passou por dentro do corpo dela.
        """,

        """
        Ao mencionar isso para Mary, ela fica desesperada gritando por ajuda. Isso chama a atenção dos zumbis por perto.
        Pedindo para que ela acalmasse, você tenta puxar o corpo dela para cima, mas, ela grita de tanta dor. Você para de puxar ela.
        Olhando para as saídas do beco, você vê zumbis se aproximando. Você não tem muito tempo.
        """,

        identacao=2)

    op1 = Opcao("Salvar Mary", lambda: salvar_morte)
    op2 = Opcao("Fugir", lambda: continuar_mary2)
    return Escolhas(op1, op2, introducao="O que decide fazer?:")

def salvar_morte():
    narrador( \
        """
        Não querendo abandonar sua amiga, você a avisa que vai puxar com tudo para tirar ela de lá.
        E mesmo assim, você não consegue puxar Mary pois o metal havia perfurado bastante, se continuasse puxando, quem mataria Mary seria eu.
        O problema é que os zumbis já nos cercavam. A escada para o telhado já estava bloqueada pelos zumbis.
        Você mata os zumbis que se aproximam, porém a cada disparo, mais zumbis iam aparecendo.
        """,

        """
        Gritos de dor e sofrimento ecoavam pelo beco.
        Ao olhar para trás, você vê sua amiga chorando pela sua vida, que acabava naquele momento, sendo devorada na sua frente.
        Sua sanidade havia acabado ali. Você gasta toda sua munição nos zumbis em cima de Mary.
        Não havia mais nada que você poderia fazer. Os zumbis juntam em cima de você e acabam com sua vida.
        Você morreu.
        """,


        identacao=2)

    op1 = Opcao("Menu Principal", lambda: especial.menu)
    return Escolhas(op1)

def continuar_mary():
    narrador(\
        """
        Desesperado, você e Edy voltam correndo para ver o que aconteceu.
        Ao olhar pra baixo, vocês veem o corpo de Mary, ensanguentado, desacordada.
        Você não acredita que Mary morreu desse jeito.
        O barulho da queda fez com que vários zumbis se reunissem ao redor do corpo dela.
        O restante você decidiu não ver.
        """,

        """
        Depois de ficarem por um tempo lá pensando no que aconteceu, você e Edy decidem descer do prédio.
        Ainda no beco, ao passar por perto da caçamba de lixo, um zumbi surpreende o seu amigo e acaba mordendo a perna dele.
        """,

        identacao=2)

    op1 = Opcao("Atirar no zumbi", lambda: atirar_zumbi_predio)
    op2 = Opcao("Salvar munição", lambda: salvar_municao_predio)
    return Escolhas(op1, op2, introducao="Você decide:")


def continuar_mary2():

    narrador(\
        """
        Analisando a situação, você percebe que não iria conseguir resgatar Mary não importa o tanto que tentasse.
        Se ficasse mais tempo ali, iria ficar cercado pelos zumbis.
        “Mary, me perdoa...” são suas últimas palavras para ela, antes de dar a volta e subir as escadas de volta para o telhado.
        Não olhando para trás, você só consegue ouvir os gritos de dor e sofrimento, do que parecia ser os últimos momentos de sua amiga.
        """,

        """
        Depois de ficarem por um tempo lá pensando no que aconteceu, você e Edy decidem descer do prédio.
        Ainda no beco, ao passar por perto da caçamba de lixo, um zumbi surpreende o seu amigo e acaba mordendo a perna dele.
        """,

        identacao=2)

    op1 = Opcao("Atirar no zumbi", lambda: atirar_zumbi_predio)
    op2 = Opcao("Salvar munição", lambda: salvar_municao_predio)
    return Escolhas(op1, op2, introducao="Você decide:")

def atirar_zumbi_predio():
    narrador(\
        """
        Sem perder tempo, você decide atirar no zumbi pra deixar Edy livre.
        Zumbis começam a se dirigir a sua direção por causa do barulho, e você escapa de lá, ajudando Edy a andar.
        """,

        identacao=2)

    return especial.cidade_1b_saida

def salvar_municao_predio():
    narrador(\
        """
        Você decide ajudar Edy sem gastar munição, porém leva mais tempo, e isso faz com que a mordida seja mais severa.
        Edy vai precisar de um apoio para conseguir andar.
        """,

        identacao=2)

    return especial.cidade_1b_saida
