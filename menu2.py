"""Menú de consola de la aplicación."""

import logging
from gestionAppPlantillasFutbol import GestionAppPlantillas

logger = logging.getLogger(__name__)


class Menu2:
    def __init__(self, gestion: GestionAppPlantillas):
        self.gestion = gestion

    def mostrar(self) -> None:
        """Muestra el menú principal y procesa las opciones."""
        while True:
            print("=================================")
            print("\tPLANTILLAS DE FUTBOL\t")
            print("=================================")
            print("1. Agregar miembro")
            print("2. Listar plantilla")
            print("3. Crear plantilla")
            print("4. Salir")

            try:
                opcion = input("Elige una opción: ").strip()
                if opcion == "1":
                    self._agregarMiembro()
                    print("has elegido agregar miembro")
                elif opcion == "2":
                    self._listarPlantilla()
                    print("has elegido listar plantilla")
                elif opcion == "3":
                    print("has elegido crear plantilla")
                elif opcion == "4":
                    logger.info("Aplicación cerrada por el usuario.")
                    print("Hasta luego.")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", opcion)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")

    def _agregarMiembro(self):
        while True:
            print("¿Que tipo de miembro quieres agregar?")
            print("1. Jugador")
            print("2. Cuerpo técnico")
            opcion = input("Selecciona una opcion: ").strip()

            if opcion in ["1", "2"]:
                if opcion == "1":
                    id = input("Elige una id: ").strip()
                    nombre = input("Elige un nombre: ").strip()
                    apellido1 = input("Elige un apellido 1: ").strip()
                    apellido2 = input("Elige un apellido 2: ").strip()
                    apellidos = f"{apellido1} {apellido2}"
                    posicion = input("Elige un posicion [portero, defensa, centrocampista o delantero]: ").strip()
                    miembro = self.gestion.agregarMiembroJuga(id, nombre, apellidos, posicion)
                    print(f"Jugador añadido correctamente: {miembro.nombre}")
                    break
                if opcion == "2":
                    id = input("Elige una id: ").strip()
                    nombre = input("Elige un nombre: ").strip()
                    apellido1 = input("Elige un apellido 1: ").strip()
                    apellido2 = input("Elige un apellido 2: ").strip()
                    apellidos = f"{apellido1} {apellido2}"
                    rol = input("Elige un posicion [entrenador, utillero]: ").strip()
                    miembro = self.gestion.agregarMiembroTecnico(id, nombre, apellidos, rol)
                    print(f"Jugador añadido correctamente: {miembro.nombre}")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de crear jugador o tecnico no válida: %s", opcion)

    def _listarPlantilla(self):
        self.gestion.listarPlantilla()



