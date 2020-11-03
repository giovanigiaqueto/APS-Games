
import especial
from base import Opcao, Escolhas

def menu():

    op1 = Opcao("inicio", lambda: especial.inicio)
    op2 = Opcao("sair", lambda: sair_menu)

    return Escolhas(op1, op2, introducao="menu principal")

def sair_menu():

    op1 = Opcao("sim", lambda: especial.sair)
    op2 = Opcao("nao", lambda: especial.menu)

    return Escolhas(op1, op2, introducao="tem certeza que deseja sair?")
