# 1. EL FORMATO NUEVO (Lo que usa tu base de datos o API moderna)
class NuevoServicioUsuarios:
    def obtener_usuarios_formato_nuevo(self):
        # El sistema nuevo usa 'full_name' y 'uuid'
        return [
            {"uuid": "123-abc", "full_name": "Ana Garcia", "email": "ana@dev.com"},
            {"uuid": "456-def", "full_name": "Carlos Lopez", "email": "carlos@dev.com"}
        ]

# 2. FUNCIÓN LEGACY (El código antiguo que no quieres o no puedes tocar)
def enviar_notificaciones_legacy(usuarios):
    """
    Esta función solo entiende el formato antiguo:
    Espera una lista de dicts con la clave 'nombre_completo'
    """
    print("--- Iniciando envío de notificaciones (Sistema Legacy) ---")
    for usuario in usuarios:
        # Si no existe 'nombre_completo', esto lanzaría un KeyError
        print(f"Enviando notificación a: {usuario['nombre_completo']}")
    print("--- Proceso finalizado ---")

# 3. CAPA DE COMPATIBILIDAD (El "Adapter")
def obtener_usuarios():
    servicio_nuevo = NuevoServicioUsuarios()
    usuarios_nuevos = servicio_nuevo.obtener_usuarios_formato_nuevo()
    
    usuarios_adaptados = []
    
    for u in usuarios_nuevos:
        # Mapeamos los datos del formato nuevo al formato que espera la función legacy
        adaptado = {
            "id": u["uuid"], # Convertimos uuid a id
            "nombre_completo": u["full_name"] # Traducimos full_name a nombre_completo
        }
        usuarios_adaptados.append(adaptado)
    
    return usuarios_adaptados

# --- EJECUCIÓN ---

# Obtenemos los usuarios a través de la capa de compatibilidad
lista_para_enviar = obtener_usuarios()

# La salida de 'lista_para_enviar' es lo que ves en tu imagen:
# [
#   {"id": "123-abc", "nombre_completo": "Ana Garcia"},
#   {"id": "456-def", "nombre_completo": "Carlos Lopez"}
# ]

# Se lo pasamos a la función vieja y funciona perfectamente
enviar_notificaciones_legacy(lista_para_enviar)
