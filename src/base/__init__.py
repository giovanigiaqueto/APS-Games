
class Opcao:

    def __init__(self, mensagen, funcao=None):
        self._mensagen = mensagen
        self._funcao = funcao

    def __call__(self, *args, **kwargs):
        if callable(self._callback):
            return self._callback(*args, **kwargs)

    def __repr__(self):
        return f"Opcao(msg='{self._mensagen}', func='{self._funcao}')"

    def mensagen(self):
        return str(self._mensagen)

    @property
    def mensagen(self, valor):
        if valor is None:
            self._mensagen = ''

        elif hasattr(valor, '__str__'):
            self._mensagen = str(valor)

        else:
            raise TypeError(f"impossivel mudar Opcao.mensagen para '{value}', tipo invalido '{type(value)}'")
    
    @property
    def funcao(self):
        return self._funcao

    @funcao.setter
    def funcao(self, valor):
        if valor is None:
            self._funcao = None

        elif callable(valor):
            self._funcao = valor

        else:
            raise TypeError(f"impossivel mudar Opcao.funcao, '{value}' nao e uma funcao valida")

class Escolhas:
    
    def __init__(self, introducao, *opcoes, copiar_opcoes=False):

        # valida introducao
        if not (introducao is None or isinstance(introducao, str)):
            raise TypeError(f"Escolhas.__init__: 'introducao' deve ser um texto ou None")

        # valida as opcoes
        ops = []
        for indice, op in enumerate(opcoes):

            if isinstance(op, (tuple, list))
                if len(op) != 2 or not isinstance(op[0], str) or (op[1] is not None and not callable(op[1])):
                    raise TypeError(f"Escolhas.__init__: 'opcoes' deve conter valores do tipo 'Opcao', {op} encontrado no indice {index}")

                ops.append(Opcao(*op))

            elif isinstance(Opcao):
                ops.append(op.copiar() if copiar_opcoes else op)

            else:
                raise TypeError(f"Escolhas.__init__: 'opcoes' deve conter valores do tipo 'Opcao', {op} encontrado no indice {index}")    
        
        self._introducao = introducao
        self._opcoes = ops
    
    def __bool__(self):
        return bool(self._opcoes)

    def __len__(self):
        return len(self._opcoes)

    def __contains__(self, valor):
        return valor in self._opcoes

    def __getitem__(self, chave): 
        # valida chave
        if not isinstance(chave, int) or chave < 0 or chave >= len(self._opcoes):
            raise IndexError(f"Escolhas.__setitem__: indice invalido {chave}")

        return self._opcoes[chave]

    def __setitem__(self, chave, valor):
        # valida chave
        if not isinstance(chave, int) or chave < 0 or chave >= len(self._opcoes):
            raise IndexError(f"Escolhas.__setitem__: indice invalido {chave}")

        if isinstance(valor, (tuple, list))
            if len(valor) != 2 or not isinstance(valor[0], str) or (valor[1] is not None and not callable(valor[1])):
                raise TypeError(f"Escolhas: impossivel alterar o valor de 'opcoes', valor invalido {valor}")

            self._opcoes[chave] = Opcao(*valor)

        elif isinstance(Opcao):
            self._opcoes[chave] = ops.append(op.copiar() if copiar_opcoes else op

        else:
            raise TypeError(f"Escolhas: impossivel alterar o valor de 'opcoes', o valor invalido {valor}")

        return chave

    def __delitem__(self, chave):
        # valida chave
        if not isinstance(chave, int) or chave < 0 or chave >= len(self._opcoes):
            raise IndexError(f"Escolhas.__setitem__: indice invalido {chave}")

        del self._opcoes[chave]

    def entrada(self, introducao, args, kwargs, *, pergunta=None, indentacao=None):
        
        # valida e converte 'indetacao' se necessario
        if indentacao is None:
            identacao = ''

        elif isinstance(identacao, int):

            if identacao < 0:
                raise ValueError(f"Escolhas.entrada: indentacao deve ser um numero positivo, texto ou None, encontrado '{identacao}'")

            identacao = ' ' * identacao

        elif not isinstance(identacao, str):
            raise ValueError(f"Escolhas.entrada: indentacao deve ser um numero positivo, texto ou None, encontrado '{identacao}'")

        # valida e converte 'pergunta' se necessario
        if pergunta is None:
            pergunta = 'escolha: '

        elif not isinstance(identacao, str):
            raise ValueError(f"Escolhas.entrada: indentacao deve ser um numero positivo, texto ou None, encontrado '{identacao}'")

        # pergunta ao usuario as escolhas
        indice_escolha = 0
        while True

            # mostra a introducao
            print(identacao, self._introducao, sep='')

            # mostra as opcoes
            for indice, op in enumerate(self._opcoes):
                print(identacao, '{: 2} - '.format(indice), op.mensagen, sep='')
        
            # entrada da escolha
            try:
                valor = input(pergunta)
                indice_escolha = int(valor)
            except ValueError:
                pass
            else:
                # escolha valida
                if indice_escolha >= 0 or indice_escolha < len(self._opcoes):
                    break
            
            # escolha invalida
            print(identacao)
            print(identacao, 'escolha invalida, tente novamente', sep='')

        # executa escolha
        return self._opcoes[indice_escolhas](*args, **kwargs)

    @property
    def introducao(self):
        return str(self._introducao)

    @introducao.setter
    def introducao(self, valor):

        if not (valor is None or isinstance(valor, str)):
            raise TypeError(f"Escolhas: impossivel alterar o valor de 'introducao', valor invalid {valor}")

        self._introducao = '' if valor is None else valor

    @property
    def opcoes(self):
        return list(self._opcoes)

    @opcoes.setter
    def opcoes(self, valor):
        
        ops = []
        for indice, op in enumerate(self._opcoes):
            if isinstance(op, (tuple, list))
                if len(indice) != 2 or not isinstance(op[0], str) or (op[1] is not None and not callable(op[1])):
                    raise TypeError(f"Escolhas: impossivel alterar o valor de 'opcoes', valor invalido {valor}")

                ops.append(Opcao(*op))

            elif isinstance(Opcao):
                ops.append(op.copiar() if copiar_opcoes else op)

            else:
                raise TypeError(f"Escolhas: impossivel alterar o valor de 'opcoes', o valor invalido {valor}")

