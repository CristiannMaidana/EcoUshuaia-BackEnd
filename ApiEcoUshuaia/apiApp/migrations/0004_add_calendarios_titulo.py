# apiApp/migrations/0004_calendarios_add_titulo.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('apiApp', '0003_alter_usuarios_email'),
    ]
    operations = [
        migrations.AddField(
            model_name='calendarios',
            name='titulo',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
