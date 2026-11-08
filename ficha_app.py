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
    """Muestra descargas, precio, ingresos brutos, comisión y netos."""
    ingresos_brutos: float = DESCARGAS * PRECIO
    comision: float = ingresos_brutos * COMISION_TIENDA
    ingresos_netos: float = ingresos_brutos - comision
    print(f"Descargas: {DESCARGAS} uds.")
    print(f"Precio: {PRECIO:.2f} €")
    print(f"Ingresos brutos: {ingresos_brutos:.2f} €")
    print(f"Comisión tienda: {comision:.2f} €")
    print(f"Ingresos netos: {ingresos_netos:.2f} €")


def opcion_4_version() -> None:
    """Empaqueta la versión en un versionCode y la desempaqueta."""
    version_code: int = (
        (VERSION_MAYOR << DESPLAZAMIENTO_MAYOR)
        | (VERSION_MENOR << DESPLAZAMIENTO_MENOR)
        | VERSION_PARCHE
    )
    version_hex: str = f"0x{version_code:0{DIGITOS_HEX_CODIGO}X}"
    mayor: int = (version_code >> DESPLAZAMIENTO_MAYOR) & MASCARA_BYTE
    menor: int = (version_code >> DESPLAZAMIENTO_MENOR) & MASCARA_BYTE
    parche: int = version_code & MASCARA_BYTE
    version_texto: str = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    desempaquetado_texto: str = f"{mayor}.{menor}.{parche}"
    print(f"Versión: {version_texto}")
    print(f"versionCode: {version_code}")
    print(f"En hexadecimal: {version_hex}")
    print(f"Desempaquetado: {desempaquetado_texto}")


def opcion_5_permisos() -> None:
    """Muestra los permisos de la app en binario y uno a uno."""
    permisos_binario: str = format(PERMISOS, f"0{DIGITOS_BINARIO}b")
    sin_ubicacion: int = PERMISOS & ~PERMISO_UBICACION
    sin_ubicacion_binario: str = format(sin_ubicacion, f"0{DIGITOS_BINARIO}b")
    print(f"En binario: {permisos_binario}")
    print(f"Internet: {(PERMISOS & PERMISO_INTERNET) != 0}")
    print(f"Notificaciones: {(PERMISOS & PERMISO_NOTIFICACIONES) != 0}")
    print(f"Cámara: {(PERMISOS & PERMISO_CAMARA) != 0}")
    print(f"Ubicación: {(PERMISOS & PERMISO_UBICACION) != 0}")
    print(f"Contactos: {(PERMISOS & PERMISO_CONTACTOS) != 0}")
    print(f"Micrófono: {(PERMISOS & PERMISO_MICROFONO) != 0}")
    print(f"Almacenamiento: {(PERMISOS & PERMISO_ALMACENAMIENTO) != 0}")
    print(f"Sin ubicación: {sin_ubicacion_binario}")


def opcion_6_color() -> None:
    """Muestra el color ARGB del icono en canales y en formato CSS."""
    alfa: int = (COLOR_ICONO >> DESPLAZAMIENTO_ALFA) & MASCARA_BYTE
    opacidad_pct: float = alfa / MASCARA_BYTE * PORCENTAJE
    rojo: int = (COLOR_ICONO >> DESPLAZAMIENTO_ROJO) & MASCARA_BYTE
    verde: int = (COLOR_ICONO >> DESPLAZAMIENTO_VERDE) & MASCARA_BYTE
    azul: int = COLOR_ICONO & MASCARA_BYTE
    hex_rojo: str = f"{rojo:0{DIGITOS_HEX_CANAL}X}"
    hex_verde: str = f"{verde:0{DIGITOS_HEX_CANAL}X}"
    hex_azul: str = f"{azul:0{DIGITOS_HEX_CANAL}X}"
    bin_rojo: str = f"{rojo:0{DIGITOS_BINARIO_CANAL}b}"
    bin_verde: str = f"{verde:0{DIGITOS_BINARIO_CANAL}b}"
    bin_azul: str = f"{azul:0{DIGITOS_BINARIO_CANAL}b}"
    css_color: str = f"#{hex_rojo}{hex_verde}{hex_azul}"
    print(f"ARGB: 0x{COLOR_ICONO:08X}")
    print(f"Rojo: {rojo} {bin_rojo} {hex_rojo}")
    print(f"Verde: {verde} {bin_verde} {hex_verde}")
    print(f"Azul: {azul} {bin_azul} {hex_azul}")
    print(f"Opacidad: {opacidad_pct:.1f} %")
    print(f"Para CSS: {css_color}")


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
