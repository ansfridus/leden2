# Generated by Django 2.1.5 on 2019-03-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LedenAdministratie', '0014_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='payed',
        ),
        migrations.AddField(
            model_name='invoice',
            name='amount_payed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Bedrag Betaald'),
        ),
    ]
