# Generated by Django 2.1.7 on 2019-04-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penagihan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_ba', models.CharField(max_length=255)),
                ('nama_anggota', models.CharField(max_length=255)),
                ('alamat', models.TextField()),
                ('no_hp', models.CharField(max_length=13)),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.TextField()),
            ],
        ),
    ]