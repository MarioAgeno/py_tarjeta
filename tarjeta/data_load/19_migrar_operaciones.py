# Migrar tabla Operaciones al modelos DJango

import os
import sys
import django
from django.db import connection

# Agrega la ruta base del proyecto y la ruta interna del settings al PATH
sys.path.append("D:/Python/PROYECTO_TARJETA/tarjeta")

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tarjeta.settings")
django.setup()

import pyodbc
from django.db import transaction
from apps.maestros.models.base_models import Plan
from apps.maestros.models.comercio_models import Comercio
from apps.maestros.models.tarjeta_models import Tarjeta
from apps.maestros.models.compra_models import Operacion

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

conusulta = '''
select tjOperaciones.* from tjOperaciones inner join tjTarjetas on tjOperaciones.idtarjeta = tjTarjetas.id 
	inner join tjComercios on tjOperaciones.idcomercio = tjComercios.id
	inner join tjPlanes on tjOperaciones.idplan = tjPlanes.id 
'''
# Query para obtener los datos de la tabla SQL Server
cursor.execute(conusulta)

def reset_modelo():
    # Elimina todos los registros del modelo `Opracion` en Django
    Operacion.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='operacion'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    # Variable para contar los registros procesados
    contador = 0
    
    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        # print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        plan = Plan.objects.get(id_plan=row[6])
        comercio = Comercio.objects.get(codigo_comercio=row[3])
        tarjeta = Tarjeta.objects.get(numero_tarjeta=row[4])

        if not plan: 
            print(f"No se encontró el Plan: {row[6]}")
            continue

        if not comercio: 
            print(f"No se encontró el Comercio : {row[3]}")
            continue

        if not tarjeta: 
            print(f"No se encontró la Tarjeta : {row[4]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `compra` y la consulta SQL
        Operacion.objects.create(
            id_operacion=row[0],
            cupon_operacion=row[1],
            fecha_operacion=row[2],
            id_comercio=comercio,
            id_tarjeta=tarjeta,
            importe_compra=row[5],
            id_plan=plan,
            autorizacion=row[7],   
            acreditado=row[8],   
            liquidacion_comercio=row[9],   
            estado_operacion=row[10],
            tipo_carga=row[11]
        )

        # Incrementar el contador
        contador += 1

        # Imprimir el contador cada 100 registros
        if contador % 500 == 0:
            print(f"{contador} registros insertados...")

# Cerrar la conexión
conn.close()

