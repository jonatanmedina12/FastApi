import json
import urllib.request
import urllib.error
import urllib.parse

# URL de ngrok
API_URL = "https://76eb-186-99-157-66.ngrok-free.app"


def make_request(path, method='GET', data=None):
    """Función auxiliar para hacer peticiones HTTP"""
    try:
        url = f"{API_URL}{path}"
        headers = {
            'Content-Type': 'application/json',
            # Ngrok puede requerir este header para evitar errores de forbidden
            'ngrok-skip-browser-warning': 'true'
        }

        if data:
            data = json.dumps(data).encode('utf-8')

        req = urllib.request.Request(
            url,
            data=data,
            headers=headers,
            method=method
        )

        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))

    except urllib.error.URLError as e:
        return {"error": f"Error de conexión: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


def get_items():
    """Obtiene todos los items"""
    return make_request('/items')


def create_item(nombre, precio, disponible=True):
    """Crea un nuevo item"""
    item = {
        "nombre": nombre,
        "precio": precio,
        "disponible": disponible
    }
    return make_request('/items', method='POST', data=item)


def lambda_handler(event, context):
    """
    Función principal que será llamada por AWS Lambda
    """
    try:
        # Determinar qué acción tomar basado en el evento
        http_method = event.get('httpMethod', 'GET')

        if http_method == 'GET':
            result = get_items()
        elif http_method == 'POST':
            # Asumimos que el body viene en el evento
            body = json.loads(event.get('body', '{}'))
            result = create_item(
                nombre=body.get('nombre'),
                precio=body.get('precio'),
                disponible=body.get('disponible', True)
            )
        else:
            result = {"error": "Método no soportado"}

        return {
            'statusCode': 200,
            'body': json.dumps(result),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }


# Para pruebas locales
if __name__ == "__main__":
    # Prueba GET
    print("Probando GET items:")
    print(get_items())