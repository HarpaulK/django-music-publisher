# Generated by Django 3.0.6 on 2020-07-08 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0007_auto_20200629_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalPublishingAgreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'ordering': ('name',), 'verbose_name': 'Music Library', 'verbose_name_plural': 'Music Libraries'},
        ),
        migrations.AddField(
            model_name='writer',
            name='original_publishing_agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='music_publisher.OriginalPublishingAgreement', verbose_name='Original Agreement'),
        ),
        migrations.AddField(
            model_name='writerinwork',
            name='original_publishing_agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='music_publisher.OriginalPublishingAgreement', verbose_name='Original Agreement'),
        ),
    ]
