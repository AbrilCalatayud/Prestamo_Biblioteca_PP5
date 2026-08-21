class Prestamo:
    """Representa el préstamo de un libro. 
    Guarda el título del libro, el socio que lo tomó prestado y los días transcurridos.
    Devuelve si está vencido o no, los días de retraso (si los hay) y un resumen con la información."""

    def __init__(self, titulo: str, nombre_socio: str, dias_transcurridos: int) -> None:
        if not titulo.strip():
            raise ValueError("El titulo no puede estar vacio")
        if not nombre_socio.strip():
            raise ValueError("El nombre del socio no puede estar vacio")
        if dias_transcurridos < 0:
            raise ValueError(f"Los dias transcurridos no pueden ser negativos: {dias_transcurridos}")
        
        self.titulo = titulo
        self.nombre_socio = nombre_socio
        self.dias_transcurridos = dias_transcurridos

    def esta_vencido(self) -> bool:
        """Devuelve si el préstamo está vencido o no."""
        return self.dias_transcurridos > 7

    def dias_de_retraso(self) -> int:
        """Devuelve los días de retraso. Si no está vencido, devuelve 0."""
        if not self.esta_vencido():
            return 0
        
        return self.dias_transcurridos - 7

    def resumen(self) -> str:
        """Devuelve un resumen con la información importante del prestamo."""
        if not self.esta_vencido():
            return f"{self.titulo} — {self.nombre_socio} — en término"
        
        return f"{self.titulo} — {self.nombre_socio} — vencido ({self.dias_de_retraso()} días)"