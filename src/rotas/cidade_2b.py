#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ..especial
from ..narracao import narrador
from ..base import Opcao, Escolhas

def rota_cidade_2b():
        narrador( \
        """
        Preocupado com sua vida no momento, você decide pegar o que parece ser a única coisa que pode causar dano.
        Ao pegar o pedaço de madeira, Edy acaba mordendo seu outro braço.
        Você acerta em cheio a cabeça dele, afastando-o de você.
        Olhando para seu amigo, que agora é um zumbi
        """,
            
        identacao=2)

    op1 = Opcao("Acabar com o sofrimento dele", lambda: acabar_sofrimento)
    op2 = Opcao("Fugir", lambda: fugir_casa)
    return Escolhas(op1, op2, introducao="Você decide:")


def acabar_sofrimento():
    narrador( \
        """
        “Sinto muito Edy.”, foram suas últimas palavras para seu amigo.
        Com o pedaço de madeira, você acerta várias vezes a cabeça de Edy.
        Seus olhos ficam cheio de lágrimas. Os acontecimentos dessa noite é algo que nunca imaginava acontecer.
        Você pega sua mochila e decide seguir para o refúgio.
        """,

        identacao=2, continuar_final=True)

    return fim_casa

def fugir_casa():
    narrador( \
        """
        Você vê a oportunidade de fugir da casa, e não pensa duas vezes antes de fazer isso.
        “Sinto muito Edy.”, foram suas últimas palavras para seu amigo.
        Após pegar sua mochila, você foge da casa e segue em direção ao refúgio. 
        """,

        identacao=2, continuar_final=True)

    return fim_casa

def fim_casa()
    narrador( \
        """
        Já a alguns quarteirões distante da casa abandonada, você se lembra da mordida que levou no braço, e parece bem feio.
        """,
        
         identacao=2)

    op1 = Opcao("Deixar a mostra", lambda: deixar_amostra)
    op2 = Opcao("Esconder mordida", lambda: esconder_mordida)
    return Escolhas(op1, op2, introducao="Deixar do jeito que está, ou esconder com a camisa?:")


##final rota_cidade_2b 1
def deixar_amostra()
    narrador( \
        """
        Você prefere deixar a mordida a mostra, talvez os guardas do refúgio te encaminhem o quanto antes para a equipe médica.
        Ao chegar no portão do refúgio, os guardas aparecem pra te receber.
        Porém eles mandam você se afastar por que você tinha chances de se tornar um zumbi, por causa da mordida.
        """,

        """
        Inconformado, você menciona que sua família está lá dentro.
        Os guardas não se importam com isso. Eles obrigam você ir embora, se não iriam atirar.
        Não resta outra opção.
        """,

        identacao=2)

    return epilogo_mordida_amostra

def epilogo_mordida_amostra()
    narrador( \
        """
        Com a entrada para o refúgio rejeitada, você, desiludido e desemparado, não tem para onde ir.
        Ao abrir a mochila para ver o que você havia para sobreviver, encontra o revólver deixado por seu pai.
        """,

        """
        Você dá uma última olhada na culpada por tudo isso, a mordida. Sabes que a qualquer momento, você vai virar um deles.
        Viver seus últimos momentos andando por aí, ou acabar com tudo isso com uma bala? De qualquer forma, eu vou morrer mesmo.
        Eu deveria ter trazido uma cerveja...
        """,

        """
        Você completou o jogo. Obrigado por jogar SURVIVE IF YOU CAN!
        """,
        identacao=2)
    
    return especial.menu

##final rota_cidade_2b 2
def fim_casa()
    narrador( \
        """
        Você acha que seria bom esconder a mordida, então você a cobre toda com sua camisa.
        Devastado com os recentes acontecimentos, você enfim chega ao portão do refúgio.
        De longe, consegue ver o portão se abrindo, e o que parecia ser duas pessoas saindo.
        """,

        """
        Chegando mais perto, com a vista ainda meio embaçada, você não acredita no que vê.
        Seu corpo começa a tremer.
        Na sua frente estavam, seus amigos. Edy, com uma bala na cabeça e Mary, toda ensanguentada.
        Ambos, falando ao mesmo tempo:
        """,

        """
        “por que você não me salvou?”
        """,

        """
        “por que eu tive que morrer?”
        """,

        """
        “você matou a gente.”
        """,

        identacao=2)

    op1 = Opcao("Atirar nos dois", lambda: atirar_duo)
    op2 = Opcao("Atirar em mim", lambda: atirar_mim)
    return Escolhas(op1, op2, introducao="“VOCÊ MATOU A GENTE.”")

