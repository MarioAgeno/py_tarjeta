import pyodbc
from django.db import transaction
#from mi_app.models import Tarjeta, Sucursal, Socio, Localidad, Provincia, Titulo, TarjetaEstado
from apps.maestros.models.tarjeta_models import Tarjeta



# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjeta;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla SQL Server
cursor.execute("SELECT * FROM tjTarjetas")

# Transacción para insertar los datos en Django
with transaction.atomic():
    # Elimina todos los registros del modelo `Tarjeta` en Django
    Tarjeta.objects.all().delete()

    for row in cursor.fetchall():
        Tarjeta.objects.create(
            id_tarjeta=row.id,
            estatus_tarjeta=row.estado == 1,
            numero_tarjeta=int(f"{row.sucursal}{row.socio}{row.adicional}"),
            id_sucursal_tarjeta=Sucursal.objects.get(id=row.sucursal),
            id_socio=Socio.objects.get(id=row.socio),
            adicional=row.adicional,
            digito_verificador=row.verificador,
            nombre_titular=row.nombre,
            domicilio=row.domicilio,
            id_localidad_tarjeta=Localidad.objects.get(nombre=row.localidad),
            id_provincia_tarjeta=Provincia.objects.get(nombre=row.provincia),
            telefono_tarjeta=row.telefono,
            telefono2_tarjeta=row.fax,
            movil_tarjeta=row.movil,
            mail_tarjeta=row.mail,
            nombre_garantia=row.garantia,
            limite_maximo_tarjeta=row.tope,
            saldo_disponible=row.saldo,
            id_titulo=Titulo.objects.get(id=row.titulo),
            id_tarjeta_estado=TarjetaEstado.objects.get(id=row.estado),
            fecha_alta=row.ingreso,
            fecha_baja=row.baja,
            vencimiento=row.vencimiento,
            liquidacion_mail=row.liqxemail,
            seguro=row.seguro,
            observacion=row.observacion
        )

# Cerrar la conexión
conn.close()
