import pytest
from solucion.prestamo import Prestamo

class TestPrestamo:
    """Tests unitarios para la clase Prestamo"""

    def test_titulo_vacio_lanza_value_error(self) -> None:
        with pytest.raises(ValueError):
            Prestamo("", "Pablo Aguirre", 4)

    def test_nombre_socio_vacio_lanza_value_error(self) -> None:
        with pytest.raises(ValueError):
            Prestamo("El Principito", "", 4)

    def test_dias_transcurridos_negativo_lanza_value_error(self) -> None:
        with pytest.raises(ValueError):
            Prestamo("El Principito", "Pablo Aguirre", -4)

    def test_prestamo_en_termino(self) -> None:
        prestamo = Prestamo("El Principito", "Pablo Aguirre", 4)
        assert prestamo.esta_vencido() is False

    def test_prestamo_vencido(self) -> None:
        prestamo = Prestamo("El Principito", "Pablo Aguirre", 9)
        assert prestamo.esta_vencido() is True

    def test_prestamo_retraso_cero(self) -> None:
        prestamo = Prestamo("El Principito", "Pablo Aguirre", 4)
        assert prestamo.dias_de_retraso() == 0

    def test_resumen_prestamo_en_termino(self) -> None:
        prestamo = Prestamo("El Principito", "Pablo Aguirre", 4)
        assert prestamo.resumen() == "El Principito — Pablo Aguirre — en término"

    def test_resumen_prestamo_vencido(self) -> None:
        prestamo = Prestamo("El Principito", "Pablo Aguirre", 9)
        assert prestamo.resumen() == "El Principito — Pablo Aguirre — vencido (2 días)"