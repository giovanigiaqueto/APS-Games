
from src.carregamento.carregadores.auxiliares import *
from src.carregamento import *

import pytest

class TestCarregarQualquer:

    def test_carregamento_simples(self):

        assert carregar_qualquer("'A'", carregar_string) == "'A'"
        assert carregar_qualquer("A", carregar_palavra) == "A"
        assert carregar_qualquer("'A'", carregar_string, carregar_palavra) == "'A'"
        assert carregar_qualquer("A", carregar_string, carregar_palavra) == "A"
        assert carregar_qualquer("A", carregar_string) is None
        assert carregar_qualquer("'A'", carregar_palavra) is None

        assert carregar_qualquer("'A'   ", carregar_string) == "'A'"
        assert carregar_qualquer("A   ", carregar_palavra) == "A"
        assert carregar_qualquer("'A'   ", carregar_string, carregar_palavra) == "'A'"
        assert carregar_qualquer("A   ", carregar_string, carregar_palavra) == "A"
        assert carregar_qualquer("A   ", carregar_string) is None
        assert carregar_qualquer("'A'   ", carregar_palavra) is None

        assert carregar_qualquer("'A''C'", carregar_string) is None
        assert carregar_qualquer("A'C'", carregar_palavra) is None
        assert carregar_qualquer("'A''C'", carregar_string, carregar_palavra) is None
        assert carregar_qualquer("A'C'", carregar_string, carregar_palavra) is None
        assert carregar_qualquer("A'C'", carregar_string) is None
        assert carregar_qualquer("'A''C'", carregar_palavra) is None

    def test_carregamento_preguicoso(self):

        assert carregar_qualquer("'A'",
            carregar_string, preguicoso=True) == (3, "'A'")
        assert carregar_qualquer("A",
            carregar_palavra, preguicoso=True) == (1, "A")
        assert carregar_qualquer("'A'", carregar_string,
            carregar_palavra, preguicoso=True) == (3, "'A'")
        assert carregar_qualquer("A", carregar_string,
            carregar_palavra, preguicoso=True) == (1, "A")
        assert carregar_qualquer("A",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_qualquer("'A'",
            carregar_palavra, preguicoso=True) == (0, None)

        assert carregar_qualquer("'A'   ",
            carregar_string, preguicoso=True) == (3, "'A'")
        assert carregar_qualquer("A   ",
            carregar_palavra, preguicoso=True) == (1, "A")
        assert carregar_qualquer("'A'   ",
            carregar_string, carregar_palavra, preguicoso=True) == (3, "'A'")
        assert carregar_qualquer("A   ",
            carregar_string, carregar_palavra, preguicoso=True) == (1, "A")
        assert carregar_qualquer("A   ",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_qualquer("'A'   ",
            carregar_palavra, preguicoso=True) == (0, None)

        assert carregar_qualquer("'A''C'",
            carregar_string, preguicoso=True) == (3, "'A'")
        assert carregar_qualquer("A'C'",
            carregar_palavra, preguicoso=True) == (1, "A")
        assert carregar_qualquer("'A''C'",
            carregar_string, carregar_palavra, preguicoso=True) == (3, "'A'")
        assert carregar_qualquer("A'C'",
            carregar_string, carregar_palavra, preguicoso=True) == (1, "A")
        assert carregar_qualquer("A'C'",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_qualquer("'A''C'",
            carregar_palavra, preguicoso=True) == (0, None)

class TestCarregarEntre:

    class TestCarregamentoSimples:

        def test_basico(self):

            assert carregar_entre("['A']", '[]', carregar_string) == "'A'"
            assert carregar_entre("['A' ]", '[]', carregar_string) == "'A'"
            assert carregar_entre("[ 'A']", '[]', carregar_string) == "'A'"
            assert carregar_entre("[ 'A' ]", '[]', carregar_string) == "'A'"

            assert carregar_entre("['A']  ", '[]', carregar_string) == "'A'"
            assert carregar_entre("[ 'A']  ", '[]', carregar_string) == "'A'"
            assert carregar_entre("['A' ]  ", '[]', carregar_string) == "'A'"
            assert carregar_entre("[ 'A' ]  ", '[]', carregar_string) == "'A'"

            assert carregar_entre("['A']'C'", '[]', carregar_string) is None
            assert carregar_entre("['A' ]'C'", '[]', carregar_string) is None
            assert carregar_entre("[ 'A']'C'", '[]', carregar_string) is None
            assert carregar_entre("[ 'A' ]'C'", '[]', carregar_string) is None

        def test_valor_invalido(self):

            assert carregar_entre("[A]", '[]', carregar_string) is None
            assert carregar_entre("[A ]", '[]', carregar_string) is None
            assert carregar_entre("[ A]", '[]', carregar_string) is None
            assert carregar_entre("[ A ]", '[]', carregar_string) is None

            assert carregar_entre("[A]  ", '[]', carregar_string) is None
            assert carregar_entre("[ A]  ", '[]', carregar_string) is None
            assert carregar_entre("[A ]  ", '[]', carregar_string) is None
            assert carregar_entre("[ A ]  ", '[]', carregar_string) is None

            assert carregar_entre("[A]'C'", '[]', carregar_string) is None
            assert carregar_entre("[A ]'C'", '[]', carregar_string) is None
            assert carregar_entre("[ A]'C'", '[]', carregar_string) is None
            assert carregar_entre("[ A ]'C'", '[]', carregar_string) is None

        def test_parenteses_invalido(self):

            assert carregar_entre("('A']", '[]', carregar_string) is None
            assert carregar_entre("('A' ]", '[]', carregar_string) is None
            assert carregar_entre("( 'A']", '[]', carregar_string) is None
            assert carregar_entre("( 'A' ]", '[]', carregar_string) is None

            assert carregar_entre("('A']  ", '[]', carregar_string) is None
            assert carregar_entre("( 'A']  ", '[]', carregar_string) is None
            assert carregar_entre("('A' ]  ", '[]', carregar_string) is None
            assert carregar_entre("( 'A' ]  ", '[]', carregar_string) is None

            assert carregar_entre("('A']'C'", '[]', carregar_string) is None
            assert carregar_entre("('A' ]'C'", '[]', carregar_string) is None
            assert carregar_entre("( 'A']'C'", '[]', carregar_string) is None
            assert carregar_entre("( 'A' ]'C'", '[]', carregar_string) is None


            assert carregar_entre("['A')", '[]', carregar_string) is None
            assert carregar_entre("['A' )", '[]', carregar_string) is None
            assert carregar_entre("[ 'A')", '[]', carregar_string) is None
            assert carregar_entre("[ 'A' )", '[]', carregar_string) is None

            assert carregar_entre("['A')  ", '[]', carregar_string) is None
            assert carregar_entre("[ 'A')  ", '[]', carregar_string) is None
            assert carregar_entre("['A' )  ", '[]', carregar_string) is None
            assert carregar_entre("[ 'A' )  ", '[]', carregar_string) is None

            assert carregar_entre("['A')'C'", '[]', carregar_string) is None
            assert carregar_entre("['A' )'C'", '[]', carregar_string) is None
            assert carregar_entre("[ 'A')'C'", '[]', carregar_string) is None
            assert carregar_entre("[ 'A' )'C'", '[]', carregar_string) is None


            assert carregar_entre("('A')", '[]', carregar_string) is None
            assert carregar_entre("('A' )", '[]', carregar_string) is None
            assert carregar_entre("( 'A')", '[]', carregar_string) is None
            assert carregar_entre("( 'A' )", '[]', carregar_string) is None

            assert carregar_entre("('A')  ", '[]', carregar_string) is None
            assert carregar_entre("( 'A')  ", '[]', carregar_string) is None
            assert carregar_entre("('A' )  ", '[]', carregar_string) is None
            assert carregar_entre("( 'A' )  ", '[]', carregar_string) is None

            assert carregar_entre("('A')'C'", '[]', carregar_string) is None
            assert carregar_entre("('A' )'C'", '[]', carregar_string) is None
            assert carregar_entre("( 'A')'C'", '[]', carregar_string) is None
            assert carregar_entre("( 'A' )'C'", '[]', carregar_string) is None

        def test_parenteses_e_valor_invalido(self):

            assert carregar_entre("(A]", '[]', carregar_string) is None
            assert carregar_entre("(A ]", '[]', carregar_string) is None
            assert carregar_entre("( A]", '[]', carregar_string) is None
            assert carregar_entre("( A ]", '[]', carregar_string) is None
            assert carregar_entre("[A)", '[]', carregar_string) is None
            assert carregar_entre("[A )", '[]', carregar_string) is None
            assert carregar_entre("[ A)", '[]', carregar_string) is None
            assert carregar_entre("[ A )", '[]', carregar_string) is None
            assert carregar_entre("(A)", '[]', carregar_string) is None
            assert carregar_entre("(A )", '[]', carregar_string) is None
            assert carregar_entre("( A)", '[]', carregar_string) is None
            assert carregar_entre("( A )", '[]', carregar_string) is None

            assert carregar_entre("(A]   ", '[]', carregar_string) is None
            assert carregar_entre("(A ]   ", '[]', carregar_string) is None
            assert carregar_entre("( A]   ", '[]', carregar_string) is None
            assert carregar_entre("( A ]   ", '[]', carregar_string) is None
            assert carregar_entre("[A)   ", '[]', carregar_string) is None
            assert carregar_entre("[A )   ", '[]', carregar_string) is None
            assert carregar_entre("[ A)   ", '[]', carregar_string) is None
            assert carregar_entre("[ A )   ", '[]', carregar_string) is None
            assert carregar_entre("(A)   ", '[]', carregar_string) is None
            assert carregar_entre("(A )   ", '[]', carregar_string) is None
            assert carregar_entre("( A)   ", '[]', carregar_string) is None
            assert carregar_entre("( A )   ", '[]', carregar_string) is None

            assert carregar_entre("(A]'C'", '[]', carregar_string) is None
            assert carregar_entre("(A ]'C'", '[]', carregar_string) is None
            assert carregar_entre("( A]'C'", '[]', carregar_string) is None
            assert carregar_entre("( A ]'C'", '[]', carregar_string) is None
            assert carregar_entre("[A)'C'", '[]', carregar_string) is None
            assert carregar_entre("[A )'C'", '[]', carregar_string) is None
            assert carregar_entre("[ A)'C'", '[]', carregar_string) is None
            assert carregar_entre("[ A )'C'", '[]', carregar_string) is None
            assert carregar_entre("(A)'C'", '[]', carregar_string) is None
            assert carregar_entre("(A )'C'", '[]', carregar_string) is None
            assert carregar_entre("( A)'C'", '[]', carregar_string) is None
            assert carregar_entre("( A )'C'", '[]', carregar_string) is None

    class TestCarregamentoPreguicoso:

        def test_basico(self):

            assert carregar_entre("['A']", '[]',
                carregar_string, preguicoso=True) == (5, "'A'")
            assert carregar_entre("['A' ]", '[]',
                carregar_string, preguicoso=True) == (6, "'A'")
            assert carregar_entre("[ 'A']", '[]',
                carregar_string, preguicoso=True) == (6, "'A'")
            assert carregar_entre("[ 'A' ]", '[]',
                carregar_string, preguicoso=True) == (7, "'A'")

            assert carregar_entre("['A']  ", '[]',
                carregar_string, preguicoso=True) == (5, "'A'")
            assert carregar_entre("[ 'A']  ", '[]',
                carregar_string, preguicoso=True) == (6, "'A'")
            assert carregar_entre("['A' ]  ", '[]',
                carregar_string, preguicoso=True) == (6, "'A'")
            assert carregar_entre("[ 'A' ]  ", '[]',
                carregar_string, preguicoso=True) == (7, "'A'")

            assert carregar_entre("['A']'C'", '[]',
                carregar_string, preguicoso=True) == (5, "'A'")
            assert carregar_entre("['A' ]'C'", '[]',
                carregar_string, preguicoso=True) == (6, "'A'")
            assert carregar_entre("[ 'A']'C'", '[]',
                carregar_string, preguicoso=True) == (6, "'A'")
            assert carregar_entre("[ 'A' ]'C'", '[]',
                carregar_string, preguicoso=True) == (7, "'A'")

        def test_valor_invalido(self):

            assert carregar_entre("[A]", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A ]", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A]", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A ]", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("[A]  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A]  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A ]  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A ]  ", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("[A]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A ]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A ]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)

        def test_parenteses_invalido(self):

            assert carregar_entre("('A']", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("('A' ]", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A']", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A' ]", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("('A']  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A']  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("('A' ]  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A' ]  ", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("('A']'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("('A' ]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A']'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A' ]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)


            assert carregar_entre("['A')", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("['A' )", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ 'A')", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ 'A' )", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("['A')  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ 'A')  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("['A' )  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ 'A' )  ", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("['A')'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("['A' )'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ 'A')'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ 'A' )'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)


            assert carregar_entre("('A')", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("('A' )", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A')", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A' )", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("('A')  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A')  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("('A' )  ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A' )  ", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("('A')'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("('A' )'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A')'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( 'A' )'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)

        def test_parenteses_e_valor_invalido(self):

            assert carregar_entre("(A]", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A ]", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A]", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A ]", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A)", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A )", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A)", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A )", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A)", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A )", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A)", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A )", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("(A]   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A ]   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A]   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A ]   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A)   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A )   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A)   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A )   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A)   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A )   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A)   ", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A )   ", '[]',
                carregar_string, preguicoso=True) == (0, None)

            assert carregar_entre("(A]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A ]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A ]'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A)'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[A )'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A)'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("[ A )'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A)'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("(A )'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A)'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
            assert carregar_entre("( A )'C'", '[]',
                carregar_string, preguicoso=True) == (0, None)
