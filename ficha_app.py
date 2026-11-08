"""Ficha técnica de una aplicación móvil antes de publicarla en la tienda."""

from typing import Final

# Añadid aquí las importaciones que necesitéis.

# ---------------------------------------------------------------------------
# Datos de la aplicación. Sustituid los del ejemplo APP-00 por los vuestros.
# ---------------------------------------------------------------------------
CODIGO: Final[str] = "APP-08"
NOMBRE: Final[str] = "Turnos de Farmacia"
PAQUETE: Final[str] = "es.salud.turnosfarmacia"
VERSION_MAYOR, VERSION_MENOR, VERSION_PARCHE = 3, 3, 1
TAMANO_APK: Final[int] = 15_728_640         # bytes
DESCARGAS: Final[int] = 12_000
PRECIO: Final[float] = 0.99                  # euros, IVA incluido
VALORACIONES: Final[int] = 500
ESTRELLAS: Final[int] = 2_125               # suma de todas las valoraciones
PERMISOS: Final[int] = 0b0001011
COLOR_ICONO: Final[int] = 0xFFC62828         # ARGB

# ---------------------------------------------------------------------------
# Datos del programa. Solo hay que cambiar AUTORES.
# ---------------------------------------------------------------------------
VERSION_PROGRAMA: Final[str] = "1.0.0"
AUTORES: Final[str] = "[usuario] · [usuario]"
PENDIENTE: Final[str] = "  (opción pendiente de implementar)"

# ---------------------------------------------------------------------------
# Constantes de la pareja. Todo valor fijo del programa va aquí, con nombre.
# ---------------------------------------------------------------------------
ANCHO: Final[int] = 44


# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------
def opcion_1_identificacion() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_2_tamano() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_3_ingresos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_4_version() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_5_permisos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_6_color() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_7_tipos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_8_redondeo() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_9_ficha() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_10_acerca_de() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


# ---------------------------------------------------------------------------
# Función principal y punto de entrada. Vienen hechos: no los modifiquéis.
# ---------------------------------------------------------------------------
def main() -> None:
    """Ejecuta las diez opciones, una detrás de otra."""
    print("--- Opción 1. Identificación de la app ---")
    opcion_1_identificacion()
    print("\n--- Opción 2. Tamaño del APK ---")
    opcion_2_tamano()
    print("\n--- Opción 3. Ingresos ---")
    opcion_3_ingresos()
    print("\n--- Opción 4. versionCode ---")
    opcion_4_version()
    print("\n--- Opción 5. Permisos ---")
    opcion_5_permisos()
    print("\n--- Opción 6. Color del icono ---")
    opcion_6_color()
    print("\n--- Opción 7. Tipos de datos ---")
    opcion_7_tipos()
    print("\n--- Opción 8. Redondeo de la valoración ---")
    opcion_8_redondeo()
    print("\n--- Opción 9. Ficha completa ---")
    opcion_9_ficha()
    print("\n--- Opción 10. Acerca de ---")
    opcion_10_acerca_de()


if __name__ == "__main__":
    main()
