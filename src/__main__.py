
from .base import Opcao, Escolhas
from . import especial

from .menu import *

from .rotas import inicio, cidade_1a, cidade_1b, cidade_2a, cidade_2b, floresta

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
            proximo = inicio.inicio

        elif gerenciador is especial.cidade_1a_inicio:
            proximo = cidade_1a.inicio

        elif gerenciador is especial.cidade_1b_inicio:
            proximo = cidade_1b.inicio

        elif gerenciador is especial.cidade_2a_inicio:
            proximo = cidade_2a.inicio

        elif gerenciador is especial.cidade_2b_inicio:
            proximo = cidade_2b.inicio

        elif gerenciador is especial.cidade_1b_saida:
            proximo = cidade_1a.descansar_ou_seguir

        elif gerenciador is especial.floresta:
            proximo = floresta.inicio

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

        #use para diagnosticos (debug)
        #if isinstance(gerenciador, Escolhas):
        #    print(*gerenciador, sep='\n')

    elif not (isinstance(proximo, (Opcao, Escolhas)) or callable(proximo) or
        especial.validar_gerenciador_especial(proximo)):
        print("erro: valor invalido desconhecido recebido", proximo)
        print("      depois de gerenciar", gerenciador, "retornando para o menu")

    else:
        gerenciador = proximo
        continue

    gerenciador = especial.menu
