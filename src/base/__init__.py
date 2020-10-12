
class Opcao:

    def __init__(self, mensagem, funcao=None):
        self._mensagem = mensagem
        self._funcao = funcao

    def __call__(self, *args, **kwargs):
        if callable(self._funcao):
            return self._funcao(*args, **kwargs)

    def __repr__(self):
        return f"Opcao(msg='{self._mensagem}', func='{self._funcao}')"

    def __eq__(self, other):
        return isinstance(other, Opcao) and self._mensagem == other._mensagem and self._funcao == other._funcao

    @property
    def mensagem(self):
        return str(self._mensagem)

    @mensagem.setter
    def mensagem(self, valor):
        if valor is None:
            self._mensagem = ''

        elif isinstance(valor, str):
            self._mensagem = str(valor)

        else:
            raise TypeError(f"impossivel mudar Opcao.mensagem para '{valor}', tipo invalido '{type(valor)}'")
    
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
            raise TypeError(f"impossivel mudar Opcao.funcao, '{valor}' nao e uma funcao valida")

class Escolhas:
    

    # ==================== LEGACY ====================
    #
    #def __init__(self, introducao, *opcoes, copiar_opcoes=False):
    #
    #    # valida introducao
    #    if not (introducao is None or isinstance(introducao, str)):
    #        raise TypeError(f"Escolhas.__init__: 'introducao' deve ser um texto ou None")
    #
    #    # valida as opcoes
    #    ops = []
    #    for indice, op in enumerate(opcoes):
    #
    #        if isinstance(op, (tuple, list)):
    #            if len(op) != 2 or not isinstance(op[0], str) or (op[1] is not None and not callable(op[1])):
    #                raise TypeError(f"Escolhas.__init__: 'opcoes' deve conter valores do tipo 'Opcao', {op} encontrado no indice {index}")
    #
    #            ops.append(Opcao(*op))
    #
    #        elif isinstance(Opcao):
    #            ops.append(op.copiar() if copiar_opcoes else op)
    #
    #       else:
    #           raise TypeError(f"Escolhas.__init__: 'opcoes' deve conter valores do tipo 'Opcao', {op} encontrado no indice {index}")    
    #    
    #   self._introducao = introducao
    #   self._opcoes = ops
    
    def __init__(self, *opcoes, copiar_opcoes=False): 
    
        # valida as opcoes
        ops = []
        for indice, op in enumerate(opcoes):
            
            if isinstance(op, (tuple, list)):
                if len(op) != 2 or not isinstance(op[0], str) or (op[1] is not None and not callable(op[1])):
                    raise TypeError(f"Escolhas.__init__: 'opcoes' deve conter valores do tipo 'Opcao', {op} encontrado no indice {index}")
                
                ops.append(Opcao(*op))
                
            elif isinstance(op, Opcao):
                ops.append(op.copiar() if copiar_opcoes else op)
                
            else:
                raise TypeError(f"Escolhas.__init__: 'opcoes' deve conter valores do tipo 'Opcao', {op} encontrado no indice {index}")    
        
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

        if isinstance(valor, (tuple, list)):
            if len(valor) != 2 or not isinstance(valor[0], str) or (valor[1] is not None and not callable(valor[1])):
                raise TypeError(f"Escolhas: impossivel alterar o valor de 'opcoes', valor invalido {valor}")

            self._opcoes[chave] = Opcao(*valor)

        elif isinstance(valor, Opcao):
            self._opcoes[chave] = valor

        else:
            raise TypeError(f"Escolhas: impossivel alterar o valor de 'opcoes', o valor invalido {valor}")

        return chave

    def __delitem__(self, chave):
        # valida chave
        if not isinstance(chave, int) or chave < 0 or chave >= len(self._opcoes):
            raise IndexError(f"Escolhas.__setitem__: indice invalido {chave}")

        del self._opcoes[chave]

    def escolher(self, introducao, pergunta=None, *, args=tuple(), kwargs={}, identacao=None):
        
        # valida e converte 'indetacao' se necessario
        if identacao is None:
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
        
        # mostra a introducao
        print(identacao)
        print(identacao, introducao, sep='')

        # pergunta ao usuario as escolhas
        indice_escolha = 0
        while True: 

            # mostra as opcoes
            for indice, op in enumerate(self._opcoes):
                print(identacao, '  {: 2} - '.format(indice), op.mensagem, sep='')
        
            # entrada da escolha
            try:
                print(identacao)
                valor = input(identacao + pergunta)
                indice_escolha = int(valor)
            except ValueError:
                pass
            else:
                # escolha valida
                if indice_escolha >= 0 and indice_escolha < len(self._opcoes):
                    break
            
            # escolha invalida 
            print(identacao, 'escolha invalida, tente novamente', sep='')

        # executa escolha
        return self._opcoes[indice_escolha](*args, **kwargs)

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
            if isinstance(op, (tuple, list)):
                if len(indice) != 2 or not isinstance(op[0], str) or (op[1] is not None and not callable(op[1])):
                    raise TypeError(f"Escolhas: impossivel alterar o valor de 'opcoes', valor invalido {valor}")

                ops.append(Opcao(*op))

            elif isinstance(Opcao):
                ops.append(op.copiar() if copiar_opcoes else op)

            else:
                raise TypeError(f"Escolhas: impossivel alterar o valor de 'opcoes', o valor invalido {valor}")

if __name__ == '__main__':

    funcao_A = lambda *args, **kwargs: print('funcao A executada')
    funcao_B = lambda *args, **kwargs: print('funcao B executada')
    funcao_C = lambda *args, **kwargs: print('funcao C executada')

    opcao_A = Opcao('opcao A', funcao_A)
    opcao_B = Opcao('opcao B', funcao_B)
    opcao_C = Opcao('opcao C', funcao_C)
    
    escolhas = Escolhas(opcao_A, opcao_B, opcao_C)

    escolhas.escolher('escolha uma opcao', 'opcao: ', identacao=2)
