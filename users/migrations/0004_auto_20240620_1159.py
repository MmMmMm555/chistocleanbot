# Generated by Django 3.2.9 on 2024-06-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rm_unused_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, default='uz', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
