#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import especial
from ..narracao import narrador
from ..base import Opcao, Escolhas

def usar_barco():
    narrador(\
    """
    Ao entrar no barco, você tenta dar partida, mas o barco não quer funcionar.
    Parece estar sem gasolina, talvez tenha um pouco guardado no depósito?
    """,

    identacao=2)

    op1 = Opcao("Procurar por gasolina no depósito", lambda: procurar)
    op2 = Opcao("Desistir e dar a volta no lago", lambda: voltar)
    return Escolhas(op1, op2, introducao="O que quer fazer?")

def procurar():
    narrador(\
    """
    Determinado a fazer o barco funcionar, você decide ir ao depósito encontrar gasolina.
    Chegando na porta, você não consegue abri-la.
    """,

    identacao=2)

    op1 = Opcao("Arrombar a porta", lambda: arrombar)
    op2 = Opcao("Disistir e dar a volta no lago", lambda: voltar)
    return Escolhas(op1, op2, introducao="Forço a entrada?")

def arrombar():
    narrador(\
    """
    Você não pensa em dar a volta e decide arrombar a porta.
    Entrando no depósito você encontra várias coisas de barcos.
    """,
    """
    Para sua sorte, há uma boa quantidade de gasolina pronta para ser utilizada.
    Você enche um recipiente que encontrou no depósito e leva para o barco.
    """,
    """
    Após encher o tanque, você consegue fazer o barco funcionar.
    Manuseando com cuidado o barco, você chega ao outro lado do lago.
    """,

    identacao=2)

    op1 = Opcao("Descer do outro lado do lago", lambda: lago)
    op2 = Opcao("Voltar? Tem certeza?", lambda : acampamento)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

#*******************************************************************

def voltar():
    narrador(\
    """
    Não querendo arriscar sua vida com o barco, decides dar a volta no lago.
    Tentando ver qual seria o lado mais rápido, não consegues chegar numa conclusão.
    Qual lado decide seguir?
    """,
    identacao=2)

    op1 = Opcao("Esquerda", lambda: esquerda)
    op2 = Opcao("Direita", lambda: direita)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def esquerda():
    narrador(\
    """
    Você decidiu ir pelo caminho da esquerda.
    Seguindo pela floresta, você vê alguns zumbis na trilha.
    Você decide...
    """,

    identacao=2)

    op1 = Opcao("Correr, na esperança de que os zumbis não te alcancem", lambda: correr)
    op2 = Opcao("Ser furtivo,passar por eles sem que te percebam", lambda: furtivo)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def correr():
    narrador(\
    """
    Esperando o momento certo, você decide correr!
    Para a sua sorte, os zumbis eram muito devagar e não conseguiram lhe alcançar.
    Após uma longa corrida, você deixa os zumbis para trás e chega ao outro lado do lago.
    """,
    identacao=2)
    op1 = Opcao("Chegada!", lambda: lago)
    op2 = Opcao("Voltar? Tem certeza?", lambda: voltar)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")


# ****************************************************
def furtivo():
    narrador(\
    """Com medo de ser notado pelos zumbis, você decide ser furtivo.
    Cuidadosamente, você passa por trás dos arbustos.
    """,
    """
    Os zumbis parecem ter escutado algo, porém não dão atenção.
    Após se distanciar um pouco dos zumbis, você continua o caminho numa velocidade maior,
    até que chegaste ao outro lado do lago.
    """,
    identacao=2)

    op1 = Opcao("Chegada!", lambda: lago)
    op2 = Opcao("Voltar? Tem certeza?", lambda: voltar)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

# *************************************************

def direita():
    narrador(\
    """
    Você decidiu ir pelo caminho da direita.
    Tudo parecia calmo, até que um lobo surge entre os arbustos.
    Ele não tem cara de quem vai deixar você se safar.
    Com uma alta chance dele lhe atacar, você decide:
    """,
    identacao=2)

    op1 = Opcao("Atacar o lobo", lambda: atacar)
    op2 = Opcao("Correr", lambda: correr)
    op3 = Opcao("Esperar e contra-atacar o lobo", lambda: contra_atacar)
    return Escolhas(op1, op2, op3, introducao="Oque você vai fazer?:")

def atacar():
    narrador(\
    """
    Com o taco de beisebol em mãos, você decide atacar o lobo!
    Porém você não contava com a velocidade dele.
    """,
    """
    O lobo desvia do seu ataque facilmente.
    E agora?
    """,
    identacao=2)

    op1 = Opcao("Atacar novamente", lambda: atacar_novamente)
    op2 = Opcao("Correr", lambda: correr)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def atacar_novamente():
    narrador(\
    """
    Você decide tentar a sorte de novo e...
    Mais uma vez, o lobo facilmente desvia de seu ataque.
    Sendo muito mais rápido que você, o lobo te ataca e não tem nada que você possa fazer.
    """,
    """
    *Você morreu*
    """,
    identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)
    return Escolhas(op, introducao="Você morreu.")

