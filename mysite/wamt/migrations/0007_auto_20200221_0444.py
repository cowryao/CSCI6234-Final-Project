# Generated by Django 3.0.3 on 2020-02-21 09:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('wamt', '0006_auto_20200221_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newgroupmanager',
            name='group_events',
            field=models.ManyToManyField(related_name='event', to='wamt.Event'),
        ),
        migrations.AlterField(
            model_name='newgroupmanager',
            name='group_user',
            field=models.ManyToManyField(related_name='groupuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newusermanager',
            name='group_owned',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='group_owned'),
        ),
    ]
