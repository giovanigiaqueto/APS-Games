
from .sequencias import carregar_sequencia, carregar_par
from .auxiliares import carregar_entre

from ..delimitadores import delim_dois_pontos

def carregar_link(texto, *, preguicoso=False):

    _texto = texto.lstrip()
    if not _texto.startswith('link'):
        return None if not preguicoso else (0, None)

    _texto = _texto[4:].lstrip()

    carregar_attributos = lambda texto, preguicoso=False: \
        carregar_sequencia(texto, delim_espaco, carregar_palavra,
        preguicoso=preguicoso, permite_unico=True)

    comprimento, atributos, alvo = carregar_par(_texto, delim_dois_pontos,
        (carregar_attributos,), (carregar_string,), preguicoso=preguicoso, estrito=True)

    if comprimento == 0 or alvo is None:
        return None if not preguicoso else (0, None)

    atributos = set() if atributos is None else set(atributos)

    _texto = _texto[comprimento:]
    if _texto == '' or _texto.isspace():
        return None if not preguicoso else (0, None)

    return (atributos, alvo) if not preguicoso else (len(texto) - len(_texto), (atributos, alvo))

if __name__ == '__main__':

    alvo = "<link externo : 'arquivo.txt'>"

    print('carregando:', f"'{alvo}'")
    valor = carregar_entre(alvo, '<>', carregar_link)

    print(f'resultado:', valor)
