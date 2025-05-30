from datetime import datetime, date, time

class Horario:
    def __init__(self, data: date | None = None, hora: time | None = None):
        agora = datetime.now()
        self._data = data if data else agora.date()
        self._hora = hora if hora else agora.time()

    def obter_horario(self):
        return self._hora.strftime('%H:%M'), self._data.strftime('%d/%m/%Y')