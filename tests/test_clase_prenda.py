import pytest

from src.domain.prenda import Prenda


def test_prenda_com_categoria_errada():
    with pytest.raises(ValueError):
        prenda1 = Prenda(nome='test', material='material', cor='cor', formalidade='formal', categoria='categoria_errada', path='images/nome.jpg')


def test_prenda_com_formalidade_errada():
    with pytest.raises(ValueError):
        prenda1 = Prenda(nome='test', material='material', cor='cor', formalidade='forma', categoria='calças', path='images/nome.jpg')