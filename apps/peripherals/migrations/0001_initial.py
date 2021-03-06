# Generated by Django 2.0.1 on 2018-02-25 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_username', models.CharField(max_length=50)),
                ('perfipheral_pin', models.IntegerField()),
                ('perfipheral_name', models.CharField(max_length=50)),
                ('perfipheral_type_id', models.IntegerField()),
                ('perfipheral_type_name', models.CharField(max_length=50)),
                ('perfipheral_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peripheral',
            fields=[
                ('pin', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeripheralType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='peripheral',
            name='peripheral_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peripherals.PeripheralType'),
        ),
    ]
