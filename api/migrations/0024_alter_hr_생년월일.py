# Generated by Django 4.1.7 on 2023-03-10 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0023_alter_hr_개인이메일_alter_hr_경력사항1_alter_hr_경력사항2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hr",
            name="생년월일",
            field=models.DateField(blank=True, null=True),
        ),
    ]
