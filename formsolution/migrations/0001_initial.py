# Generated by Django 3.0.11 on 2020-11-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eDN_ASN_Ref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edn_asn_ref', models.CharField(max_length=20)),
                ('plant', models.CharField(max_length=10)),
                ('dock', models.CharField(max_length=2)),
                ('due_date', models.DateTimeField(null=True)),
                ('number_of_order', models.IntegerField(default=0)),
                ('supplier', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Truck_Plan_Collection_Ref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_plan_ref', models.CharField(max_length=20)),
                ('route_trip', models.CharField(max_length=10)),
                ('location_to', models.CharField(max_length=10)),
                ('plan_arrive', models.DateTimeField(null=True)),
                ('number_of_order', models.IntegerField(default=0)),
                ('supplier', models.CharField(max_length=50)),
            ],
        ),
    ]
