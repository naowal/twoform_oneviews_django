from django.db import models

class Truck_Plan_Collection_Ref(models.Model):
    truck_plan_ref = models.CharField(max_length=20)
    route_trip = models.CharField(max_length=10)
    location_to = models.CharField(max_length=10)
    plan_arrive = models.DateTimeField(null=True)
    number_of_order = models.IntegerField(default=0)
    supplier = models.CharField(max_length=50)

class eDN_ASN_Ref(models.Model):
    edn_asn_ref = models.CharField(max_length=20)
    plant = models.CharField(max_length=10)
    dock = models.CharField(max_length=2)
    due_date = models.DateTimeField(null=True)
    number_of_order = models.IntegerField(default=0)
    supplier = models.CharField(max_length=50)