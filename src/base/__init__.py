
class Opcao:

    def __init__(self, mensagem, funcao=None):
        """cria um objeto do tipo Opcao que pode exibir 'mensagem' na tela,
            ou executar sua funcao interna"""

        self._mensagem = mensagem
        self._funcao = funcao

    def __call__(self, *args, **kwargs):
        """executa a funcao interna se disponivel, (ex: opcao(1, 2, 3))"""

        if callable(self._funcao):
            return self._funcao(*args, **kwargs)

    def __repr__(self):
        return f"Opcao(msg='{self._mensagem}', func='{self._funcao}')"

    def __eq__(self, other):
        """implementacao do operador de igualdade '==''"""

        # checa se o objeto é do mesmo tipo
        if not isinstance(other, Opcao):
            return False

        # checa se o objeto tem os mesmos valores
        return (self._mensagem  == other._mensagem and
                self._funcao    == other._funcao)

    def exibir(self, *, indice=None, identacao=None):

        if identacao is None:
            identacao = ''

        elif isinstance(identacao, int):

            if identacao < 0:
                raise ValueError(("Opcao.exibir: identacao nao pode ser "
                    f"um numero negativo, encontrado {identacao}"))

            identacao = ' ' * identacao

        elif not isinstance(identacao, str):
            raise TypeError(("Opcao.exibir: identacao deve ser um numero "
                f"positivo, texto ou None, encontrado {type(identacao)}"))

        if indice is None:
            indice = ''

        elif isinstance(indice, int):

            if indice < 0:
                raise ValueError(("Opcao.exibir: indice nao pode ser "
                    f"um numero negativo, encontrado {indice}"))

            indice = f'{indice: 2} - '

        elif not isinstance(indice, str):
            raise ValueError(("Opcao.exibir: identacao deve ser um numero "
                f"positivo, texto ou None, encontrado '{indice}'"))

        print(identacao, indice, self.mensagem, sep='')

    @staticmethod
    def convertivel_para_opcao(self, objeto):

        if not isinstance(objeto, (list, tuple)):
            return False

        if len(objeto) != 2:
            return False

        if isinstance(objeto[0], str) and (objeto[1] is None or callable(objeto[1])):
            return True

        return False

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
            raise TypeError(("impossivel mudar Opcao.mensagem para "
                f"'{valor}', tipo nao permitido {type(valor)}"))

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
            raise TypeError(("impossivel mudar Opcao.funcao, "
                f"'{valor}' nao e uma funcao valida"))

