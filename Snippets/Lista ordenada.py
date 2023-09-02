from __future__ import annotations
from typing import List
from dataclasses import dataclass, field


def estaOrdenada(ls_objetos: List[int], diferencia: int = 1) -> bool:
    lon_lista: int = len(ls_objetos)

    if lon_lista in [0, 1]:
        raise Exception("Introduce una lista con dos o mas objetos")

    for index_actual in range(0, lon_lista - 1):
        val_actual: int = ls_objetos[index_actual]
        siguiente_val : int = ls_objetos[index_actual + 1]
        dif_valores: int = siguiente_val - val_actual

        if dif_valores != diferencia:
            return False

    return True


@dataclass(frozen=True)
class Prueba:
    _num_instancias: int = field(default=0, repr=False, init=False)
    val: int = field(default=0)

    def __post_init__(self):
        Prueba._num_instancias += 1

    @staticmethod
    def instancias_creadas() -> int:
        return Prueba._num_instancias


if __name__ == "__main__":
    ListaPruebas: List[Prueba] = [Prueba(val=num) for num in range(0, 10 + 1) if num%2 == 0]
    ListaValsPrueba: List[int] = [Prueba.val for Prueba in ListaPruebas]

    pruebas_ordenadas: bool = estaOrdenada(ListaValsPrueba, 2)

    print(f"La lista esta {'ordenda' if pruebas_ordenadas else 'de la verga'}")
    print(f"Se han creado {Prueba.instancias_creadas()} instancias de la clase Prueba")
