# Generated by Django 4.1.1 on 2023-03-28 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("staffs", "0001_initial"),
        ("corecode", "0009_alter_assignsubject_class_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignsubject",
            name="class_name",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="corecode.studentclass",
            ),
        ),
        migrations.AlterField(
            model_name="assignsubject",
            name="teacher_name",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="staffs.staff",
            ),
        ),
        migrations.AlterField(
            model_name="subjectitem",
            name="subject_data",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="corecode.assignsubject",
            ),
        ),
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