def correr():
    narrador(\
    """
    Não querendo arriscar sua sorte em atacar o lobo, você decide correr.
    Porém, o lobo é bem mais rápido que você, e aos poucos vai te alcançando.
    O que vai fazer?
    """,
    identacao=2)

    op1 = Opcao("Continuar correndo", lambda: correndo)
    op2 = Opcao("Subir em uma árvore", lambda: arvore)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def correndo():
    narrador(\
    """
    Você decide continuar correndo.
    Não foi umas das opções mais espertas, até porque você sabe que o lobo é mais rápido que você.
    Mesmo correndo tanto, você se cansa e o lobo te alcança, pulando em você e acabando com sua vida.
    """,
    """
    *Você morreu*
        """,
    identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def arvore():
    narrador(\
        """
    Você decide subir na árvore mais próxima.
    Logo após você ficar em cima do tronco, o lobo te alcança, e fica lhe encarando por vários minutos.
    """,
    """
    Cansado de esperar, ele desiste de te caçar e vai embora.
    Com receio do lobo ainda estar por perto, você decide esperar alguns minutos pra depois descer da árvore.
    Após uma pequena caminhada, você chega ao outro lado do lago.
     """,
    identacao=2)

    op1 = Opcao("Chegada!", lambda: lago)
    op2 = Opcao("Voltar? Tem certeza?", lambda: voltar)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

# *********************************************

def contra_atacar():
    narrador(\
    """
    Você decide esperar o lobo lhe atacar.
    E quando isso acontece...
    """,
    """
    *POW!!!*
    """,
    """
    Acertou o lobo em cheio!
    O lobo machucado, não quis tentar a sorte com você e decidiu fugir.
    Após o embate com o lobo, você continua o caminho até chegar ao outro lado do lago.
    """,
    identacao=2)

    op1 = Opcao("Chegada", lambda: lago)
    op2 = Opcao("Voltar? Tem certeza?", lambda: voltar)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

# *********************************************************

def lago():
    narrador( \
    """
    Ao chegar no outro lado do lago, você vê um único caminho.
    Caminho esse que levava direto para a cidade.
    """,
    """
    Você finalmente chegou na cidade.
    Na avenida principal, você consegue ver o refúgio a alguns metros de onde você está, porém uma horda de zumbis estava entre você e o refúgio. Chegar lá não parece ser fácil.
    O que pretende fazer?
    """,
    identacao=2)

    op1 = Opcao("Lutar no caminho para o refúgio", lambda: refugio)
    op2 = Opcao("Se camuflar com sangue de zumbi", lambda: sangue)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def refugio():
    narrador(\
    """
    Corajoso que você é, decides lutar pelo caminho até chegar no refúgio.
    Seu taco de beisebol dá conta de vários zumbis. Até que ele se quebra.
    Você está no meio da horda de zumbis sem nenhum tipo de arma.
    Sem nenhuma rota de fuga, você é cercado pelos zumbis, e devorado pelos mesmos.
    """,
    """
    *Você morreu.*
    """,
    identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def sangue():
    narrador(\
        """
        Você se lembra de ter visto essa façanha em um videogame, e decide tentar fazer o mesmo.
        Para sua sorte, há um zumbi separado da horda. Você chama a atenção dele e o acerta na
        cabeça e várias vezes na barriga, abrindo por dentro.
        Com o zumbi no chão, você abre o buraco feito na barriga do zumbi e enche suas mãos de sangue,
        e esfrega em todo seu rosto, corpo e roupas, até que esteja fedendo por completo, igual um zumbi.
        Pronto para um dos maiores desafios da sua vida, você segue em direção a horda.
        Você anda o mais devagar possível, para não tentar chamar atenção dos zumbis.
        Evitando o contato com eles, você consegue passar por uma boa parte, até que um zumbi para na sua frente.
        """,
        """
        Não sabendo o que fazer, você em estado de choque, fica parado, esperando.
        """,
        """
        O zumbi não encontrou nada de humano em você e decide sair do caminho.
        Com o coração na boca, você continua andando em direção ao refúgio.
        Finalmente você passa pela horda e se encontra na frente do portão do refúgio, onde guardas
        estão monitorando pela torre.
        Você acena para os guardas que correm para abrir o portão para ti.
        """,
        """
        Epílogo

        Dentro do refúgio, você pergunta para os guardas se duas pessoas chamadas Edy e Mary vieram para cá,
        porém eles não tinham informação nenhuma, e recomendaram que você fosse checar no dormitório.
        Chegando lá, você encontra seus amigos Edy e Mary, que chorava de felicidade por ver você vivo.
        Dizem eles que quando acordaram, estavam na beira da estrada todo machucados, por isso não estavam
        no carro comigo. Soldados do exército passaram por lá e trouxeram eles para o refúgio.
        “Tentamos de tudo para fazê-los voltarem lá e procurar por você, eles até foram, porém só encontraram
        um carro com ninguém dentro. Ficamos muitos preocupados que algo poderia ter acontecido com você.”
        Agora, uma nova vida se inicia. Como sobreviver a esse inesperado apocalipse? Só o futuro dirá.
        """,
        identacao=2, continuar_final=True)

    op = Opcao("Voltar ao Menu Princial", lambda : especial.menu)

    return Escolhas(op,
        introducao="Você completou o jogo. Obrigado por jogar SURVIVE IF YOU CAN!")
