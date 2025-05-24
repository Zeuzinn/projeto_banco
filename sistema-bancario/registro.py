from datetime import datetime

def obter_data_e_hora():
    data_e_hora = datetime.now()
    return data_e_hora.strftime('%H:%M'), data_e_hora.strftime('%d/%m/%Y')







