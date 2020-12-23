# Generated by Django 3.1.3 on 2020-12-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201222_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('عيون', 'عيون'), ('عظام', 'عظام'), ('جراحة', 'جراحة'), ('اشعة', 'اشعة'), ('ولادة', 'ولادة'), ('جلدية', 'جلدية'), ('قلب', 'قلب'), ('مخ واعصاب', 'مخ واعصاب')], max_length=50, null=True, verbose_name=' دكتور ؟:'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='join_now',
            field=models.DateTimeField(auto_now_add=True, default=1, verbose_name='وقت الانضمام :'),
            preserve_default=False,
        ),
    ]