def atirar_duo()
    narrador( \
        """
        Sua mente não aguenta mais. Porque estão me culpando? Você se pergunta.
        “Só me deixem em paz, por favor... ME DEIXEM EM PAZ!!”
        *bang* *bang*
        A dor de cabeça que te tanto incomodava, por um momento, vai embora.
        Porém, logo menos, você recobra a consciência da situação.
        """,

        """
        Os dois corpos, mortos pelo disparo do seu revólver não eram Edy e Mary, e sim, dois guardas.
        Guardas que monitoravam o pessoal que chegava de fora.
        Você desacreditado, se ajoelha no chão e derruba sua arma.
        “O que foi que eu fiz para mere- “
        *bang*
        """,

        """
        Um disparo mais alto e barulhento pôde se ouvir vindo da torre.
        Armado com um rifle de precisão, o soldado posicionado na torre efetua o disparo em ti, apagando sua existência na hora.
        Você morreu.
        """,
        identacao=2)
    
    return especial.menu

def atirar_mim()
    narrador( \
        """
        As vozes de Edy e Mary ecoavam na sua cabeça. Você não tinha mais controle de você mesmo.
        Chorando por tudo que aconteceu, você leva o revólver para sua cabeça.
        Pronto pra tirar sua própria vida, você escuta uma pessoa gritar na torre.
        “Não faça isso!”
        """,

        """
        Essa pessoa desce as escadas correndo pra falar com você.
        A escuridão que você enxergava, se dispersava pela luz da esperança.
        Você encontrou seu pai, que estava ajudando na torre.
        """,

        """
        Um abraço de pai e filho faz com que as vozes da sua cabeça desapareçam.
        Você percebe que na verdade quem estava na sua frente eram apenas dois guardas.
        Após isso, seu pai te leva para dentro do refúgio, onde você se reencontra com sua mãe e vocês três matam a saudade.
        Porém, havia um tópico muito importante a ser discutido.
        Só dependia de você, se seus pais, teriam conhecimento do que aconteceu, ou não.
        """,

    identacao = 2)

    op1 = Opcao("Não Contar", lambda: nao_contar)
    op2 = Opcao("Contar", lambda: contar)
    return Escolhas(op1, op2, introducao="Contar?")


def nao_contar()
    narrador( \
        """
        Você decide esconder a mordida de seus pais e de todo mundo.
        Porém, com o passar do tempo você começa ficar febril e se sentir mal.
        E foi no meio da noite, onde todo mundo descansava, que o pior acontece.
        """,

        """
        As pessoas do dormitório nunca imaginavam que havia um zumbi entre eles.
        Eu fiz algo que nunca na minha vida teria feito.
        Sim, meus pais foram as minhas primeiras vítimas.
        """,

        """
        Após a morte deles, algumas pessoas acordaram e viram a cena, e começaram a gritar pedindo por ajuda.
        Não demorou muito para os guardas aparecerem, e com isso, acabarem com minha vida de morto-vivo.
        """,
        
        identacao=2)

    return epilogo_mordida_amostra


def epilogo_nao_contar()
    narrador( \
        """
        O dormitório todo estava em choque. As pessoas presenciaram um ato que nunca, jamais queriam ter que ver.
        Pegaram o meu corpo para fazer pesquisas científicas sobre os mortos-vivos.
        Espero que eu seja útil pelo menos para isso.
        Mãe, Pai, Mary, Edy. Me desculpem. A culpa é toda minha.
        Eu que fui a causa da morte de vocês. Espero algum dia receber o perdão de vocês.
        """,

        """
        Você completou o jogo. Obrigado por jogar SURVIVE IF YOU CAN!
        """,
        identacao=2)

    return especial.menu


def contar()
    narrador( \
        """
        Você conta para seus pais sobre a mordida, deixando-os super preocupados.
        Eles decidem te levar imediatamente para o médico do refúgio.
        Chegando lá, o médico ao ver a mordida do zumbi fica desesperado, e sai correndo para chamar os guardas.
        """,

        """
        Os guardas entram no consultório e sem perguntar questões, pegam você pelo braço e o arrastam para fora do refúgio.
        Seus pais gritavam para que não fizessem isso com você, mas, há regras no refúgio, para a segurança de toda a população.
        """,

        identacao=2)

    return epilogo_mordida_amostra


def epilogo_contar()
    narrador( \
        """
        Expulso do refúgio, separado de seus pais, sem seus dois amigos, e podendo virar zumbi a qualquer momento.
        Você não consegue imaginar um dia pior que esse.
        E pensar que o responsável por eu não poder ficar no refúgio foi o Edy...
        Maldito, porque ele foi me morder?
        """,

        """
        Enfim, você dá uma última olhada na culpada por tudo isso, a mordida. Sabes que a qualquer momento, você vai virar um deles.
        Viver seus últimos momentos andando por aí, ou acabar com tudo isso com uma bala?
        De qualquer forma, eu vou morrer mesmo. Eu deveria ter aproveitado a festa melhor...
        """,

        """
        Você completou o jogo. Obrigado por jogar SURVIVE IF YOU CAN!
        """,
        
        identacao=2)

    return especial.menu
