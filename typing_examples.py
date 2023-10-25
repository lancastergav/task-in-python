"""
This modules it's not related to the RLE project. Its only purpose is
just to ilustrate how to use type declarations with Python and mypy.

(c) João Galamba, 2022
$$LICENSE(GPL)
"""

from typing import Callable, Sequence


def fun00(objs: Sequence) -> Sequence:
    return [*objs, 2, 'A']
#:

fun00([1, 2])
fun00(range(10))    # range is a sequence, so that's ok
fun00("AB")         # a string is a Sequence
fun00(1)            # ERROR: Argument 1 to "fun0" has incompatible type "int"
res: list = fun00([10, 20, 30])
                    # ERROR: error: Incompatible types in assignment 
                    # (expression has type "Sequence[Any]"  variable has 
                    # type "List[Any]") ->  Ou seja, a sequência devolvida pela 
                    # função pode não se compatível com uma lista
                    # Tal com em Java, C++, e outras lings. OO, podemos 
                    # fazer um upcasting (cast de algo mais específico para
                    # algo mais genérico) mas não podemos fazer um 
                    # downcasting (cast de genérico para específico)

def fun01(objs: Sequence[int]) -> Sequence:
    return [*objs, 2, 'A']
#:

fun01((1, 2))
fun01("AB")         # ERROR: Argument 1 to "fun01" has incompatible type "str"
fun01(b'AB')        # bytes is a sequence of ints, so this is OK

def fun02(objs: Sequence[int]) -> Sequence[int]:
    return [float(obj) for obj in objs]    # ERROR: List comprehension has 
                                           # incompatible type List[float]
#:

def fun2(a: int, f: Callable[[float], float]) -> bool:
    return a > f(a)
#:

def g(x: float) -> float:
    return 3 / x
#:

def h(x: int) -> float:
    return 3 / x
#:

fun2(2, lambda x: 2 * x)
fun2(2, g)
fun2(2, h)              # ERROR: Argument 2 to "fun1" has incompatible type


def fun3(a: int, f: Callable[..., None], fargs: Sequence) -> Sequence:
    f(*fargs)
    return (a, 2*a)
#:

def p(x: int) -> int:
    return x
#:

def q(x: int):
    print(x)
#:

fun3(2, p, (2,))        # ERROR: Argument 2 to "fun3" has incompatible type 
                        # "Callable[[int], int]"
fun3(2, q, (2,))            # ok, q returns None implicitly (in Python, a 
                            # function without a return or with a bare return,
                            # always returns None)
fun3(2, lambda x: x, (2,))  # ok, lambda's argument types and return values 
                            # are ignored
