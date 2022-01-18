# import context
from common import archivo_2
# import pytest

def test_mi_funcion_resta():
	assert isinstance(archivo_2.mi_funcion_resta(2,3), int)

if __name__ == '__main__':
	test_mi_funcion_resta()