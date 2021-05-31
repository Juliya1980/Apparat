from django.db import models

# Create your models here.

class Zone(models.Model):
    id = models.AutoField(primary_key=True)  # ИД зоны
    name = models.TextField(null=True)  # Имя зоны


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)  # ИД датчика
    name = models.TextField(null=True)  # Наименование датчика
    zone_id = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)  # Зона нахождения
    status = models.BooleanField(null=True)  # Статус датчика: True - в сети, False - не в сети


class Pribori(models.Model):
    id = models.AutoField(primary_key=True)  # ИД прибора
    name = models.TextField(null=True)  # Наименование прибора
    zone_id = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)  # Зона нахождения
    status = models.BooleanField(null=True)  # Статус прибора: True - в сети, False - не в сети


class Rezim(models.Model):
    id = models.AutoField(primary_key=True)  # ИД режима
    name = models.TextField(null=True)  # Наименование режима
    len_rezim = models.FloatField(null=True)  # Длительность режима
    datchik_id = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True)  # ИД датчика
    normativ_datchik = models.FloatField(null=True)  # Нормативное значение датчика
    pribor_id = models.ForeignKey(Pribori, on_delete=models.SET_NULL, null=True)  # ИД прибора
    normativ_pribor = models.FloatField(null=True)  # Нормативное значение прибора


class Product(models.Model):
    id = models.AutoField(primary_key=True)  # ИД продукта
    name = models.TextField(null=True)  # Наименование продукта
    time_oper = models.DateTimeField(null=True)  # Дата и время окончания приготовления продукта
    value = models.FloatField(null=True)  # Количество продукта
    ediz = models.TextField(null=True)  # Единицы измерения
    prim = models.TextField(null=True)  # Примечание / вкусовые характеристики
    rezim_id = models.ForeignKey(Rezim, on_delete=models.SET_NULL, null=True)  # Использованный режим


class SystemChanges(models.Model):
    id = models.AutoField(primary_key=True)  # ИД операции мониторинга системы
    time_oper = models.DateTimeField(null=True)  # Время совершения операции
    datchik_id = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True)  # ИД датчика
    quantity_datchik = models.FloatField(null=True)  # Показания датчика
    pribor_id = models.ForeignKey(Pribori, on_delete=models.SET_NULL, null=True)  # ИД прибора
    quantity_pribor = models.FloatField(null=True)  # Показания прибора
    status = models.BooleanField(null=True)  # Статус системы: True - в сети, False - не в сети
