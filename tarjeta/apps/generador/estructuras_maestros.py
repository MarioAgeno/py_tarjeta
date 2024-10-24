# Define las columnas Bootstrap y sección para cada campo
estructura_campos = {
    'actividad': {
        'Información Actividad': {
            'fila_1': [
                {'field_name': 'estatus_actividad', 'columna': 2},
                {'field_name': 'descripcion_actividad', 'columna': 4},
                {'field_name': 'fecha_registro_actividad', 'columna': 2}
            ]
        }
    },

    'provincia': {
        'Información Provincia': {
            'fila_1': [
                {'field_name': 'estatus_provincia', 'columna': 2},
                {'field_name': 'codigo_provincia', 'columna': 1},
                {'field_name': 'nombre_provincia', 'columna': 3},
            ]
        }
    },

    'localidad': {
        'Información Localidad': {
            'fila_1': [
                {'field_name': 'estatus_localidad', 'columna': 2},
                {'field_name': 'nombre_localidad', 'columna': 3},
                {'field_name': 'codigo_postal', 'columna': 2},
                {'field_name': 'id_provincia', 'columna': 3},
            ]
        }
    },

    'tipo_documento_identidad': {
        'Información Tipo Documento Identidad': {
            'fila_1': [
                {'field_name': 'estatus_tipo_documento_identidad', 'columna': 2},
                {'field_name': 'nombre_documento_identidad', 'columna': 2},
                {'field_name': 'tipo_documento_identidad', 'columna': 2},
                {'field_name': 'codigo_afip', 'columna': 2},
                {'field_name': 'ws_afip', 'columna': 2},
            ]
        }
    },

    'tipo_iva': {
        'Información Tipo I.V.A.': {
            'fila_1': [
                {'field_name': 'estatus_tipo_iva', 'columna': 2},
                {'field_name': 'codigo_iva', 'columna': 2},
                {'field_name': 'nombre_iva', 'columna': 3},
                {'field_name': 'discrimina_iva', 'columna': 2},
            ]
        }
    },

    'cliente': {
        'Información General': {
            'fila_1': [
                {'field_name': 'estatus_cliente', 'columna': 2},
                {'field_name': 'nombre_cliente', 'columna': 4},
                {'field_name': 'domicilio_cliente', 'columna': 6},
            ],
            'fila_2': [
                {'field_name': 'codigo_postal', 'columna': 2},
                {'field_name': 'id_provincia', 'columna': 4},
                {'field_name': 'id_localidad', 'columna': 4},
            ],
            'fila_3': [
                {'field_name': 'tipo_persona', 'columna': 2},
                {'field_name': 'id_tipo_documento_identidad', 'columna': 2},
                {'field_name': 'cuit', 'columna': 2},
                {'field_name': 'id_tipo_iva', 'columna': 2},
                {'field_name': 'condicion_venta', 'columna': 2},
            ],
            'fila_4': [
                {'field_name': 'telefono_cliente', 'columna': 2},
                {'field_name': 'fax_cliente', 'columna': 2},
                {'field_name': 'movil_cliente', 'columna': 2},
                {'field_name': 'email_cliente', 'columna': 3},
                {'field_name': 'email2_cliente', 'columna': 3},
            ],
            'fila_5': [
                {'field_name': 'transporte_cliente', 'columna': 3},
                {'field_name': 'id_vendedor', 'columna': 3},
                {'field_name': 'fecha_nacimiento', 'columna': 2},
                {'field_name': 'fecha_alta', 'columna': 2},
                {'field_name': 'sexo', 'columna': 2},
            ],
            'fila_6': [
                {'field_name': 'id_actividad', 'columna': 3},
                {'field_name': 'id_sucursal', 'columna': 3},
                {'field_name': 'id_percepcion_ib', 'columna': 3},
                {'field_name': 'numero_ib', 'columna': 3},
            ],
            'fila_7': [
                {'field_name': 'vip', 'columna': 2},
                {'field_name': 'mayorista', 'columna': 2},
                {'field_name': 'sub_cuenta', 'columna': 2},
                {'field_name': 'observaciones_cliente', 'columna': 6},
            ],
            # Agrega más filas o campos según sea necesario
        },
        'Black List': {
            'fila_1': [
                {'field_name': 'black_list', 'columna': 2},
                {'field_name': 'black_list_motivo', 'columna': 5},
                {'field_name': 'black_list_usuario', 'columna': 3},
                {'field_name': 'fecha_baja', 'columna': 2},
            ],
        },
    },

    'sucursal': {
        'Información Sucursal': {
            'fila_1': [
                {'field_name': 'estatus_sucursal', 'columna': 2},
                {'field_name': 'nombre_sucursal', 'columna': 4},
                {'field_name': 'codigo_michelin', 'columna': 2},
            ],
            'fila_2': [
                {'field_name': 'domicilio_sucursal', 'columna': 4},
                {'field_name': 'id_localidad', 'columna': 2},
                {'field_name': 'id_provincia', 'columna': 2},
            ],
            'fila_3': [
                {'field_name': 'telefono_sucursal', 'columna': 2},
                {'field_name': 'email_sucursal', 'columna': 4},
                {'field_name': 'inicio_actividad', 'columna': 2},
            ],
        }
    },

    'plan': {
        'Información Plan': {
            'fila_1': [
                {'field_name': 'estatus_plan', 'columna': 2},
                {'field_name': 'nombre_plan', 'columna': 4},
                {'field_name': 'vencimiento_plan', 'columna': 2},
            ],
            'fila_2': [
                {'field_name': 'interes_plan', 'columna': 2},
                {'field_name': 'costo_financiero_plan', 'columna': 2},
                {'field_name': 'cuotas_plan', 'columna': 2}
            ]
        }
    },

    'empresa': {
        'Información Empresa': {
            'fila_1': [
                {'field_name': 'estatus_empresa', 'columna': 2},
                {'field_name': 'razon_social', 'columna': 4},
                {'field_name': 'nombre_empresa', 'columna': 4},
            ],
            'fila_2': [
                {'field_name': 'domicilio', 'columna': 4},
                {'field_name': 'localidad', 'columna': 3},
                {'field_name': 'provincia', 'columna': 3},
                {'field_name': 'codigo_postal', 'columna': 2},
            ],
            'fila_3': [
                {'field_name': 'telefono', 'columna': 3},
                {'field_name': 'telefono2', 'columna': 3},
                {'field_name': 'movil', 'columna': 3},
            ],
            'fila_4': [
                {'field_name': 'iva', 'columna': 3},
                {'field_name': 'cuit', 'columna': 2},
                {'field_name': 'ingreso_bruto', 'columna': 2},
            ],
            'fila_5': [
                {'field_name': 'mail', 'columna': 4},
                {'field_name': 'web', 'columna': 4},
                {'field_name': 'imagen', 'columna': 4},
            ],
        }
    },

    'numero': {
        'Información Numeros': {
            'fila_1': [
                {'field_name': 'cupon', 'columna': 3},
            ],
        }
    },

    'parametro': {
        'Información Parámetros': {
            'fila_1': [
                {'field_name': 'gastos', 'columna': 2},
                {'field_name': 'tasa', 'columna': 2},
                {'field_name': 'punitorios', 'columna': 2},
                {'field_name': 'minimo', 'columna': 2},
            ],
            'fila_2': [
                {'field_name': 'cierre_ultimo', 'columna': 3},
                {'field_name': 'cierre_actual', 'columna': 3},
                {'field_name': 'cierre_proximo', 'columna': 3},
            ],
            'fila_3': [
                {'field_name': 'vencimiento_ultimo', 'columna': 3},
                {'field_name': 'vencimiento_actual', 'columna': 3},
                {'field_name': 'vencimiento_proximo', 'columna': 3},
            ],
            'fila_4': [
                {'field_name': 'retencion_debito_credito', 'columna': 3},
                {'field_name': 'retencion_iva_estacion_servicio', 'columna': 3},
            ],
            'fila_5': [
                {'field_name': 'retencion_ib_general', 'columna': 3},
                {'field_name': 'retencion_ib', 'columna': 3},
                {'field_name': 'retencion_ib_minimo', 'columna': 3},
            ],
            'fila_6': [
                {'field_name': 'retencion_ganancia', 'columna': 3},
                {'field_name': 'retencion_ganancia_minimo', 'columna': 3},
                {'field_name': 'retencion_ganancia_nc', 'columna': 3},
                {'field_name': 'retencion_ganancia_minimo_nc', 'columna': 3},
            ],
            'fila_7': [
                {'field_name': 'retencion_iva', 'columna': 3},
                {'field_name': 'retencion_iva_nc', 'columna': 3},
                {'field_name': 'retencion_iva_minimo', 'columna': 3},
            ],
            'fila_8': [
                {'field_name': 'sello', 'columna': 3},
                {'field_name': 'seguro', 'columna': 3},
                {'field_name': 'dias_mora', 'columna': 3},
                {'field_name': 'gastos_mail', 'columna': 3},
            ],
            'fila_9': [
                {'field_name': 'mensaje', 'columna': 12},
            ],
            'fila_10': [
                {'field_name': 'codigo_roela', 'columna': 2},
            ],        

        }
    },
}
