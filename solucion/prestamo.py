class Prestamo:
    def __init__(self, titulo, nombre_socio, dias_transcurridos):
        if not titulo.strip():
            raise ValueError("El titulo no puede estar vacio")
        if not nombre_socio.strip():
            raise ValueError("El nombre del socio no puede estar vacio")
        if dias_transcurridos < 0:
            raise ValueError(f"Los dias transcurridos no pueden ser negativos: {dias_transcurridos}")
        
        self.titulo = titulo
        self.nombre_socio = nombre_socio
        self.dias_transcurridos = dias_transcurridos

    def esta_vencido(self):
        return self.dias_transcurridos > 7

    def dias_de_retraso(self):
        if self.esta_vencido() is False:
            return 0
        else:
            return self.dias_transcurridos - 7

    def resumen(self):
        pass