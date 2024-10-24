import re 

class Horario:
    """
    Clase que representa un horario con un día y una franja horaria.
    Valida que el día esté en una lista de días válidos y que las horas estén en formato HH:MM.
    """
    
    DIAS_VALIDOS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    HORA_REGEX = r"^(?:[01]\d|2[0-3]):[0-5]\d$"  # Formato HH:MM (00:00 a 23:59)
    
    def __init__(self, dia, hora_inicio, hora_fin):
        """
        Inicializa el objeto Horario.
        :param dia: Día de la semana en que se realiza la actividad.
        :param hora_inicio: Hora de inicio en formato HH:MM.
        :param hora_fin: Hora de fin en formato HH:MM.
        """
        if dia not in self.DIAS_VALIDOS:
            raise ValueError(f"El día '{dia}' no es válido. Debe ser uno de {self.DIAS_VALIDOS}.")
        if not re.match(self.HORA_REGEX, hora_inicio):
            raise ValueError(f"La hora de inicio '{hora_inicio}' no tiene el formato correcto (HH:MM).")
        if not re.match(self.HORA_REGEX, hora_fin):
            raise ValueError(f"La hora de fin '{hora_fin}' no tiene el formato correcto (HH:MM).")
        
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    
    def __str__(self):
        """
        Representación en cadena del objeto Horario.
        :return: Una cadena con el formato "Día: hora_inicio - hora_fin".
        """
        return f"{self.dia}: {self.hora_inicio} - {self.hora_fin}"
    
    def convertir_a_minutos(self, hora):
        """
        Convierte una hora en formato HH:MM a minutos desde las 00:00.
        :param hora: Hora en formato HH:MM.
        :return: El número de minutos desde las 00:00.
        """
        horas, minutos = map(int, hora.split(":"))
        return horas*60 + minutos
    
    def horas_solapadas(self, otra_hora):
        """
        Verifica si dos horarios se solapan.
        :param otra_hora: Un objeto Horario con el que se comparará el solapamiento.
        :return: True si los horarios se solapan, False en caso contrario.
        """
        if self.dia != otra_hora.dia:
            return False
        
        inicio_1_minutos = self.convertir_a_minutos(self.hora_inicio)
        fin_1_minutos = self.convertir_a_minutos(self.hora_fin)
        inicio_2_minutos = self.convertir_a_minutos(otra_hora.hora_inicio)
        fin_2_minutos = self.convertir_a_minutos(otra_hora.hora_fin)
        
        return not (fin_1_minutos <= inicio_2_minutos or fin_2_minutos <= inicio_1_minutos)