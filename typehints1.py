# https://docs.python.org/3/library/typing.html#the-any-type
# https://docs.python.org/3/library/typing.html

from typing import List, Union, Tuple, Dict, Any, NewType, Callable, \
    Sequence, Iterable

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Gabriel Galacci'

# Sequências
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Gabriel']
tupla_especificada: Tuple[int, int, int, str] = (1, 2, 3, 'Gabriel')
tupla_nao_especificada: Tuple = (1, 2, 3, 'Gabriel')

# Dicionários e conjuntos
# Meu tipo
meudict = Dict[str, Union[str, int, List[int]]]  # Alias

pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Gabriel',
    'sobrenome': 'Galacci',
    'idade': 30
}

pessoa2: Dict[str, Any] = {
    'nome': 'Gabriel',
    'sobrenome': 'Galacci',
    'idade': 30
}

pessoa3: meudict = {
    'nome': 'Gabriel',
    'sobrenome': 'Galacci',
    'idade': 30,
    'lista': [1, 2, 3, 4, 5]
}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(123456789)


# Funções
def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def retorna_funcao2(funcao: Callable[[], None]) -> Callable:
    return funcao


def fala_oi():
    print('Oi!')


def soma(x: int, y: int) -> int:
    return x + y


retorna_funcao2(fala_oi)()
retorna_funcao(soma)(10, 20)


# Classes
class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


# Iteradores
def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))
