"""Operaciones de gestión de app plantillas."""
import os
from datetime import date
import logging
import random
from typing import Dict, Optional, Type

from models import Miembro, Jugador, CuerpoTecnico

logger = logging.getLogger(__name__)

plantilla = {}

class GestionAppPlantillas:
    """Gestiona personajes y búsquedas usando diccionarios por identificador."""

    def agregarMiembroJuga(self, id, nombre, apellidos, posicion):
        try:
            id = id.strip().lower()
            nombre = nombre.strip().lower()
            apellidos = apellidos.strip().lower()
            posicion = posicion.strip().lower()
            if posicion not in ("portero", "defensa", "centrocampista", "delantero"):
                raise ValueError("posicion no valida escribe : portero, defensa, centrocampista, delantero")
            nuevoMiembro = Jugador(id, nombre, apellidos, posicion)
            plantilla[nuevoMiembro.identificador] = nuevoMiembro
            logger.info("Personaje jugador agregado con exito")
            print("Personaje jugador agregado con exito")


            carpeta = "registroSQL"
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)

            ruta_salida = f"{carpeta}/personaje{nuevoMiembro.identificador}insertado.sql"

            with open(ruta_salida, "w", encoding="utf-8") as f:
                    id = int (nuevoMiembro.identificador)
                    nombre = nuevoMiembro.nombre
                    apellidos = nuevoMiembro.apellidos
                    posicion = nuevoMiembro.posicion

                    f.write(f"INSERT INTO jugador (id, nombre, apellidos, posicion) VALUES ({id}, '{nombre}','{apellidos}','{posicion}')\n")
                    f.flush()

            logging.info("JUGADOR ESCRITO EN SQL")


            return nuevoMiembro
        except Exception:
            logger.exception("Error en agregar miembro jugador.")
            print("Se ha producido un error. Consulta el archivo aplicacion.log.")
            return None

    def agregarMiembroTecnico(self, id, nombre, apellidos, rol):
        try:
            id = id.strip().lower()
            nombre = nombre.strip().lower()
            apellidos = apellidos.strip().lower()
            rol = rol.strip().lower()
            if rol not in ("entrenador ", "utillero"):
                raise ValueError("Rol no valida escribe : entrenador , utillero")
            nuevoMiembro = CuerpoTecnico(id, nombre, apellidos, rol)
            plantilla[nuevoMiembro.identificador] = nuevoMiembro
            logger.info("Personaje cuerpo tecnico agregado con exito")
            print("Personaje cuerpo tecnico agregado con exito")

            carpeta = "registroSQL"
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)

            ruta_salida = f"{carpeta}/personaje{nuevoMiembro.identificador}insertado.sql"

            with open(ruta_salida, "w", encoding="utf-8") as f:
                id = int (nuevoMiembro.identificador)
                nombre = nuevoMiembro.nombre
                apellidos = nuevoMiembro.apellidos
                rol = nuevoMiembro.rol

                f.write(f"INSERT INTO miembro (id, nombre, apellidos, posicion) VALUES ({id},'{nombre}','{apellidos}','{rol}');\n")
                f.flush()

            logging.info("JUGADOR ESCRITO EN SQL")

            return nuevoMiembro
        except Exception:
            logger.exception("Error en agregar miembro cuerpo tecnico.")
            print("Se ha producido un error. Consulta el archivo aplicacion.log.")
            return None
