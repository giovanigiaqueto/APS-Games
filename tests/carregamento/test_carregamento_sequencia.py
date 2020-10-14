
from src.carregamento.carregadores.sequencias import *
from src.carregamento.carregadores.base import carregar_string, carregar_palavra
from src.carregamento.delimitadores import delim_espaco, delim_virgula

import pytest

class TestCarregarPar:

    class TestCarregamentoNormal:

        def test_carregamento_simples(self):

            assert carregar_par("A B", delim_espaco, carregar_palavra) == ("A", "B")
            assert carregar_par("A.B", delim_espaco, carregar_palavra) is None
            assert carregar_par("A", delim_espaco, carregar_palavra) is None
            assert carregar_par(" A", delim_espaco, carregar_palavra) == (None, "A")

            assert carregar_par("A B   ", delim_espaco, carregar_palavra) == ("A", "B")
            assert carregar_par("A.B   ", delim_espaco, carregar_palavra) is None
            assert carregar_par("A   ", delim_espaco, carregar_palavra) == ("A", None)
            assert carregar_par("A   ", delim_virgula, carregar_palavra) is None
            assert carregar_par(" A   ", delim_espaco, carregar_palavra) == (None, "A")

            assert carregar_par("A B'C'", delim_espaco, carregar_palavra) is None
            assert carregar_par("A.B'C'", delim_espaco, carregar_palavra) is None
            assert carregar_par("A'C'", delim_espaco, carregar_palavra) is None
            assert carregar_par(" A'C'", delim_espaco, carregar_palavra) is None

        def test_carregamento_preguicoso(self):

            assert carregar_par("A B", delim_espaco,
                carregar_palavra, preguicoso=True) == (3, "A", "B")
            assert carregar_par("A.B", delim_espaco,
                carregar_palavra, preguicoso=True) == (1, "A", None)
            assert carregar_par("A", delim_espaco,
                carregar_palavra, preguicoso=True) == (1, "A", None)
            assert carregar_par(" A", delim_espaco,
                carregar_palavra, preguicoso=True) == (2, None, "A")

            assert carregar_par("A B   ", delim_espaco,
                carregar_palavra, preguicoso=True) == (3, "A", "B")
            assert carregar_par("A.B   ", delim_espaco,
                carregar_palavra, preguicoso=True) == (1, "A", None)
            assert carregar_par("A   ", delim_espaco,
                carregar_palavra, preguicoso=True) == (1, "A", None)
            assert carregar_par(" A   ", delim_espaco,
                carregar_palavra, preguicoso=True) == (2, None, "A")

            assert carregar_par("A B'C'", delim_espaco,
                carregar_palavra, preguicoso=True) == (3, "A", "B")
            assert carregar_par("A.B'C'", delim_espaco,
                carregar_palavra, preguicoso=True) == (1, "A", None)
            assert carregar_par("A'C'", delim_espaco,
                carregar_palavra, preguicoso=True) == (1, "A", None)
            assert carregar_par(" A'C'", delim_espaco,
                carregar_palavra, preguicoso=True) == (2, None, "A")

    class TestCarregamentoEstrito:

        def test_carregamento_simples(self):

            assert carregar_par("A B", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) == ("A", "B")
            assert carregar_par("A.B", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("A", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par(" A", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) == (None, "A")

            assert carregar_par("A 'B'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("A.'B'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("'A'.B", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("'A'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par(" 'A'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None

            assert carregar_par("A 'B'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) == ("A", "'B'")
            assert carregar_par("A.'B'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par("'A'.B", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par("'A'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par("A ", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) == ("A", None)
            assert carregar_par(" 'A'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) == (None, "'A'")


            assert carregar_par("A B   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) == ("A", "B")
            assert carregar_par("A.B   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("A   ", delim_virgula,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par(" A   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) == (None, "A")

            assert carregar_par("A 'B'   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("A.'B'   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("'A'.B   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("'A'   ", delim_virgula,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par(" 'A'   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None

            assert carregar_par("A 'B'   ", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) == ("A", "'B'")
            assert carregar_par("A.'B'   ", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par("'A'.B   ", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par("'A'   ", delim_virgula,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par(" 'A'   ", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) == (None, "'A'")


            assert carregar_par("A B'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("A.B'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("A'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par(" A'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None

            assert carregar_par("A 'B''C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("A.'B''C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("'A'.B'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par("'A''C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None
            assert carregar_par(" 'A''C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,), estrito=True) is None

            assert carregar_par("A 'B''C'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par("A.'B''C'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par("'A'.B'C'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par("'A''C'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None
            assert carregar_par(" 'A''C'", delim_espaco,
                (carregar_palavra,), (carregar_string,), estrito=True) is None

        def test_carregamento_preguicoso(self):

            assert carregar_par("A B", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (3, "A", "B")
            assert carregar_par("A.B", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("A", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par(" A", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (2, None, "A")

            assert carregar_par("A 'B'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("A.'B'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("'A'.B", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par("'A'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par(" 'A'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)

            assert carregar_par("A 'B'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (5, "A", "'B'")
            assert carregar_par("A.'B'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("'A'.B", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par("'A'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par("A ", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par(" 'A'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (4, None, "'A'")


            assert carregar_par("A B   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (3, "A", "B")
            assert carregar_par("A.B   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("A   ", delim_virgula,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par(" A   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (2, None, "A")

            assert carregar_par("A 'B'   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("A.'B'   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("'A'.B   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par("'A'   ", delim_virgula,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par(" 'A'   ", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)

            assert carregar_par("A 'B'   ", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (5, "A", "'B'")
            assert carregar_par("A.'B'   ", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("'A'.B   ", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par("'A'   ", delim_virgula,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par(" 'A'   ", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (4, None, "'A'")


            assert carregar_par("A B'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (3, "A", "B")
            assert carregar_par("A.B'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("A'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par(" A'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (2, None, "A")

            assert carregar_par("A 'B''C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("A.'B''C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("'A'.B'C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par("'A''C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par(" 'A''C'", delim_espaco,
                (carregar_palavra,), (carregar_palavra,),
                preguicoso=True, estrito=True) == (0, None, None)

            assert carregar_par("A 'B''C'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (5, "A", "'B'")
            assert carregar_par("A.'B''C'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (1, "A", None)
            assert carregar_par("'A'.B'C'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par("'A''C'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (0, None, None)
            assert carregar_par(" 'A''C'", delim_espaco,
                (carregar_palavra,), (carregar_string,),
                preguicoso=True, estrito=True) == (4, None, "'A'")
