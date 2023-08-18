from django.db import models


class Airport(models.Model):
    name = models.TextField(db_column='Name', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Airport'


class Flight(models.Model):
    flyght_id = models.BigAutoField(primary_key=True)
    attribute1 = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='Attribute1', blank=True, null=True)  # Field name made lowercase.
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Flight'


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    login = models.ForeignKey('User', models.DO_NOTHING, db_column='login')
    order_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Order'


class Schedule(models.Model):
    schedule_id = models.BigAutoField(primary_key=True)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)
    departure_city_name = models.ForeignKey(Airport, models.DO_NOTHING, db_column='departure_city_name',
                                            related_name='%(class)s_departure_city_name')
    arrival_city_name = models.ForeignKey(Airport, models.DO_NOTHING, db_column='arrival_city_name',
                                          related_name='%(class)s_arrival_city_name')
    duration = models.BigIntegerField(db_column='Duration')  # Field name made lowercase.
    monday = models.TimeField(db_column='Monday', blank=True, null=True)  # Field name made lowercase.
    tuesday = models.TimeField(db_column='Tuesday', blank=True, null=True)  # Field name made lowercase.
    wednesday = models.TimeField(db_column='Wednesday', blank=True, null=True)  # Field name made lowercase.
    thursday = models.TimeField(db_column='Thursday', blank=True, null=True)  # Field name made lowercase.
    friday = models.TimeField(db_column='Friday', blank=True, null=True)  # Field name made lowercase.
    saturday = models.TimeField(db_column='Saturday', blank=True, null=True)  # Field name made lowercase.
    sunday = models.TimeField(db_column='Sunday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedule'


class Ticket(models.Model):
    ticket_id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    flyght = models.ForeignKey(Flight, models.DO_NOTHING)
    pasport_id = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    seat_number = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ticket'


class User(models.Model):
    login = models.TextField(primary_key=True)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'User'


class Vehicle(models.Model):
    vehicle_id = models.TextField(primary_key=True)
    assembly_date = models.DateTimeField()
    type = models.TextField()
    seat_amount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vehicle'
