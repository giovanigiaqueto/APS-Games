
from .auxiliares import carregar_qualquer

def carregar_par(texto, delimitador, *carregadores, preguicoso=False, estrito=False):

    _texto = texto

    carregadores_primeiro, carregadores_segundo = carregadores, carregadores
    if estrito:
        carregadores_primeiro, carregadores_segundo = carregadores

    primeiro_comprimento, primeiro = carregar_qualquer(texto, *carregadores_primeiro, preguicoso=True)
    texto = texto[primeiro_comprimento:]

    #LEGACY: implementacao antiga nao permitia um par (None, valor)
    #if primeiro is None:
    #    return None if not preguicoso else (0, None, None)

    match = delimitador.match(texto) #TODO: traducao de match
    if match is None:
        return None if not preguicoso else (primeiro_comprimento, primeiro, None)

    texto = texto[match.span()[1]:]

    segundo_comprimento, segundo = carregar_qualquer(texto, *carregadores_segundo, preguicoso=True)
    segundo_comprimento += match.span()[1]

    if segundo is None:
        #LEGACY: implementacao antiga nao permitia um par (valor, None) caso preguicoso=False
        #return None if not preguicoso else (primeiro_comprimento, primeiro, None)
        segundo_comprimento = 0

    texto = texto[segundo_comprimento:]
    if not preguicoso:
        return None if texto != '' and not texto.isspace() else (primeiro, segundo)

    return primeiro_comprimento + segundo_comprimento, primeiro, segundo

def carregar_sequencia(texto, delimitador, *carregadores, preguicoso=False, permite_unico=False):

    valores = []
    indice = 0

    while True:

        # carrega o proximo valor
        comprimento, valor = carregar_qualquer(texto[indice:], *carregadores, preguicoso=True)
        indice += comprimento

        # sem valor ou valor invalido
        if comprimento == 0 or valor is None:
            break

        # remove o delimitador
        match = delimitador.match(texto[indice:])
        if match is None:

            # previne uma lista com um item sem um delimitador no final
            if permite_unico or valores:
                valores.append(valor)

            break

        else:
            valores.append(valor)

        indice += match.span()[1]

    texto = texto[indice:]
    if not preguicoso and (texto != '' and texto.isspace()):
        return None

    return (indice, valores) if valores else (0, None)
