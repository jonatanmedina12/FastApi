# API de Productos con FastAPI y AWS Lambda

Este proyecto implementa una API simple de productos utilizando FastAPI y un cliente AWS Lambda para consumir la API. La API maneja operaciones básicas GET y POST para productos tecnológicos.

## Estructura del Proyecto

```
├── api/
│   ├── main.py          # Servidor FastAPI
│   └── requirements.txt  # Dependencias para la API
├── lambda/
│   ├── lambda_function.py    # Cliente Lambda
│   └── requirements.txt      # Dependencias para Lambda
└── README.md
```

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Cuenta AWS (para la función Lambda)
- ngrok (para exponer la API local)

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd [NOMBRE_DEL_PROYECTO]
```

2. Instalar dependencias para la API:
```bash
cd api
pip install -r requirements.txt
```

### Dependencias principales
```
fastapi==0.104.1
uvicorn==0.24.0
requests==2.31.0
```

## Ejecución de la API

1. Iniciar el servidor FastAPI:
```bash
uvicorn main:app --reload
```

2. Exponer la API con ngrok:
```bash
ngrok http 8000
```

## Estructura de Datos

### Modelo de Item
```python
class Item(BaseModel):
    nombre: str
    precio: float
    disponible: bool = True
```

## Endpoints

### API Local

- GET `/items`: Obtiene todos los items
- GET `/items/{item_id}`: Obtiene un item específico por ID
- POST `/items`: Crea un nuevo item

### Ejemplos de Uso

#### Obtener todos los items
```bash
curl http://localhost:8000/items
```

#### Crear un nuevo item
```bash
curl -X POST http://localhost:8000/items \
-H "Content-Type: application/json" \
-d '{"nombre": "Nuevo Producto", "precio": 99.99, "disponible": true}'
```

## Configuración de AWS Lambda

1. Crear una nueva función Lambda
2. Subir el código de `lambda_function.py`
3. Configurar la URL de la API en la variable `API_URL`

### Eventos de Prueba para Lambda

#### GET Request
```json
{
    "httpMethod": "GET"
}
```

#### POST Request
```json
{
    "httpMethod": "POST",
    "body": "{\"nombre\": \"Laptop\", \"precio\": 999.99, \"disponible\": true}"
}
```

## Datos Precargados

La API viene con 10 productos tecnológicos precargados:
- Laptop Gaming
- Monitor 4K
- Teclado Mecánico
- Mouse Gamer
- Auriculares RGB
- Webcam HD
- SSD 1TB
- Tarjeta Gráfica RTX
- RAM 16GB
- Gabinete RGB

## Consideraciones de Seguridad

- La API tiene CORS habilitado para todos los orígenes (`*`)
- No implementa autenticación
- Usa almacenamiento en memoria (no persistente)

## Desarrollo

Para contribuir al proyecto:

1. Crear un fork del repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit a tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Limitaciones

- Los datos se almacenan en memoria y se pierden al reiniciar el servidor
- No incluye validación avanzada de datos
- No implementa manejo de errores avanzado
- No incluye tests

## Posibles Mejoras Futuras

- Agregar persistencia de datos con una base de datos
- Implementar autenticación y autorización
- Agregar más endpoints (PUT, DELETE)
- Implementar validación más robusta
- Agregar documentación con Swagger
- Agregar tests unitarios y de integración
- Implementar rate limiting
- Agregar logging

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)