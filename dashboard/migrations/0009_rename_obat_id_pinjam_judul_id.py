# Generated by Django 4.1.3 on 2023-02-03 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_pinjam_obat_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pinjam',
            old_name='obat_id',
            new_name='judul_id',
        ),
    ]
