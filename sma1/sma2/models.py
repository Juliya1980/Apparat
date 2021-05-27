from django.db import models

# Create your models here.

class Zone(models.Model):
    # ID добавляется автомтически средствами джанго.
    # https://docs.djangoproject.com/en/dev/topics/db/models/#automatic-primary-key-fields
    # Не понятно зачем это поле здесь, теперь так принято?
    id = models.AutoField(primary_key=True)  # ИД зоны
    name = models.TextField(null=True)  # Имя зоны


# Все таки принято писать на английском. Вдруг придется выходить на междунароный рынок?
# Назовем это Sensor
class Datchiki(models.Model):
    id = models.AutoField(primary_key=True)  # ИД датчика
    name = models.TextField(null=True)  # Наименование датчика
    zone_id = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)  # Зона нахождения
    status = models.BooleanField(null=True)  # Статус датчика: True - в сети, False - не в сети
    # Вот тут, похоже, кроется главное недопонимание.
    # Датчик не может быть в сети или не в сети. Точнее, такая информация без привязки ко
    # времени смысла не имеет. Время у нас есть только в SystemChanges, но по смыслу модели
    # получается, что если запись SystemChanges от датчика N, со временем T, то он как бы уже в сети.
    # Видимо, ты подразумеваешь, что система сама опрашивает датчики и делает выводы о его активности.
    # Чуть позже я напишу почему это не удобно в нашем случае.


# Эта модель для чего?
# Логично было бы, чтобы прибор логически объединял несколько датчиков,
# а пока получается, что у нас приборы и датчики объединяет некая "Зона".
# Таким образом датчик и прибор у нас равноправные и одинаковые сущности с разными названиями
class Pribori(models.Model):
    id = models.AutoField(primary_key=True)  # ИД прибора
    name = models.TextField(null=True)  # Наименование прибора
    zone_id = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)  # Зона нахождения
    status = models.BooleanField(null=True)  # Статус прибора: True - в сети, False - не в сети


# Это для хранения режима приготовления?
# Терминологический вопрос: нормативное значение датчика это некое целевое значение?
# Вообще именно тут все сложно. Приготовление это скорее последовательность нескольких режимов.
# Но тут я пока не готов осознать как это должно выглядеть.
class Rezim(models.Model):
    id = models.AutoField(primary_key=True)  # ИД режима
    name = models.TextField(null=True)  # Наименование режима
    len_rezim = models.FloatField(null=True)  # Длительность режима
    datchik_id = models.ForeignKey(Datchiki, on_delete=models.SET_NULL, null=True)  # ИД датчика
    normativ_datchik = models.FloatField(null=True)  # Нормативное значение датчика
    pribor_id = models.ForeignKey(Pribori, on_delete=models.SET_NULL, null=True)  # ИД прибора
    normativ_pribor = models.FloatField(null=True)  # Нормативное значение прибора


# Тут отлично! :)
class Product(models.Model):
    id = models.AutoField(primary_key=True)  # ИД продукта
    name = models.TextField(null=True)  # Наименование продукта
    time_oper = models.DateTimeField(null=True)  # Дата и время окончания приготовления продукта
    value = models.FloatField(null=True)  # Количество продукта
    ediz = models.TextField(null=True)  # Единицы измерения
    prim = models.TextField(null=True)  # Примечание / вкусовые характеристики
    rezim_id = models.ForeignKey(Rezim, on_delete=models.SET_NULL, null=True)  # Использованный режим


# Тут по существу ничего не сказать, т.к. все, что выше развалилось. :)
class SystemChanges(models.Model):
    id = models.AutoField(primary_key=True)  # ИД операции мониторинга системы
    time_oper = models.DateTimeField(null=True)  # Время совершения операции
    datchik_id = models.ForeignKey(Datchiki, on_delete=models.SET_NULL, null=True)  # ИД датчика
    quantity_datchik = models.FloatField(null=True)  # Показания датчика
    pribor_id = models.ForeignKey(Pribori, on_delete=models.SET_NULL, null=True)  # ИД прибора
    quantity_pribor = models.FloatField(null=True)  # Показания прибора
    status = models.BooleanField(null=True)  # Статус системы: True - в сети, False - не в сети
