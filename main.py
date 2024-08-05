# https://docs.python.org/3/library/doctest.html
# https://docs.python.org/3/library/unittest.html
from calculadora import soma

# Testes manuais
# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(-10.5, 20.5))

try:
    print(soma(15, '15'))
except AssertionError as e:
    print(f'Conta Inválida: {e}')

print(soma(10, 25))
