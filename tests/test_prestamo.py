import pytest
from solucion.prestamo import Prestamo

class TestPrestamo:
    def test_titulo_vacio_lanza_value_error(self):
        with pytest.raises(ValueError):
            Prestamo("", "Pablo Aguirre", 4)

    def test_nombre_socio_vacio_lanza_value_error(self):
        with pytest.raises(ValueError):
            Prestamo("El Principito", "", 4)

    def test_dias_transcurridos_negativo_lanza_value_error(self):
        with pytest.raises(ValueError):
            Prestamo("El Principito", "Pablo Aguirre", -4)

    def test_prestamo_en_termino(self):
        pass

    def test_prestamo_vencido(self):
        pass

    def test_prestamo_retraso_cero(self):
        pass