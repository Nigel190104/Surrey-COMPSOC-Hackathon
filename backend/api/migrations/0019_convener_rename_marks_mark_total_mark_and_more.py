# Generated by Django 5.0.2 on 2024-03-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_convener'),
    ]

    operations = [
        
        migrations.RenameField(
            model_name='mark',
            old_name='marks',
            new_name='total_mark',
        ),
        migrations.AddField(
            model_name='mark',
            name='functional_criteria',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mark',
            name='style_criteria',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mark',
            name='syntax_criteria',
            field=models.IntegerField(default=0),
        ),
    ]