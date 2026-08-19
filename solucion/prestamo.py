class Prestamo:
    def __init__(self, titulo, nombre_socio, dias_transcurridos):
        if not titulo.strip():
            raise ValueError("El titulo no puede estar vacio")
        if not nombre_socio.strip():
            raise ValueError("El nombre del socio no puede estar vacio")
        if dias_transcurridos < 0:
            raise ValueError(f"Los dias transcurriods no pueden ser negativos: {dias_transcurridos}")
        
        self.titulo = titulo
        self.nombre_socio = nombre_socio
        self.dias_transcurridos = dias_transcurridos

    def esta_vencido(self):
        pass

    def dias_de_retraso(self):
        pass

    def resumen(self):
        pass