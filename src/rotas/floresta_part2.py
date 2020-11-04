import especial
from narracao import narrador
from base import Opcao, Escolhas


def usar_barco():
    narrador(\
        'Ao entrar no barco, você tenta dar partida, mas o barco não quer funcionar.'
        'Parece estar sem gasolina, talvez tenha um pouco guardado no depósito?'
        'O que quer fazer?'
    identacao=2)

    op1 = Opcao("Procurar por gasolina no depósito", lambda: procurar)
    op2 = Opcao("Desistir e dar a volta no lago", lambda: voltar)
    return Escolhas(op1, op2, introducao="O que você vai fazer?:")

def procurar():
    narrador(\
        'Determinado a fazer o barco funcionar, você decide ir ao depósito encontrar gasolina.'
        'Chegando na porta, você não consegue abri-la.'
        'Forço a entrada?'
    identacao=2)

    op1 = Opcao("Arrombar a porta", lambda: arrombar)
    op2 = Opcao("Disistir e dar a volta no lago", lambda: voltar)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def arrombar():
    narrador(\
        'Você não pensa em dar a volta e decide arrombar a porta.'
        'Entrando no depósito você encontra várias coisas de barcos.'
        'Para sua sorte, há uma boa quantidade de gasolina pronta para ser utilizada.'
        'Você enche um recipiente que encontrou no depósito e leva para o barco.'
        'Após encher o tanque, você consegue fazer o barco funcionar.'
        'Manuseando com cuidado o barco, você chega ao outro lado do lago.'
     )
# **************AQUI PARA CONTINUAR APÓS O LAGO***************************
def voltar():
    narrador(\
        'Não querendo arriscar sua vida com o barco, decides dar a volta no lago.'
        'Tentando ver qual seria o lado mais rápido, não consegues chegar numa conclusão.'
        'Qual lado decide seguir?'
    identacao=2)

    op1 = Opcao("Esquerda", lambda: esquerda)
    op2 = Opcao("Direita", lambda: direita)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def esquerda():
    narrador(\'
        'Você decidiu ir pelo caminho da esquerda.'
        'Seguindo pela floresta, você vê alguns zumbis na trilha.'
        'Você decide...'
    identacao=2)

    op1 = Opcao("Correr, na esperança de que os zumbis não te alcancem", lambda: correr)
    op2 = Opcao("Ser furtivo,passar por eles sem que te percebam", lambda: furtivo)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")
def correr():
    narrador(\
        'Esperando o momento certo, você decide correr!'
        'Para a sua sorte, os zumbis eram muito devagar e não conseguiram lhe alcançar.'
        'Após uma longa corrida, você deixa os zumbis para trás e chega ao outro lado do lago.'
     )

# ******************AQUI PARA CONTINUAR APÓS O LAGO**********************************
def furtivo():
    narrador(\
        'Com medo de ser notado pelos zumbis, você decide ser furtivo.'
'Cuidadosamente, você passa por trás dos arbustos.'
'Os zumbis parecem ter escutado algo, porém não dão atenção.'
'Após se distanciar um pouco dos zumbis, você continua o caminho numa velocidade maior, '
'até que chegaste ao outro lado do lago.'
     )

# *****************AQUI PARA CONTINUAR APÓS O LAGO************************************

def direita():
    narrador(\
        'Você decidiu ir pelo caminho da direita.'
        'Tudo parecia calmo, até que um lobo surge entre os arbustos.'
        'Ele não tem cara de quem vai deixar você se safar.'
        'Com uma alta chance dele lhe atacar, você decide:'
    identacao=2)

    op1 = Opcao("Atacar o lobo", lambda: atacar)
    op2 = Opcao("Correr", lambda: correr)
    op3 = Opcao("Esperar e contra-atacar o lobo", lambda: contra_atacar)
    return Escolhas(op1, op2, op3, introducao="Oque você vai fazer?:")

def atacar():
    narrador(\
        'Com o taco de beisebol em mãos, você decide atacar o lobo!'
        'Porém você não contava com a velocidade dele.'
        'O lobo desvia do seu ataque facilmente.'
        'E agora?'
    identacao=2)

    op1 = Opcao("Atacar novamente", lambda: atacar_novamente)
    op2 = Opcao("Correr", lambda: correr)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def atacar_novamente():
    narrador(\
        'Você decide tentar a sorte de novo e...'
        'Mais uma vez, o lobo facilmente desvia de seu ataque.'
        'Sendo muito mais rápido que você, o lobo te ataca e não tem nada que você possa fazer.'
        '*Você morreu*'
    identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def correr():
    narrador(\
        'Não querendo arriscar sua sorte em atacar o lobo, você decide correr.'
        'Porém, o lobo é bem mais rápido que você, e aos poucos vai te alcançando.'
        'O que vai fazer?'
    identacao=2)

    op1 = Opcao("Continuar correndo", lambda: correndo)
    op2 = Opcao("Subir em uma árvore", lambda: arvore)
    return Escolhas(op1, op2, introducao="Oque você vai fazer?:")

def correndo():
    narrador(\
        'Você decide continuar correndo.'
        'Não foi umas das opções mais espertas, até porque você sabe que o lobo é mais rápido que você.'
        'Mesmo correndo tanto, você se cansa e o lobo te alcança, pulando em você e acabando com sua vida.'
        '*Você morreu*'
    identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def arvore():
    narrador(\
        'Você decide subir na árvore mais próxima.'
        'Logo após você ficar em cima do tronco, o lobo te alcança, e fica lhe encarando por vários minutos.'
        'Cansado de esperar, ele desiste de te caçar e vai embora.'
        'Com receio do lobo ainda estar por perto, você decide esperar alguns minutos pra depois descer da árvore.'
        'Após uma pequena caminhada, você chega ao outro lado do lago.'
    )
    # ***************AQUI PARA CONTINUAR APÓS O LAGO****************************************

def contra_atacar():
    narrador(\
        'Você decide esperar o lobo lhe atacar.'
        'E quando isso acontece... *pow!*'
        'Acertou o lobo em cheio!'
        'O lobo machucado, não quis tentar a sorte com você e decidiu fugir.'
        'Após o embate com o lobo, você continua o caminho até chegar ao outro lado do lago.'
    )
    # ******************AQUI PARA CONTINUAR APÓS O LAGO*****************************************
