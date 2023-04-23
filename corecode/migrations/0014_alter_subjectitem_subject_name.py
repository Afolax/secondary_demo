# Generated by Django 4.1.1 on 2023-03-28 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0013_alter_subjectitem_subject_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subjectitem",
            name="subject_name",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="corecode.subject",
            ),
        ),
    ]
