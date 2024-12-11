# Microblogging API

Microblogging API es una plataforma de blogging simple que permite a los usuarios crear mensajes breves, seguir a otros usuarios y ver un timeline combinado de los tweets de las personas que siguen. Esta solución está diseñada para ser escalable y de alto rendimiento, utilizando Redis para el manejo de datos en memoria.

## Características

- **Publicación de tweets**: Los usuarios pueden publicar mensajes breves.
- **Seguir a otros usuarios**: Los usuarios pueden seguir a otros para construir su red.
- **Timeline combinado**: Mezcla de tweets de los usuarios que sigue, ordenados cronológicamente.

## 🛠 Tecnologías Utilizadas

- **Python 3.11**: Para la implementación de la API.
- **FastAPI:** Para construir la API REST.
- **Redis:** Para almacenamiento in-memory rápido y eficiente.
- **Docker:** Para empaquetar y correr fácilmente la aplicación.
- **Pytest:** Para testing automatizado.

## 🚀 Configuración

### Requisitos
- Python 3.11+
- Redis
- Docker (opcional, para usar contenedores)

### Instalación

1. Clona este repositorio:

    git clone https://github.com/Flor87Posta/Microblogging.git
    cd Microblogging

2. Instala las dependencias:

    python -m venv env
    source env/bin/activate  # Linux/Mac
    env\Scripts\activate     # Windows
    pip install -r requirements.txt

3. Configura Redis:

    Asegúrate de que Redis esté corriendo en `localhost` en el puerto `6379`.

4. Corre la aplicación:

    uvicorn app.main:app --reload

5. Accede a la aplicación:

    [uvicorn app.main:app --reload](http://127.0.0.1:8000)

6. Corre los tests:

    pytest --disable-warnings


### Dockerización
Si prefieres usar Docker:

1. Construye la imagen:

    docker build -t microblogging .

2. Corre el contenedor:

    docker run -p 8000:8000 microblogging

    Abre el Navegador: http://127.0.0.1:8000
    Para ver la documentacion de la API: http://127.0.0.1:8000/docs

3. Si prefieres correr Redis y la API juntos usando docker-compose:

Crea un archivo docker-compose.yml:

version: "3.8"
services:
  redis:
    image: redis:alpine
    container_name: redis
    ports:
      - "6379:6379"

  microblogging-api:
    build: .
    container_name: microblogging
    ports:
      - "8000:8000"
    depends_on:
      - redis

Inicia ambos servicios con:

docker-compose up --build

Accede a la API en: http://localhost:8000.


## Endpoints Disponibles

### Usuarios
- **Seguir a un usuario:** `POST /api/v1/users/{user_id}/follow/{follow_id}`
- **Obtener usuarios seguidos:** `GET /api/v1/users/{user_id}/following`

### Tweets
- **Publicar un tweet:** `POST /api/v1/tweets`
- **Obtener tweets de un usuario:** `GET /api/v1/tweets/{user_id}`

### Timeline
- **Ver el timeline:** `GET /api/v1/users/{user_id}/timeline?page={page}&page_size={page_size}`



## 🌐 Arquitectura

### Diagrama

La arquitectura consiste en:
1. **Usuarios** que interactúan con la API.
2. **FastAPI** como la capa de servicio que procesa las solicitudes y maneja la lógica de negocio.
3. **Redis** como la base de datos en memoria, utilizada para almacenamiento y recuperación rápida de datos como tweets y relaciones de usuarios.

El diseño está optimizado para manejar altos volúmenes de tráfico y rapidez en la respuesta.

La API utiliza Redis para el almacenamiento en memoria de los tweets y las relaciones entre usuarios. Esto permite consultas rápidas y eficientes. Además, el diseño modular asegura que sea fácil de mantener y escalar.

Por ello, Redis se configura con dos bases de datos separadas:

Base de datos principal: Utilizada por los servicios en producción para manejar las operaciones normales (guardar un tweet, obtener tweets de un usuario, añadir a un usuario a la lista de seguidos, obtener la lista de usuarios seguidos, ordenar cronológicamente los tweets de los usuarios que un usuario sigue).
Base de datos de pruebas: Exclusivamente para los tests unitarios, garantizando que los datos de producción no sean afectados durante las pruebas.
Este enfoque asegura una separación clara entre el entorno de producción y las pruebas, evitando conflictos y permitiendo que las pruebas se ejecuten en un entorno limpio.

### Justificación de Redis
- **Ventajas:**
    - Baja latencia para operaciones.
    - Escalabilidad horizontal: Redis permite crecer horizontalmente para soportar millones de usuarios y datos en tiempo real
    - Manejo eficiente de estructuras de datos complejas como listas y conjuntos.

---
## Autor

[Flor87Posta](https://github.com/Flor87Posta)
---


