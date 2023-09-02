from asyncio import create_task, run
from asyncio.tasks import Task, gather
from random import randint
from sqlite3.dbapi2 import Row
from typing import List

from aiosqlite import Connection, connect
from aiosqlite.cursor import Cursor


async def CrearTabla(con: Connection) -> None:
    cur: Cursor = await con.cursor()
    await cur.execute("DROP TABLE IF EXISTS I;")
    await cur.execute("CREATE TABLE I (Num BIGINT);")
    await cur.close()

    print("Creada base limpia")


async def crear_nums(con: Connection, NuevoNum: int) -> None:
    print(f"Cursor de {NuevoNum} a punto de ser creado")
    cur: Cursor = await con.cursor()
    print(f"Creado cursor de {NuevoNum}")

    print(f"A punto de ejecutar cursor {NuevoNum}")
    await cur.execute("INSERT INTO I (Num) VALUES (?)", (NuevoNum,))
    print(f"Insertado {NuevoNum} a la base")

    print(f"Cerrando cursor {NuevoNum}")
    await cur.close()
    print(f"Cursor {NuevoNum} cerrado")


async def ImprimirTabla(con: Connection) -> None:
    cur: Cursor = await con.execute("SELECT * FROM I")

    async for row in cur:
        print(row["Num"])

    await cur.close()


async def main() -> None:
    db: Connection = await connect("base.db")
    db.row_factory = Row

    await CrearTabla(db)
    NumerosNuevos: List[Task] = [create_task(crear_nums(db, randint(1, 100))) for _ in range(50)]
    await gather(*NumerosNuevos)
    await ImprimirTabla(db)

    await db.close()


if __name__ == "__main__":
    from time import time

    start: float = time()
    run(main())
    print(f"Ended in {time() - start} seconds")
