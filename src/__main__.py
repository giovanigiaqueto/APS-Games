
from base import Opcao, Escolhas
import especial

def menu():

    op1 = Opcao("inicio", lambda: especial.inicio)
    op2 = Opcao("sair", lambda: sair_menu)

    return Escolhas(op1, op2, introducao="menu principal")

def sair_menu():

    op1 = Opcao("sim", lambda: especial.sair)
    op2 = Opcao("nao", lambda: especial.menu)

    return Escolhas(op1, op2, introducao="tem certeza que deseja sair?")

def inicio():

    op1 = Opcao("sair vivo", lambda: viver)
    op2 = Opcao("tentar nao morrer", lambda: morrer)

    return Escolhas(op1, op2, introducao="{inserir introducao inicio}")

def viver():

    op1 = Opcao("completar o jogo", lambda: completar_jogo)
    op2 = Opcao("olha para traz", lambda: olhar)

    return Escolhas(op1, op2, introducao="{inserir introducao inicio-1a}")

def morrer():

    op1 = Opcao("voltar para o menu", lambda: menu)
    return  Escolhas(op1, introducao="voce morreu")

def olhar():

    op1 = Opcao("voltar para o menu", lambda: menu)
    return Escolhas(op1, introducao="voce olha para traz e morre")

def completar_jogo():

    op1 = Opcao("voltar para o menu", lambda: menu)
    return Escolhas(op1, introducao="voce completa o jogo, mas morre no processo")

gerenciador = menu
proximo = None

while True:

    if isinstance(gerenciador, Escolhas):
        proximo = gerenciador.escolher()

    elif especial.validar_gerenciador_especial(gerenciador):

        if gerenciador is especial.sair:
            break

        elif gerenciador is especial.menu:
            proximo = menu

        elif gerenciador is especial.inicio:
            proximo = inicio

        else:
            print( "erro: falha ao gerenciar GerenciadorEspecial,",
                  f"      acao desconhecida '{gereciador}',",
                   "      retornando ao menu", sep='\n')

            proximo = especial.menu

    elif isinstance(gerenciador, Opcao) or callable(gerenciador):
        proximo = gerenciador()

    else:
        print("erro: gerenciador desconhecido detectado",
            gerenciador, "retornando ao menu")

        gerenciador = especial.menu
        continue

    if proximo is None:
        print("erro: valor invalido None recebido depois de gerenciar",
            gerenciador, ", retornando ao menu")

    elif not (isinstance(proximo, (Opcao, Escolhas)) or callable(proximo) or
        especial.validar_gerenciador_especial(proximo)):
        print("erro: valor invalido desconhecido recebido", proximo)
        print("      depois de gerenciar", gerenciador, "retornando para o menu")

    else:
        gerenciador = proximo
        continue

    gerenciador = especial.menu
