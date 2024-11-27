# Define las columnas Bootstrap y sección para cada campo
estructura_campos = {
    'actividad': {
        'Información Actividad': {
            'fila_1': [
                {'field_name': 'estatus_actividad', 'columna': 2},
                {'field_name': 'nombre_actividad', 'columna': 4},
                {'field_name': 'interes_actividad', 'columna': 2},
                {'field_name': 'codigo_afip', 'columna': 2},
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
                {'field_name': 'codigo_postal', 'columna': 2},
                {'field_name': 'nombre_localidad', 'columna': 3},
                {'field_name': 'id_provincia', 'columna': 3},
            ]
        }
    },

    'tipo_documento_identidad': {
        'Información Tipo Documento Identidad': {
            'fila_1': [
                {'field_name': 'estatus_tipo_documento_identidad', 'columna': 2},
                {'field_name': 'tipo_documento_identidad', 'columna': 2},
                {'field_name': 'descripcion_documento_identidad', 'columna': 3},
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

    'sucursal': {
        'Información Sucursal': {
            'fila_1': [
                {'field_name': 'estatus_sucursal', 'columna': 2},
            ],
            'fila_2': [
                {'field_name': 'nombre_sucursal', 'columna': 4},
                {'field_name': 'codigo_postal', 'columna': 2},
            ],
            'fila_3': [
                {'field_name': 'domicilio_sucursal', 'columna': 3},
                {'field_name': 'localidad_sucursal', 'columna': 3},
            ],
            'fila_4': [
                {'field_name': 'telefono', 'columna': 2},
                {'field_name': 'telefono2', 'columna': 2},
                {'field_name': 'movil', 'columna': 2},
            ],
            'fila_5': [
                {'field_name': 'mail', 'columna': 6},
            ],
            'fila_6': [
                {'field_name': 'ruta_archivo', 'columna': 6},
            ],
        }
    },

    'plan': {
        'Información Plan': {
            'fila_1': [
                {'field_name': 'estatus_plan', 'columna': 2},
            ],
            'fila_2': [
                {'field_name': 'nombre_plan', 'columna': 4},
                {'field_name': 'vencimiento_plan', 'columna': 2},
            ],
            'fila_3': [
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
                {'field_name': 'domicilio', 'columna': 2},
                {'field_name': 'localidad', 'columna': 2},
                {'field_name': 'provincia', 'columna': 2},
                {'field_name': 'codigo_postal', 'columna': 2},
            ],
            'fila_3': [
                {'field_name': 'telefono', 'columna': 2},
                {'field_name': 'telefono2', 'columna': 2},
                {'field_name': 'movil', 'columna': 2},
            ],
            'fila_4': [
                {'field_name': 'iva', 'columna': 2},
                {'field_name': 'cuit', 'columna': 2},
                {'field_name': 'ingreso_bruto', 'columna': 2},
            ],
            'fila_5': [
                {'field_name': 'mail', 'columna': 3},
                {'field_name': 'web', 'columna': 3},
                {'field_name': 'imagen', 'columna': 3},
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
            'fila_0': [
                {'field_name': 'id_empresa', 'columna': 3},
            ],
            'fila_1': [
                {'field_name': 'gastos', 'columna': 2},
                {'field_name': 'gastos_mail', 'columna': 2},
                {'field_name': 'dias_mora', 'columna': 2},
            ],
            'fila_2': [
                {'field_name': 'tasa', 'columna': 2},
                {'field_name': 'punitorios', 'columna': 2},
                {'field_name': 'minimo', 'columna': 2},
            ],
            'fila_3': [
                {'field_name': 'cierre_ultimo', 'columna': 2},
                {'field_name': 'cierre_actual', 'columna': 2},
                {'field_name': 'cierre_proximo', 'columna': 2},
            ],
            'fila_4': [
                {'field_name': 'vencimiento_ultimo', 'columna': 2},
                {'field_name': 'vencimiento_actual', 'columna': 2},
                {'field_name': 'vencimiento_proximo', 'columna': 2},
            ],
            'fila_5': [
                {'field_name': 'retencion_debito_credito', 'columna': 2},
                {'field_name': 'retencion_iva_estacion_servicio', 'columna': 2},
            ],
            'fila_6': [
                {'field_name': 'retencion_ib_general', 'columna': 2},
                {'field_name': 'retencion_ib', 'columna': 2},
                {'field_name': 'retencion_ib_minimo', 'columna': 2},
            ],
            'fila_7': [
                {'field_name': 'retencion_ganancia', 'columna': 2},
                {'field_name': 'retencion_ganancia_minimo', 'columna': 2},
                {'field_name': 'retencion_ganancia_nc', 'columna': 2},
                {'field_name': 'retencion_ganancia_minimo_nc', 'columna': 2},
            ],
            'fila_8': [
                {'field_name': 'retencion_iva', 'columna': 2},
                {'field_name': 'retencion_iva_nc', 'columna': 2},
                {'field_name': 'retencion_iva_minimo', 'columna': 2},
            ],
            'fila_9': [
                {'field_name': 'sello', 'columna': 2},
                {'field_name': 'seguro', 'columna': 2},
            ],
            'fila_10': [
                {'field_name': 'mensaje', 'columna': 12},
            ],
            'fila_11': [
                {'field_name': 'codigo_roela', 'columna': 2},
            ],        
        }
    },

    'tarjeta_estado': {
        'Información Estados Tarjetas': {
            'fila_1': [
                {'field_name': 'estatus_tarjeta_estado', 'columna': 2},
                {'field_name': 'descripcion_tarjeta_estado', 'columna': 4},
            ],
            'fila_2': [
                {'field_name': 'mensaje', 'columna': 6},
            ],
        }
    },

    'titulo': {
        'Información Titulos': {
            'fila_1': [
                {'field_name': 'estatus_titulo', 'columna': 2},
                {'field_name': 'titulo', 'columna': 4},
            ]
        }
    },

    'plan_comercio': {
        'Información Planes de Comercios': {
            'fila_1': [
                {'field_name': 'estatus_plan_comercio', 'columna': 2},
            ],
            'fila_2': [
                {'field_name': 'id_plan', 'columna': 4},
            ],
            'fila_3': [
                {'field_name': 'id_comercio', 'columna': 4},
            ]
        }
    },

    'comercio': {
        'Información Comercios': {
            'fila_1': [
                {'field_name': 'estatus_comercio', 'columna': 2},
                {'field_name': 'id_sucursal', 'columna': 4},
                {'field_name': 'codigo_comercio', 'columna': 2},
                {'field_name': 'pin', 'columna': 2},
            ],
            'fila_2': [
                {'field_name': 'codigo_socio', 'columna': 2},
                {'field_name': 'nombre_titular', 'columna': 4},
                {'field_name': 'razon_social_comercio', 'columna': 4},
            ],
            'fila_3': [
                {'field_name': 'domicilio_comercio', 'columna': 3},
                {'field_name': 'id_provincia', 'columna': 3},
                {'field_name': 'id_localidad', 'columna': 3},
            ],
            'fila_5': [
                {'field_name': 'telefono_comercio', 'columna': 2},
                {'field_name': 'telefono2_comercio', 'columna': 2},
                {'field_name': 'movil_comercio', 'columna': 2},
            ],
            'fila_6': [
                {'field_name': 'mail_comercio', 'columna': 3},
                {'field_name': 'id_actividad', 'columna': 3},
            ],
            'fila_7': [
                {'field_name': 'id_tipo_iva', 'columna': 2},
                {'field_name': 'cuit_comercio', 'columna': 2},
                {'field_name': 'ingreso_bruto', 'columna': 2},
                {'field_name': 'porcentaje_consumo', 'columna': 2},
                {'field_name': 'porcentaje_retencion_ib', 'columna': 2},
            ],
            'fila_9': [
                {'field_name': 'monto_fijo', 'columna': 2},
                {'field_name': 'exento_ganancias', 'columna': 2},
                {'field_name': 'estacion_servicio', 'columna': 2},
                {'field_name': 'debito_credito', 'columna': 2},
                {'field_name': 'acreditar_cuenta', 'columna': 2},
            ],
            'fila_11': [
                {'field_name': 'mensaje', 'columna': 6},
            ],
            'fila_12': [
                {'field_name': 'leido', 'columna': 2},
            ],
        }
    },

    'tarjeta': {
        'Información Tarjeta': {
            'fila_1': [
                {'field_name': 'estatus_tarjeta', 'columna': 2},
                {'field_name': 'id_sucursal', 'columna': 4},
            ],
            'fila_2': [
                {'field_name': 'codigo_socio', 'columna': 2},
                {'field_name': 'nombre_titular', 'columna': 4},
                {'field_name': 'adicional', 'columna': 2},
                {'field_name': 'digito_verificador', 'columna': 2},
                {'field_name': 'numero_tarjeta', 'columna': 2},
            ],
            'fila_3': [
                {'field_name': 'nombre_garantia', 'columna': 3},
                {'field_name': 'id_titulo', 'columna': 3},
                {'field_name': 'id_tarjeta_estado', 'columna': 3},
            ],
            'fila_4': [
                {'field_name': 'fecha_alta', 'columna': 2},
                {'field_name': 'vencimiento', 'columna': 2},
                {'field_name': 'fecha_baja', 'columna': 2},
                {'field_name': 'limite_maximo_tarjeta', 'columna': 2},
                {'field_name': 'saldo_disponible', 'columna': 2},
            ],
            'fila_5': [
                {'field_name': 'domicilio', 'columna': 3},
                {'field_name': 'id_provincia', 'columna': 3},
                {'field_name': 'id_localidad', 'columna': 3},
            ],
            'fila_6': [
                {'field_name': 'telefono_tarjeta', 'columna': 2},
                {'field_name': 'telefono2_tarjeta', 'columna': 2},
                {'field_name': 'movil_tarjeta', 'columna': 2},
                {'field_name': 'mail_tarjeta', 'columna': 3},
            ],
            'fila_7': [
                {'field_name': 'observacion', 'columna': 6},
                {'field_name': 'liquidacion_mail', 'columna': 2},
                {'field_name': 'seguro', 'columna': 1},
            ],
        }
    },

    'registro_limite': {
        'Información Limites de tarjetas': {
            'fila_1': [
                {'field_name': 'estatus_registro_limite', 'columna': 2},
                {'field_name': 'id_tarjeta', 'columna': 4},
            ],
            'fila_2': [
                {'field_name': 'maximo_limite', 'columna': 3},
                {'field_name': 'fecha_limite', 'columna': 2},
            ],
        }
    },
}
