# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Calendarios(models.Model):
    id_calendario = models.AutoField(primary_key=True)
    novedad = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()

    class Meta:
        managed = False
        db_table = 'calendarios'

    def __str__(self):
        return f"{self.fecha} {self.hora} {self.novedad}"


class Contenedores(models.Model):
    id_contenedor = models.AutoField(primary_key=True)
    nombre_contenedor = models.CharField(max_length=50)
    color_contenedor = models.CharField(max_length=20)
    capacidad_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fecha_instalacion = models.DateField(blank=True, null=True)
    ultimo_vaciado = models.DateTimeField(blank=True, null=True)
    descripcion_ubicacion = models.TextField(blank=True, null=True)
    id_zona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='id_zona', blank=True, null=True)
    id_residuo = models.ForeignKey('Residuos', models.DO_NOTHING, db_column='id_residuo', blank=True, null=True)
    id_coordenada = models.ForeignKey('Coordenadas', models.DO_NOTHING, db_column='id_coordenada', blank=True, null=True)
    id_mapa = models.ForeignKey('Mapas', models.DO_NOTHING, db_column='id_mapa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contenedores'
        unique_together = (('nombre_contenedor', 'id_mapa'),)


class Coordenadas(models.Model):
    id_coordenada = models.AutoField(primary_key=True)
    archivo_coordenada = models.JSONField(unique=True, blank=True, null=True)
    tipo_archivo = models.CharField(max_length=30, blank=True, null=True)
    coordenada = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    tipo_coordenada = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coordenadas'


class Direcciones(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    barrio = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    codigo_postal = models.CharField(max_length=20, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    id_coordenada = models.ForeignKey(Coordenadas, models.DO_NOTHING, db_column='id_coordenada', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'


class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    fecha_estado = models.DateTimeField(blank=True, null=True)
    volumen = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    id_sensor = models.ForeignKey('Sensores', models.DO_NOTHING, db_column='id_sensor', blank=True, null=True)
    id_tipo_estado = models.ForeignKey('TipoEstados', models.DO_NOTHING, db_column='id_tipo_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


class Mapas(models.Model):
    id_mapa = models.AutoField(primary_key=True)
    nombre_mapa = models.CharField(unique=True, max_length=50)
    id_coordenada = models.ForeignKey(Coordenadas, models.DO_NOTHING, db_column='id_coordenada')

    class Meta:
        managed = False
        db_table = 'mapas'


class MedicionSensores(models.Model):
    id_medicion_sensor = models.AutoField(primary_key=True)
    fecha_hora_medicion = models.DateTimeField()
    porcentaje_ocupacion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    volumen_medido = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    alerta_generada = models.BooleanField(blank=True, null=True)
    id_sensor = models.ForeignKey('Sensores', models.DO_NOTHING, db_column='id_sensor')
    id_contenedor = models.ForeignKey(Contenedores, models.DO_NOTHING, db_column='id_contenedor')

    class Meta:
        managed = False
        db_table = 'medicion_sensores'


class Notificaciones(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField()
    tipo_notificacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificaciones'


class RegistroRecolecciones(models.Model):
    id_registro_recoleccion = models.AutoField(primary_key=True)
    volumen = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_hora_recoleccion = models.DateTimeField()
    observaciones = models.TextField(blank=True, null=True)
    id_contenedor = models.ForeignKey(Contenedores, models.DO_NOTHING, db_column='id_contenedor')
    id_residuo = models.ForeignKey('Residuos', models.DO_NOTHING, db_column='id_residuo')
    id_zona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='id_zona')
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'registro_recolecciones'


class Residuos(models.Model):
    id_residuo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    instruccion_reciclado = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'residuos'

    def __str__(self):
        return self.nombre


class Sensores(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    nombre_sensor = models.CharField(max_length=50)
    fecha_instalacion_sensor = models.DateField(blank=True, null=True)
    numero_serie = models.CharField(unique=True, max_length=100)
    id_contenedor = models.ForeignKey(Contenedores, models.DO_NOTHING, db_column='id_contenedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensores'
        unique_together = (('id_contenedor', 'nombre_sensor'),)


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class TipoEstados(models.Model):
    id_tipo_estado = models.AutoField(primary_key=True)
    nombre_estados = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_estados'


class TipoUsuarios(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_usuarios'

    def __str__(self):
        return self.tipo_usuario


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    id_direccion = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='id_direccion', blank=True, null=True)
    id_zona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='id_zona', blank=True, null=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuarios, models.DO_NOTHING, db_column='id_tipo_usuario', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usuarios'


class UsuariosHistorialesResiduos(models.Model):
    id_usuario_historial_residuos = models.AutoField(primary_key=True)
    cantidad_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unidad = models.CharField(max_length=10, blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    id_residuo = models.ForeignKey(Residuos, models.DO_NOTHING, db_column='id_residuo')
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'usuarios_historiales_residuos'
        unique_together = (('id_usuario', 'id_residuo'),)


class UsuariosRegistroContenedores(models.Model):
    id_usuario_registro_contenedor = models.AutoField(primary_key=True)
    nota_usuario_contenedor = models.TextField(blank=True, null=True)
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario')
    id_contenedor = models.ForeignKey(Contenedores, models.DO_NOTHING, db_column='id_contenedor')

    class Meta:
        managed = False
        db_table = 'usuarios_registro_contenedores'
        unique_together = (('id_usuario', 'id_contenedor'),)


class UsuariosTienenNotificaciones(models.Model):
    id_usuario_notificacion = models.AutoField(primary_key=True)
    leido = models.BooleanField(blank=True, null=True)
    fecha_recibido = models.DateTimeField(blank=True, null=True)
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario')
    id_notificaciones = models.ForeignKey(Notificaciones, models.DO_NOTHING, db_column='id_notificaciones')

    class Meta:
        managed = False
        db_table = 'usuarios_tienen_notificaciones'
        unique_together = (('id_usuario', 'id_notificaciones'),)


class Zonas(models.Model):
    id_zona = models.AutoField(primary_key=True)
    nombre_zona = models.CharField(max_length=50, blank=True, null=True)
    color_zona = models.CharField(max_length=20, blank=True, null=True)
    id_mapa = models.ForeignKey(Mapas, models.DO_NOTHING, db_column='id_mapa', blank=True, null=True)
    id_calendario = models.ForeignKey(Calendarios, models.DO_NOTHING, db_column='id_calendario', blank=True, null=True)
    id_coordenada = models.ForeignKey(Coordenadas, models.DO_NOTHING, db_column='id_coordenada', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas'
        unique_together = (('nombre_zona', 'id_mapa'), ('color_zona', 'id_mapa'),)
