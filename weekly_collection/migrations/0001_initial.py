# Generated by Django 3.2 on 2021-04-19 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start', models.DateField()),
                ('week_end', models.DateField()),
                ('active', models.BooleanField(default=False, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.recipe')),
                ('week', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='weekly_collection.weeklycollection')),
            ],
        ),
    ]
