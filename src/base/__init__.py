
class Opcao:

    """
    classe para escolhas feitas pelo usuario

    atributos:
        mensagem - texto da opcao
        funcao   - funcao da opcao

    permite:
        exibicao do texto da opcao com o metodo 'exibir',
        comparacao de igualdade com outros objetos,
        execucao da funcao interna quando o objeto e chamado
    """

    def __init__(self, mensagem, funcao=None):
        """cria um objeto do tipo Opcao que pode exibir a 'mensagem' na tela,
            ou executar sua funcao interna"""

        self._mensagem = mensagem
        self._funcao = funcao

    def __call__(self, *args, **kwargs):
        """executa a funcao interna, se disponivel, com os argumentos fornecidos"""

        if callable(self._funcao):
            return self._funcao(*args, **kwargs)

    def __repr__(self):
        """representacao textual da opcao"""
        return f"Opcao(msg='{self._mensagem}', func='{self._funcao}')"

    def __eq__(self, other):
        """implementacao do operador de igualdade"""

        # checa se o objeto é do mesmo tipo
        if not isinstance(other, Opcao):
            return False

        # checa se o objeto tem os mesmos valores
        return (self._mensagem  == other._mensagem and
                self._funcao    == other._funcao)

    def exibir(self, *, indice=None, identacao=None):
        """
        mostra o texto/mensagem da opcao no terminal.

        se 'indice' for fornecido, deve ser um numero positivo
        a ser mostrado antes que o texto da opcao.

        se 'identacao' for fornecido, deve ser um texto ou
        numero de espacos a serem mostrados antes da opcao.
        se indice for fornecido, esse texto sera mostrado antes dele.
        """

        # verifica e converte 'identacao' se necessario
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

        # verifica 'indice'
        if indice is None:
            indice = ''

        elif isinstance(indice, int):

            if indice < 0:
                # indice negativo, retorne um erro
                raise ValueError(("Opcao.exibir: indice nao pode ser "
                    f"um numero negativo, encontrado {indice}"))

            # indice numerico valido
            indice = f'{indice: 2} - '

        elif not isinstance(indice, str):
            # indice invalido de tipo desconhecido, retorne um erro
            raise ValueError(("Opcao.exibir: identacao deve ser um numero "
                f"positivo, texto ou None, encontrado '{indice}'"))

        # mostre o texto da opcao
        print(identacao, indice, self._mensagem, sep='')

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
        """
        manda o usuario escolher uma das opcoes da classe, retornando o numero
        da escolha e a opcao escolhida.

        imprime no terminal uma introducao, cada uma das opcoes com o seu numero
        de escolha e um texto de pergunta (padrao: 'escolha: '). se um numero
        invalido for fornecido, um erro sera mostrado e o usuario sera perguntado
        novamente ate uma resposta valida for entrada.

        se 'introducao' NAO for fornecido, a introducao padrao da classe sera
        usada em seu lugar, se nenhum delas forem fornecidas um erro sera mostrado.

        'pergunta', se fornecido, deve ser um texto.

        se 'indentacao' for fornecido, deve ser um texto ou um numero de espacos
        a ser imprimido antes de cada linha, permitido que o texto seja identado.
        """

        # valida e converte 'idetacao' se necessario
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


        # valida 'introducao' e se necessario usa a introducao do objeto
        if introducao is None:

            # nenhuma introducao fornecida, retorne um erro
            if self._introducao is None:
                raise ValueError(("Escolhas.entrada: nenhuma introducao foi "
                    "fornecida para a funcao e o objeto nao possui uma introducao padrao"))

            # usando a introducao padrao do objeto
            introducao = self._introducao

        elif not isinstance(introducao, str):
            # tipo invalido para introducao, retorne um erro
            raise TypeError(("Escolhas.entrada: introducao deve ser do tipo "
                f"texo ou None, encontrado {type(introducao)}"))

        elif not isinstance(identacao, str):
            raise TypeError(("Escolhas.entrada: identacao deve ser um numero "
                f"positivo, texto ou None, encontrado {type(identacao)}"))


        # valida e converte 'pergunta' se necessario
        if pergunta is None:
            pergunta = 'escolha: '


        # mostra a introducao
        print(identacao)
        print(identacao, introducao, sep='')

        # mostra as opcoes
        for indice, op in enumerate(self._opcoes):
            op.exibir(indice=indice, identacao='  '+identacao)

        # espacamento entre as opcoes e a pergunta
        print(identacao)

        # manda o usuario escolher uma opcao,
        # permanecendo no loop ate que um valor valido seja fornecido.
        indice_escolha = 0
        while True:

            # entrada da escolha
            try:
                valor = input(identacao + pergunta)
                indice_escolha = int(valor)
            except ValueError:
                pass
            else:
                # verifica se a escolha esta dentro dos valores permitidos
                if indice_escolha >= 0 and indice_escolha < len(self._opcoes):
                    break

            # escolha invalida
            print(identacao, 'escolha invalida, tente novamente', sep='')
            print(identacao)

        # retorna o numero da escolha e escolha do usuario
        return indice_escolha, self._opcoes[indice_escolha]

    def escolher(self, introducao=None, pergunta=None, identacao=None, *, args=tuple(), kwargs={}):
        """
        manda o usuario escolher uma das opcoes da classe, executando sua funcao
        com os argumentos fornecidos. chama o metodo 'escolher_indice' internamente.

        imprime no terminal uma introducao, cada uma das opcoes com o seu numero
        de escolha e um texto de pergunta (padrao: 'escolha: '). se um numero
        invalido for fornecido, um erro sera mostrado e o usuario sera perguntado
        novamente ate uma resposta valida for entrada.

        se 'introducao' NAO for fornecido, a introducao padrao da classe sera
        usada em seu lugar, se nenhum delas forem fornecidas um erro sera mostrado.

        'pergunta', se fornecido, deve ser um texto.

        se 'indentacao' for fornecido, deve ser um texto ou um numero de espacos
        a ser imprimido antes de cada linha, permitido que o texto seja identado.
        """

        # escolher a opcao atravez da funcao interna
        indice, opcao = self.escolher_indice(introducao, pergunta, identacao)

        # executa a opcao com os argumentos fornecidos
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
