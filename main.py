"""Punto de entrada de la aplicación."""

import logging
from gestion import Gestion
from menu import Menu
from menu2 import Menu2
import os



def configurar_logging() -> None:
    # Crear la carpeta logs si no existe
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(
                "logs/villanoYHeroe.log",
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ]
    )


def main() -> None:
    configurar_logging()
    logger = logging.getLogger(__name__)
    logger.info("Inicio de la aplicación.")

    try:
        while True:
            print("Eligue entre dos aplicaciones")
            print("(1) Heroes y villanos")
            print("(2) Plantillas de Fútbol")
            print("(0) Salir")
            opciones = input("Eligue la aplicacion: ").strip()

            if opciones in ["1", "2", "3"]:
                if opciones == "1":
                    gestion = Gestion()
                    menu = Menu(gestion)
                    menu.mostrar()
                elif opciones == "2":
                    gestion2 = Gestion()
                    menu2 = Menu2(gestion2)
                    menu2.mostrar()
                elif opciones == "0":
                    logger.info("Aplicación En inicio por el usuario.")
                    print("Hasta luego de inicio.")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de elegir menu no válida: %s", opciones)


    except Exception:
        logger.exception("Error fatal en la aplicación.")
        print("La aplicación ha finalizado por un error. Consulta aplicacion.log.")
    finally:
        logger.info("Fin de la aplicación.")


if __name__ == "__main__":
    main()
