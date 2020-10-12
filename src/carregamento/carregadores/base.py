
import re

from .sequencias import carregar_sequencia
from .auxiliares import carregar_entre

from ..delimitadores import delim_virgula

def carregar_string(texto, *, preguicoso=False):

    match = re.match(r"'[^'\n\r]*'", texto) #TODO: traducao de match
    if match is None:
        return None if not preguicoso else (0, None)

    valor = texto[slice(*(match.span()))]
    texto = texto[match.span()[1]:]
    if not preguicoso and (texto != '' and not texto.isspace()):
        return None

    return (match.span()[1], valor)

def carregar_palavra(texto, *, preguicoso=False):

    match = re.match(r'\b\w+\b', texto) #TODO: traducao de match
    if match is None:
        return None if not preguicoso else (0, None)

    valor = texto[slice(*(match.span()))]
    texto = texto[match.span()[1]:]
    if not preguicoso and (texto != '' and not texto.isspace()):
        return None

    return (match.span()[1], valor)

def carregar_lista(texto, carregadores, preguicoso=False):

    return carregar_entre(texto, '[]', carregar_sequencia,
        args=(delim_virgula, *carregadores), preguicoso=preguicoso)
