
def carregar_qualquer(texto, *carregadores, preguicoso=False):

    validar = ((lambda resultado: resultado is not None) if not preguicoso else
                (lambda resultado: resultado[0] != 0 and resultado[1] is not None))

    resultado = None
    for carregador in carregadores:

        resultado = carregador(texto, preguicoso=preguicoso)
        if validar(resultado):
            return resultado

    return None if not preguicoso else (0, None)

def carregar_entre(texto, delimitadores, carregador, *,
    args=tuple(), kwargs={}, preguicoso=False):

    if not isinstance(delimitadores, str):
        raise TypeError(("carregar_entre: esperado str "
            f"para delimitadores, '{type(delimitadores)}' encontrado"))


    if len(delimitadores) == 1:
        delimitadores = delimitadores * 2

    elif len(delimitadores) != 2:
        raise ValueError(("carregar_entre: delimitadores deve ser uma string com 1 ou 2 caracters"))


    if not texto.startswith(delimitadores[0]):
        return None if not preguicoso else (0, None)


    comprimento_frontal = len(texto)
    texto = texto[1:].lstrip()

    comprimento_frontal -= len(texto)


    comprimento, valor = carregador(texto, *args, preguicoso=True, **kwargs)
    if comprimento == 0 or valor is None:
        return None if not preguicoso else (0, None)

    texto = texto[comprimento:]

    comprimento_posterior = len(texto)
    texto = texto.lstrip()

    comprimento_posterior -= len(texto)

    if texto[0] != delimitadores[1]:
        return None if not preguicoso else (0, None)

    texto = texto[1:]
    if not preguicoso:
        return None if texto != '' and not texto.isspace() else valor

    return (comprimento + comprimento_frontal + comprimento_posterior + 1, valor)
