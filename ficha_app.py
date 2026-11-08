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
AUTORES: Final[str] = "Alejandro Nuñez · Sebastian"
PENDIENTE: Final[str] = "  (opción pendiente de implementar)"

# ---------------------------------------------------------------------------
# Constantes de la pareja. Todo valor fijo del programa va aquí, con nombre.
# ---------------------------------------------------------------------------
ANCHO: Final[int] = 44
CARACTER_DOBLE: Final[str] = "="
CARACTER_SIMPLE: Final[str] = "-"
COMISION_TIENDA: Final[float] = 0.15         # 15 % de cada venta
BYTES_MB: Final[int] = 10 ** 6               # 1 MB de la tienda, en bytes
BYTES_MIB: Final[int] = 2 ** 20
PORCENTAJE: Final[int] = 100                 # para expresar en %
UN_DECIMAL: Final[Decimal] = Decimal("0.1")  # cuantificador para 1 decimal
DOS_DECIMALES: Final[Decimal] = Decimal("0.01")  # 2 decimales
DIGITOS_BINARIO: Final[int] = 7              # un permiso por cifra binaria
DESPLAZAMIENTO_MENOR: Final[int] = 8         # bits que ocupa el parche
DESPLAZAMIENTO_MAYOR: Final[int] = 16        # bits que ocupan parche y menor
MASCARA_BYTE: Final[int] = 0xFF              # los ocho bits de abajo
DESPLAZAMIENTO_ROJO: Final[int] = 16
DESPLAZAMIENTO_VERDE: Final[int] = 8
DESPLAZAMIENTO_ALFA: Final[int] = 24
DIGITOS_BINARIO_CANAL: Final[int] = 8        # un canal de color ocupa 8 bits
DIGITOS_HEX_CODIGO: Final[int] = 6           # cifras hex de un versionCode
DIGITOS_HEX_CANAL: Final[int] = 2            # cifras hex de un canal

PERMISO_INTERNET: Final[int] = 0b0000001
PERMISO_NOTIFICACIONES: Final[int] = 0b0000010
PERMISO_CAMARA: Final[int] = 0b0000100
PERMISO_UBICACION: Final[int] = 0b0001000
PERMISO_CONTACTOS: Final[int] = 0b0010000
PERMISO_MICROFONO: Final[int] = 0b0100000
PERMISO_ALMACENAMIENTO: Final[int] = 0b1000000


# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------


def linea_separadora(caracter: str) -> str:
    """Devuelve una línea formada por el carácter repetido ANCHO veces."""
    return caracter * ANCHO


def cabecera_centrada(texto: str) -> str:
    """Devuelve el texto centrado en un ancho de ANCHO caracteres."""
    return texto.center(ANCHO)


# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------


def opcion_1_identificacion() -> None:
    """Muestra código, nombre, paquete y versión de la app."""
    version_texto: str = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    print(f"Código: {CODIGO}")
    print(f"Nombre: {NOMBRE}")
    print(f"Paquete: {PAQUETE}")
    print(f"Versión: {version_texto}")


def opcion_2_tamano() -> None:
    """Muestra el tamaño del APK en bytes, MB, MiB y la diferencia."""
    tamano_mb: float = TAMANO_APK / BYTES_MB
    tamano_mib: float = TAMANO_APK / BYTES_MIB
    diferencia_pct: float = (tamano_mb - tamano_mib) / tamano_mb * PORCENTAJE
    print(f"Bytes: {TAMANO_APK} B")
    print(f"En la tienda: {tamano_mb:.2f} MB")
    print(f"En el móvil: {tamano_mib:.2f} MiB")
    print(f"Diferencia: {diferencia_pct:.1f} %")


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
