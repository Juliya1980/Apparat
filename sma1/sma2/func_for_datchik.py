import json
from django.http import HttpResponse
from .models import Sensor, SystemChanges
from datetime import datetime
import logging

logging.basicConfig(filename="sample.log", format='[%(asctime)s] [%(levelname)s] => %(message)s', level=logging.INFO)

data = json.dumps({'dat1': 35.7, 'dat2': 40.5, 'dat3': 41.0})

def vvod_info_datchiki(data=data):
    """
    Функция ввода в таблицу Datchiki.
    На входе - словарь в формате json, у которого все значения "ключ" : "значение" - в формате строк.
    Если поданные данные отсуствуют (len (data)) == 0, то запись в БД не осущствляется,
    если больше - данные заносятся в БД:
    В случае успешного ввода данных -> запись в лог-файл (журнал).
    """
    try:
        if len(data) == 0:
            logging.info("Данные по датчикам не поступили")
        else:
            data = json.loads(data)
            for i in data:
                sys_chang = SystemChanges()
                sys_chang.time_oper = datetime.today()
                if not Sensor.objects.filter(name=i).exists():
                    new_dat = Sensor()
                    new_dat.name = i
                    new_dat.save()
                    logging.info("Добавлен новый датчик %s", i)
                sys_chang.datchik_id = Sensor.objects.filter(name=i).get()
                sys_chang.quantity_datchik = data[i]
                sys_chang.save()
                logging.info("Введены данные по датчику %s - %s градусов", i, data[i])
    except Exception as e:
        logging.error("SystemChanges is not saved %s", e)
        return HttpResponse("Bad Request: SystemChanges is not saved")

