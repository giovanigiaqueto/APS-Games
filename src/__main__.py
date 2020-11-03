
from base import Opcao, Escolhas
import especial

from menu import *

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