class Escolhas:

    def __init__(self, *opcoes, introducao=None, copiar_opcoes=False):

        # valida as opcoes
        ops = []
        for indice, op in enumerate(opcoes):

            if isinstance(op, (tuple, list)):
                if Opcao.convertivel_para_opcao(op):
                    ops.append(Opcao(*op))

                else:
                    raise TypeError(("Escolhas.__init__: 'opcoes' deve conter "
                        f"valores do tipo 'Opcao', {op} encontrado no indice {index}"))

            elif isinstance(op, Opcao):
                ops.append(op.copiar() if copiar_opcoes else op)

            else:
                raise TypeError(("Escolhas.__init__: 'opcoes' deve conter valores "
                    f"do tipo 'Opcao', {op} encontrado no indice {index}"))

        if introducao is not None and not isinstance(introducao, str):
            raise TypeError(("Escolhas.__init__: introducao deve ser do tipo "
                f"str (texo) ou None, encontrado {type(introducao)}"))

        self._opcoes = ops
        self._introducao = introducao

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
            if not convertivel_para_opcao(valor):
                raise ValueError(("Escolhas: impossivel alterar o valor de "
                    f"'opcoes', valor invalido {valor}"))

            self._opcoes[chave] = Opcao(*valor)

        elif isinstance(valor, Opcao):
            self._opcoes[chave] = valor

        else:
            raise TypeError(("Escolhas: impossivel alterar o valor de 'opcoes'"
                f", tipo nao permitido {type(valor)}"))

        return chave

    def __delitem__(self, chave):
        # valida chave
        if not isinstance(chave, int) or chave < 0 or chave >= len(self._opcoes):
            raise IndexError(f"Escolhas.__setitem__: indice invalido {chave}")

        del self._opcoes[chave]

    def escolher_indice(self, introducao=None, pergunta=None, identacao=None):

        # valida e converte 'indetacao' se necessario
        if identacao is None:
            identacao = ''

        elif isinstance(identacao, int):

            if identacao < 0:
                raise ValueError(("Escolhas.entrada: identacao nao pode "
                    f"ser um numero negativo, encontrado {identacao}"))

            identacao = ' ' * identacao

        elif not isinstance(identacao, str):
            raise TypeError(("Escolhas.entrada: identacao deve ser um numero "
                f"positivo, texto ou None, encontrado {type(identacao)}"))

        if introducao is None:

            if self._introducao is None:
                raise ValueError(("Escolhas.entrada: nenhuma introducao foi "
                    "fornecida para a funcao e o objeto nao possui uma introducao padrao"))

            introducao = self._introducao

        elif not isinstance(introducao, str):
            raise TypeError(("Escolhas.entrada: introducao deve ser do tipo "
                f"texo ou None, encontrado {type(introducao)}"))

        # valida e converte 'pergunta' se necessario
        if pergunta is None:
            pergunta = 'escolha: '

        elif not isinstance(identacao, str):
            raise TypeError(("Escolhas.entrada: identacao deve ser um numero "
                f"positivo, texto ou None, encontrado {type(identacao)}"))

        # mostra a introducao
        print(identacao)
        print(identacao, introducao, sep='')

        # pergunta ao usuario as escolhas
        indice_escolha = 0
        while True:

            # mostra as opcoes
            for indice, op in enumerate(self._opcoes):
                op.exibir(indice=indice, identacao='  '+identacao)

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

        # retorna escolha
        return indice_escolha, self._opcoes[indice_escolha]

    def escolher(self, introducao=None, pergunta=None, identacao=None, *, args=tuple(), kwargs={}):

        # escolher opcao
        indice, opcao = self.escolher_indice(introducao, pergunta, identacao)

        # executar opcao
        return opcao(*args, **kwargs)

    @property
    def introducao(self):
        return self._introducao

    @introducao.setter
    def introducao(self, valor):

        if valor is None or isinstance(valor, str):
            self._introducao = valor
        else:
            raise TypeError(("Escolhas: impossivel alterar o valor de 'introducao'"
                f", tipo nao permitido {type(valor)}"))

    @property
    def opcoes(self):
        return list(self._opcoes)

    @opcoes.setter
    def opcoes(self, valor):

        ops = []
        for indice, op in enumerate(self._opcoes):
            if isinstance(op, (tuple, list)):
                if self.convertivel_para_opcao(op):
                    ops.append(Opcao(*op))

                else:
                    raise ValueError(("Escolhas: impossivel alterar o valor de "
                        f"'opcoes', valor invalido {valor}"))

            elif isinstance(Opcao):
                ops.append(op.copiar() if copiar_opcoes else op)

            else:
                raise TypeError(("Escolhas: impossivel alterar o valor de "
                    f"'opcoes', tipo nao permitido {type(valor)}"))

if __name__ == '__main__':

    funcao_A = lambda *args, **kwargs: print('funcao A executada')
    funcao_B = lambda *args, **kwargs: print('funcao B executada')
    funcao_C = lambda *args, **kwargs: print('funcao C executada')

    opcao_A = Opcao('opcao A', funcao_A)
    opcao_B = Opcao('opcao B', funcao_B)
    opcao_C = Opcao('opcao C', funcao_C)

    escolhas = Escolhas(opcao_A, opcao_B, opcao_C)

    escolhas.escolher('escolha uma opcao', 'opcao: ', identacao=2)
