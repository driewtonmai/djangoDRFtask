# Generated by Django 2.2.6 on 2019-10-31 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(1, 'Language courses'), (2, 'culinarnye courses'), (3, 'vojdenie courses'), (4, 'programming courses')])),
                ('impath', models.CharField(max_length=20, verbose_name='Imapath')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'phone'), (2, 'email'), (3, 'facebook')], verbose_name='variants')),
                ('value', models.CharField(max_length=64)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='courses.Course', verbose_name='Contacts')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=64, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=64, verbose_name='Longitude')),
                ('adress', models.CharField(max_length=128, verbose_name='Adress')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='courses.Course', verbose_name='Branch')),
            ],
        ),
    ]
