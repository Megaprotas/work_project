# Generated by Django 3.0.5 on 2020-05-27 17:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor', models.CharField(default='', max_length=100)),
                ('contractor_name', models.CharField(default='', max_length=100)),
                ('facility', models.CharField(default='', max_length=100)),
                ('date_of_arrival', models.DateField(default=django.utils.timezone.now)),
                ('time_of_arrival', models.TimeField(default=django.utils.timezone.now)),
                ('date_of_finish', models.DateField(default=django.utils.timezone.now)),
                ('time_of_finish', models.TimeField(default=django.utils.timezone.now)),
                ('job_location', models.CharField(default='', max_length=100)),
                ('job_spec', models.TextField(default='', max_length=500)),
                ('equipment', models.TextField(default='', max_length=100)),
                ('status_closed', models.BooleanField(default=False)),
                ('works_completed', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ElectricalWorks',
            fields=[
                ('permit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='permits.Permit')),
                ('location1', models.CharField(default='', max_length=100)),
                ('location2', models.CharField(default='', max_length=100)),
                ('location3', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Electrical Works Permit',
                'verbose_name_plural': 'Electrical Works Permits',
                'ordering': ('date_of_arrival',),
            },
            bases=('permits.permit',),
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('permit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='permits.Permit')),
                ('safety_precautions', models.TextField(default='', max_length=200)),
                ('ra_ready', models.BooleanField(default=False)),
                ('ms_ready', models.BooleanField(default=False)),
                ('confined_space_entry', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'General Permit',
                'verbose_name_plural': 'General Permits',
                'ordering': ('date_of_arrival',),
            },
            bases=('permits.permit',),
        ),
        migrations.CreateModel(
            name='HotWorks',
            fields=[
                ('permit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='permits.Permit')),
                ('ppe', models.BooleanField(default=False)),
                ('welding_screen', models.BooleanField(default=False)),
                ('smoke_heat_isolated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Hot Works Permit',
                'verbose_name_plural': 'Hot Works Permits',
                'ordering': ('date_of_arrival',),
            },
            bases=('permits.permit',),
        ),
    ]