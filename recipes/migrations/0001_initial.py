# Generated by Django 3.1.7 on 2021-03-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.CharField(max_length=200)),
                ('allergen', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('main_ingredients', models.CharField(max_length=300)),
                ('meal_picture', models.CharField(max_length=200)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('additional_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('origin', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('M&V', 'Meat and Veggie'), ('VRN', 'Vegetarian'), ('VGN', 'Vegan')], max_length=20)),
                ('description', models.TextField(max_length=600)),
                ('cooking_time', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=20)),
            ],
        ),
    ]
