
class GerenciadorEspecial(type):

    instancias = {}

    def __init__(cls, nome, bases, atributos):

        assert nome.startswith("Gerenciador"), 'o nome da classe deve comecar com Gerenciador'

        bases = tuple(list(bases) + [GerenciadorEspecial])

        super(GerenciadorEspecial, cls).__init__(cls, bases, atributos)

        nome_instancia = nome.lstrip("Gerenciador").strip('_').lower()
        globals()[nome_instancia] = cls()

    def __call__(cls, *args, **kwargs):

        instancia = GerenciadorEspecial.instancias.get(cls, None)
        if instancia is not None:
            return instancia

        instancia = super(GerenciadorEspecial, cls).__call__(*args, **kwargs)
        GerenciadorEspecial.instancias[cls] = instancia

        return instancia

def validar_gerenciador_especial(valor):
    return type(valor) in GerenciadorEspecial.instancias

class GerenciadorMenu(metaclass=GerenciadorEspecial):
    pass

class GerenciadorSair(metaclass=GerenciadorEspecial):
    pass

class GerenciadorInicio(metaclass=GerenciadorEspecial):
    pass

class GerenciadorCidade_1A_Inicio(metaclass=GerenciadorEspecial):
    pass

class GerenciadorCidade_1B_Inicio(metaclass=GerenciadorEspecial):
    pass

class GerenciadorCidade_2A_Inicio(metaclass=GerenciadorEspecial):
    pass

class GerenciadorCidade_2B_Inicio(metaclass=GerenciadorEspecial):
    pass

class GerenciadorCidade_1B_Saida(metaclass=GerenciadorEspecial):
    pass
