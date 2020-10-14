
from src.carregamento import *

import pytest

class TestCarregarString:

    def test_carregamento_simples(self):

        assert carregar_string("'A'") == "'A'"
        assert carregar_string("'A'   ") == "'A'"
        assert carregar_string("'A''B'") is None
        assert carregar_string("''A''B''") is None

        assert carregar_string("") is None
        assert carregar_string("A'B'") is None

    def test_carregamento_preguicoso(self):

        assert carregar_string("'A'", preguicoso=True) == (3, "'A'")
        assert carregar_string("'A''B'", preguicoso=True) == (3, "'A'")
        assert carregar_string("''A''B''", preguicoso=True) == (2, "''")

        assert carregar_string("", preguicoso=True) == (0,  None)
        assert carregar_string("A'B'", preguicoso=True) == (0, None)

class TestCarregarPalavra:

    def test_carregamento_simples(self):

        assert carregar_palavra("ABC") == "ABC"
        assert carregar_palavra("ABC    ") == "ABC"
        assert carregar_palavra("ABC DEF") is None

        assert carregar_palavra("") is None
        assert carregar_palavra(" ") is None

    def test_carregamento_preguicoso(self):

        assert carregar_palavra("ABC", preguicoso=True) == (3, "ABC")
        assert carregar_palavra("ABC    ", preguicoso=True) == (3, "ABC")
        assert carregar_palavra("ABC DEF", preguicoso=True) == (3, "ABC")

        assert carregar_palavra("", preguicoso=True) == (0, None)
        assert carregar_palavra(" ", preguicoso=True) == (0, None)

class TestCarregarLista:

    def test_carregamento_simples(self):

        assert carregar_lista("['A', 'B']", carregar_string) == ["'A'", "'B'"]
        assert carregar_lista("['A' 'B']", carregar_string) is None
        assert carregar_lista("'A', 'B'", carregar_string) is None

        assert carregar_lista("['A', 'B']   ", carregar_string) == ["'A'", "'B'"]
        assert carregar_lista("['A' 'B']   ", carregar_string) is None
        assert carregar_lista("'A', 'B'    ", carregar_string) is None

        assert carregar_lista("['A', 'B']'C'", carregar_string) is None
        assert carregar_lista("['A' 'B']'C'", carregar_string) is None
        assert carregar_lista("'A', 'B' 'C'", carregar_string) is None

        carregadores = (carregar_string, carregar_palavra)
        assert carregar_lista("[A, 'B']", *carregadores) == ["A", "'B'"]
        assert carregar_lista("['A', B]", *carregadores) == ["'A'", "B"]
        assert carregar_lista("['A', 'B']", *carregadores) == ["'A'", "'B'"]
        assert carregar_lista("[A, B]", *carregadores) == ["A", "B"]

        assert carregar_lista("[A, 'B']   ", *carregadores) == ["A", "'B'"]
        assert carregar_lista("['A', B]   ", *carregadores) == ["'A'", "B"]
        assert carregar_lista("['A', 'B']   ", *carregadores) == ["'A'", "'B'"]
        assert carregar_lista("[A, B]   ", *carregadores) == ["A", "B"]

        assert carregar_lista("[A, 'B']'C'", *carregadores) is None
        assert carregar_lista("['A', B]'C'", *carregadores) is None
        assert carregar_lista("['A', 'B']'C'", *carregadores) is None
        assert carregar_lista("[A, B]'C'", *carregadores) is None

        del carregadores
        assert carregar_lista("[A, B]", carregar_string) is None
        assert carregar_lista("[A, 'B']", carregar_string) is None
        assert carregar_lista("['A', B]", carregar_string) is None

        assert carregar_lista("[A, B]   ", carregar_string) is None
        assert carregar_lista("[A, 'B']   ", carregar_string) is None
        assert carregar_lista("['A', B]   ", carregar_string) is None

        assert carregar_lista("[A, B]'C'", carregar_string) is None
        assert carregar_lista("[A, 'B']'C'", carregar_string) is None
        assert carregar_lista("['A', B]'C'", carregar_string) is None

    def test_carregamento_preguicoso(self):

        assert carregar_lista("['A', 'B']",
            carregar_string, preguicoso=True) == (10, ["'A'", "'B'"])
        assert carregar_lista("['A' 'B']",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("'A', 'B'",
            carregar_string, preguicoso=True) == (0, None)

        assert carregar_lista("['A', 'B']   ",
            carregar_string, preguicoso=True) == (10, ["'A'", "'B'"])
        assert carregar_lista("['A' 'B']   ",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("'A', 'B'   ",
            carregar_string, preguicoso=True) == (0, None)

        assert carregar_lista("['A', 'B']'C'",
            carregar_string, preguicoso=True) == (10, ["'A'", "'B'"])
        assert carregar_lista("['A' 'B']'C'",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("'A', 'B''C'",
            carregar_string, preguicoso=True) == (0, None)

        carregadores = (carregar_string, carregar_palavra)
        assert carregar_lista("[A, 'B']",
            *carregadores, preguicoso=True) == (8, ["A", "'B'"])
        assert carregar_lista("['A', B]",
            *carregadores, preguicoso=True) == (8, ["'A'", "B"])
        assert carregar_lista("['A', 'B']",
            *carregadores, preguicoso=True) == (10, ["'A'", "'B'"])
        assert carregar_lista("[A, B]",
            *carregadores, preguicoso=True) == (6, ["A", "B"])

        assert carregar_lista("[A, 'B']   ",
            *carregadores, preguicoso=True) == (8, ["A", "'B'"])
        assert carregar_lista("['A', B]   ",
            *carregadores, preguicoso=True) == (8, ["'A'", "B"])
        assert carregar_lista("['A', 'B']   ",
            *carregadores, preguicoso=True) == (10, ["'A'", "'B'"])
        assert carregar_lista("[A, B]   ",
            *carregadores, preguicoso=True) == (6, ["A", "B"])

        assert carregar_lista("[A, 'B']'C'",
            *carregadores, preguicoso=True) == (8, ["A", "'B'"])
        assert carregar_lista("['A', B]'C'",
            *carregadores, preguicoso=True) == (8, ["'A'", "B"])
        assert carregar_lista("['A', 'B']'C'",
            *carregadores, preguicoso=True) == (10, ["'A'", "'B'"])
        assert carregar_lista("[A, B]'C'",
            *carregadores, preguicoso=True) == (6, ["A", "B"])

        del carregadores
        assert carregar_lista("[A, B]",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("[A, 'B']",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("['A', B]",
            carregar_string, preguicoso=True) == (0, None)

        assert carregar_lista("[A, B]   ",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("[A, 'B']   ",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("['A', B]   ",
            carregar_string, preguicoso=True) == (0, None)

        assert carregar_lista("[A, B]'C'",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("[A, 'B']'C'",
            carregar_string, preguicoso=True) == (0, None)
        assert carregar_lista("['A', B]'C'",
            carregar_string, preguicoso=True) == (0, None)
