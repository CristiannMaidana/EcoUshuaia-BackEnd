from django.db import migrations, models
import django.utils.timezone as tz

class Migration(migrations.Migration):
    dependencies = [
        ('apiApp', '0004_add_calendarios_titulo')
    ]
    operations = [
        migrations.RenameField(
            model_name='calendarios',
            old_name='novedad',
            new_name='cuerpo'
        ),
        migrations.AddField(
            model_name='calendarios',
            name='duracion',
            field=models.DurationField(default=0), preserve_default=False
        ),
        migrations.AddField(
            model_name='calendarios',
            name='subtitulo',
            field=models.CharField(max_length=160, blank=True, null=True)
        ),
        migrations.AddField(
            model_name='calendarios',
            name='todo_el_dia',
            field=models.BooleanField(default=False)
        ),
        migrations.AddField(
            model_name='calendarios',
            name= 'categoria_noticia',
            field= models.CharField(max_length=40, default=''),  preserve_default=False
        ),
        migrations.AddField(
            model_name='calendarios',
            name= 'creado_at',
            field= models.DateTimeField(default=tz.now), preserve_default=False
        ),
    ]
