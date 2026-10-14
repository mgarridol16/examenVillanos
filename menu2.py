"""Menú de consola de la aplicación."""

import logging
from gestion import Gestion

logger = logging.getLogger(__name__)


class Menu2:
    def __init__(self, gestion: Gestion):
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
                    print("has elegido agregar miembro")
                elif opcion == "2":
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


