#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .. import especial
from ..base import Opcao, Escolhas
from ..narracao import narrador

def inicio():

    narrador(\
    """
    Sem tempo pra pensar, você pega a mochila e acerta Edy em cheio.
    Seu revólver que estava guardado, cai da mochila no chão.
    """,
    """
    Você pega o revólver e mira na cabeça de Edy. Na sua mente,
    você quer acabar com o sofrimento dele, porém, você não quer atirar nele.
    """, identacao=2)

    op1 = Opcao("Livrar Edy desta vida de Zumbi", lambda: livrar_edy)
    op2 = Opcao("Fugir", lambda: fugir)

    return Escolhas(op1, op2,
        introducao="Não tendo muito tempo até que Edy volte a te atacar, você:")

def livrar_edy():

    narrador(\
    """
    “Sinto muito Edy.”, foram suas últimas palavras para seu amigo.

    *bang*
    Com um disparo certeiro na cabeça, Edy desaba no chão.
    Seus olhos ficam cheio de lágrimas.
    Os acontecimentos dessa noite é algo que nunca imaginava acontecer.
    Você pega sua mochila e decide seguir para o refúgio.
    """, identacao=2, continuar_final=True)

    return refugio

def fugir():

    narrador(\
    """
    Você vê a oportunidade de fugir da casa,
    e não pensa duas vezes antes de fazer isso.
    """,
    """
    “Sinto muito Edy.”, foram suas últimas palavras para seu amigo.
    Deixando sua mochila de lado, você segue em direção ao refúgio.
    """, identacao=2, continuar_final=True)

    return refugio

def refugio():

    narrador(\
    """
    Devastado com os recentes acontecimentos, você enfim chega ao portão do refúgio.
    """,
    """
    De longe, consegue ver o portão se abrindo, e o que parecia ser duas pessoas saindo.
    Chegando mais perto, com a vista ainda meio embaçada, você não acredita no que vê.
    Seu corpo começa a tremer.
    """,
    """
    Na sua frente estavam, seus amigos. Edy, com uma bala na cabeça e Mary,
    toda ensanguentada. Ambos, falando ao mesmo tempo:
    “por que você não me salvou?”
    """,
    """
    “por que eu tive que morrer?”
    """,
    """
    “você matou a gente.”
    """, identacao=2, continuar_final=True)

    op1 = Opcao("Atirar nos dois", lambda: atirar_guardas)
    op2 = Opcao("Atirar em mim", lambda: atirar_em_si)

    return Escolhas(op1, op2, introducao="“VOCÊ MATOU A GENTE.”")

def atirar_guardas():

    narrador(\
    """
    Sua mente não aguenta mais. Porque estão me culpando? Você se pergunta.
    “Só me deixem em paz, por favor... ME DEIXEM EM PAZ!!”
    *bang* *bang*
    """
    """
    A dor de cabeça que te tanto incomodava, por um momento, vai embora.
    Porém, logo menos, você recobra a consciência da situação.
    Os dois corpos, mortos pelo disparo do seu revólver não eram Edy e Mary,
    e sim, dois guardas, que monitoravam o pessoal que chegava de fora.
    """
    """
    Você desacreditado, se ajoelha no chão e derruba sua arma.
    “O que foi que eu fiz para mere- “
    *bang*

    Um disparo mais alto e barulhento pôde se ouvir vindo da torre.
    Armado com um rifle de precisão, o soldado posicionado na torre
    efetua o disparo em você, apagando sua existência na hora.
    """, identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def atirar_em_si():

    narrador(\
    """
    As vozes de Edy e Mary ecoavam na sua cabeça. Você não tinha mais controle de você mesmo.
    Chorando por tudo que aconteceu, você leva o revólver para sua cabeça.
    """,
    """
    Pronto pra tirar sua própria vida, você escuta uma pessoa gritar na torre.
    “Não faça isso!”

    Essa pessoa desce as escadas correndo pra falar com você.
    A escuridão que você enxergava, se dispersava pela luz da esperança.
    Você encontrou seu pai, que estava ajudando na torre.
    Um abraço de pai e filho faz com que as vozes da sua cabeça desapareçam.
    Você percebe que na verdade quem estava na sua frente eram apenas dois guardas.
    """
    """
    Epílogo

    Seu pai te ajuda a caminhar para dentro do refúgio,
    para encontrar sua mãe que estava muito preocupada com você.

    Lá dentro você explica o motivo da tentativa de suicídio.
    Tudo o que aconteceu depois que você foi embora da festa na cidade vizinha.

    Você agora tem um longo caminho pela frente, mesmo seguro dentro do refúgio,
    com a companhia de seus pais, a morte de seus amigos será um grande peso
    que terás que carregar consigo pro resto da sua vida.
    """, identacao=2, continuar_final=True)

    op = Opcao("Voltar ao Menu", lambda: especial.menu)

    return Escolhas(op, introducao="Você completou o jogo. Obrigado por jogar SURVIVE IF YOU CAN!")
