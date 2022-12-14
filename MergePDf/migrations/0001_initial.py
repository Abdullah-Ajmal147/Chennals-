# Generated by Django 3.2.15 on 2022-09-29 17:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelA',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='modelB',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('describe', models.CharField(blank=True, max_length=50, null=True)),
                ('modela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modela', to='MergePDf.modela')),
            ],
        ),
    ]
