from typing import Literal

import pytest

from verificanum import multiplos_ambos, multiplos_vazio, multiplos5, multiplos7

# Parametrização dos testes
@pytest.mark.parametrize("a, expected", [
    (35, 'fizzbuzz'),
    (10, 'Número digitado não é múltiplo de 5 e nem de 7!'),
    (14, 'Número digitado não é múltiplo de 5 e nem de 7!'),
])
def test_multiplos_ambos(a, expected):
    assert multiplos_ambos(a) == expected

@pytest.mark.parametrize("a, expected", [
    (10, 'fizz'),
    (3, 'Número digitado não é múltiplo de 5!'),
    (25, 'fizz'),
])
def test_multiplos5(a, expected):
    assert multiplos5(a) == expected

@pytest.mark.parametrize("a, expected", [
    (14, 'buzz'),
    (9, 'Número digitado não é múltiplo de 7!'),
    (49, 'buzz'),
])
def test_multiplos7(a, expected):
    assert multiplos7(a) == expected

@pytest.mark.parametrize("a, expected", [
    (2, 'miss'),
    (11, 'miss'),
    (35, None),
])
def test_multiplos_vazio(a, expected):
    assert multiplos_vazio(a) == expected

