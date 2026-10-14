"""Operaciones de gestión de app plantillas."""

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
            return nuevoMiembro
        except Exception:
            logger.exception("Error en agregar miembro cuerpo tecnico.")
            print("Se ha producido un error. Consulta el archivo aplicacion.log.")
            return None
