import pytest 0
from ejerciciopruebas import sumar, restar, multiplicar, dividir

@pytest.mark.parametrize("a,b,resultado",[
    (2,3,5)
    (10,5,15)
    (8,1,10)
]
)
def test_sumar_ok(a,b,resultado):
    assert sumar(a,b)== resultado
    
@pytest.mark.parametrize("a,b,resultado",[
    (2,3,-1)
    (10,5,5 )
    (-1,1,-2)
]
)
def test_restar_ok(a,b,resultado):
    assert restar(a,b)== resultado
    
@pytest.mark.parametrize("a,b,resultado",[
  (2,3,6)
  (10,5,50)
  (-2,-4,8)
]
)
def test_multiplicar_ok(a,b,resultado):
    assert multiplicar(a,b)== resultado  

@pytest.mark.parametrize("a,b,resultado",[
  (6,3,2)
  (10,5,2)
  (-24,-4,6)
]
)
def test_dividir_ok(a,b,resultado):
    assert dividir(a,b)== resultado  

def test_dividir_error(a,b):
    with pytest.raises(ValueError, match="validado error división por cero"):
     dividir(5,0)   