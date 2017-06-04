# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('servis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akcija',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('akcija', models.TextField()),
                ('cijena', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Kupac',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ime', models.CharField(max_length=50)),
                ('prezime', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('marka', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vrsta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('vrsta', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='nalog',
            name='cijena',
            field=models.DecimalField(max_digits=12, null=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='nalog',
            name='dodatno',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='nalog',
            name='odgovor_k',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='nalog',
            name='opis_k',
            field=models.TextField(default='adsasdasd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nalog',
            name='opis_s',
            field=models.TextField(default='adasdasdasd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nalog',
            name='pretpostavka_cijene',
            field=models.DecimalField(max_digits=12, null=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='nalog',
            name='serijski_br',
            field=models.CharField(max_length=50, default=-900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nalog',
            name='upit_k',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='nalog',
            name='serviser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='akcija',
            name='nalog',
            field=models.ForeignKey(to='servis.Nalog'),
        ),
        migrations.AddField(
            model_name='nalog',
            name='kupac',
            field=models.ForeignKey(to='servis.Kupac', default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nalog',
            name='marka',
            field=models.ForeignKey(to='servis.Marka', default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nalog',
            name='status',
            field=models.ForeignKey(to='servis.Status', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nalog',
            name='vrsta',
            field=models.ForeignKey(to='servis.Vrsta', default=1),
            preserve_default=False,
        ),
    ]
