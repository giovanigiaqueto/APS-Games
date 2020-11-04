
def narrador(*paragrafos, identacao=None, pergunta=None, continuar_final=False):

    # validar a pergunta

    __pergunta = pergunta
    if __pergunta is None:
        __pergunta = "continuar "

    # validar a identacao
    if identacao is None:
        identacao = ''

    elif isinstance(identacao, int):

        if identacao < 0:
            raise ValueError(("especial.narrador: identacao nao pode "
                f"ser um numero negativo, encontrado {identacao}"))

        identacao = ' ' * identacao

    elif not isinstance(identacao, str):
        raise TypeError(("especial.narrador: identacao deve ser um numero "
            f"positivo, texto ou None, encontrado {type(identacao)}"))

    # narrar paragrafos
    print()
    for indice, paragrafo in enumerate(corrigir_paragrafos(*paragrafos)):

        # adiciona a identacao
        paragrafo = '\n'.join([identacao + linha for linha in paragrafo.split('\n')])

        # mostra o paragrafo
        print('\n', paragrafo, end='\n\n', sep='')

        # espera o usuario digitar enter
        if continuar_final or indice < (len(paragrafos) - 1):

            # dica de enter somente no comeco do jogo
            if pergunta is None and not hasattr(narrador, 'primeiro_continue'):
                narrador.primeiro_continue = False
                input("aperte enter para continuar ")

            else:
                input(pergunta)

def corrigir_paragrafos(*paragrafos):

    paragrafos = remover_linhas_vazias(*paragrafos)
    paragrafos = remover_identacao(*paragrafos)
    return paragrafos

def remover_linhas_vazias(*paragrafos):

    for paragrafo in paragrafos:

        indice_inicial = 0
        indice_final = 0
        linhas = paragrafo.split('\n')

        for indice, linha in enumerate(linhas):

            if linha and not linha.isspace():
                indice_inicial = indice
                break

        for indice, linha in enumerate(linhas[::-1]):

            if linha and not linha.isspace():
                indice_final = len(linhas) - indice
                break

        yield '\n'.join(linhas[indice_inicial:indice_final])

def remover_identacao(*paragrafos):

    for paragrafo in paragrafos:

        # calcula a identacao
        identacao = detectar_identacao(paragrafo)

        # remove a identacao
        paragrafo = '\n'.join([linha[identacao:] for linha in paragrafo.split('\n')])

        # cria um generator para economizar memoria e agilizar a funcao
        yield paragrafo

def detectar_identacao(paragrafo):

    # calcula identacao
    ler_identacao = lambda linha: len(linha) - len(linha.lstrip())
    identacoes = [ler_identacao(linha) for linha in paragrafo.split('\n')]

    # menor identacao
    if len(identacoes) == 1:
        return identacoes[0]

    return min(*identacoes)
