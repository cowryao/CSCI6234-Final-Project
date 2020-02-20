# Generated by Django 3.0.3 on 2020-02-20 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('wamt', '0002_auto_20200220_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_location', models.CharField(max_length=200)),
                ('event_start_vote_time', models.DateTimeField(verbose_name='start vote time')),
                ('event_end_vote_time', models.DateTimeField(verbose_name='end vote time')),
                ('event_time', models.DateTimeField(verbose_name='event time')),
            ],
        ),
        migrations.CreateModel(
            name='GroupEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('group_events', models.ManyToManyField(to='wamt.Event')),
            ],
        ),
    ]
