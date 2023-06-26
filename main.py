#API para separar citas de entrenamiento con Luffy, Zoro, Sanji.

from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.post("/agendar")
async def agendarCita(entrenador: str, informacion: dict):
    conexion = sqlite3.connect("OnePiece-API\\onePiece.db")
    cursor = conexion.cursor()
    cursor.execute(f"insert into {entrenador} (nombre, apellido, edad, dia, hora) values (?, ?, ?, ?, ?)", (informacion["nombre"], informacion["apellido"], informacion["edad"], informacion["dia"], informacion["hora"]))
    conexion.commit()
    conexion.close()
    return f"entrenamiento agendado con exito"


@app.get("/informacion/{nombre}/{entrenador}")
async def miCita(nombre: str, entrenador: str):
    conexion = sqlite3.connect("OnePiece-API\\onePiece.db")
    cursor = conexion.cursor()
    cursor.execute(f"select * from {entrenador} where nombre = '{nombre}'")
    info = cursor.fetchone()
    conexion.close()
    return f"la informacion de su entrenamiento: {info}, su numero de id es: {info[0]}"


@app.put("/cambiar")
async def cambiarInfo(nombre: str, entrenador: str, informacion: dict):
    conexion = sqlite3.connect("OnePiece-API\\onePiece.db")
    cursor = conexion.cursor()
    cursor.execute(f"update {entrenador} set nombre=?, apellido=?, edad=?, dia=?, hora=? where nombre = ?", (informacion["nombre"], informacion["apellido"], informacion["edad"], informacion["dia"], informacion["hora"], nombre))
    conexion.commit()
    conexion.close()
    return f"la informacion del entrenamiento ha sido actualizada"


@app.delete("/eliminar")
async def eliminarCita(id: int, entrenador: str):
    conexion = sqlite3.connect("OnePiece-API\\onePiece.db")
    cursor = conexion.cursor()
    cursor.execute(f"delete from {entrenador} where id = '{id}'")
    conexion.commit()
    conexion.close()
    return "entrenamiento cancelado con exito"
