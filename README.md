# 🐕 DogDex

DogDex es una aplicación web para explorar y conocer distintas razas de perros. Su objetivo es ofrecer un catálogo visual con información sobre el origen, las características físicas, el pelaje y la historia de cada raza.

El proyecto se desarrolla como una aplicación *full stack*, con una API REST en Python y un frontend en React.

## Tecnologías

| Componente              | Tecnología               |
| ----------------------- | ------------------------ |
| Backend                 | Python, FastAPI          |
| Base de datos           | PostgreSQL               |
| ORM                     | SQLAlchemy               |
| Migraciones             | Alembic                  |
| Validación de datos     | Pydantic                 |
| Frontend (planeado)     | React, TypeScript y Vite |
| Pruebas manuales de API | Bruno                    |

## Funcionalidades del backend

* Consulta de razas con búsqueda, filtros y paginación.
* Consulta del detalle de una raza mediante su `slug`.
* Información sobre país de origen, grupo, pelaje, medidas, esperanza de vida e historia.
* Fotografías locales con metadatos de autoría y licencia.
* Importación de razas y fotografías mediante archivos JSON.
* Migraciones de base de datos con Alembic.

## Estructura general

```text
DogDex/
├── backend/
│   ├── alembic/
│   ├── app/
│   │   ├── db/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   └── main.py
│   ├── data/
│   │   ├── breeds.json
│   │   └── breed_images.json
│   ├── scripts/
│   │   ├── import_breeds.py
│   │   └── import_breed_images.py
│   ├── static/
│   │   └── images/
│   │       └── breeds/
│   └── .env
├── frontend/
└── README.md
```

## Cómo iniciar el backend

### 1. Requisitos

Tener instalados Python, PostgreSQL y Git.

Para el desarrollo inicial se utiliza Python 3.9 y PostgreSQL 17.

### 2. Clonar el repositorio

```bash
git clone https://github.com/EdwinAAH/dogdex.git
cd DogDex/backend
```

### 3. Crear y activar el entorno virtual

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar dependencias

Con el entorno virtual activo:

```bash
pip install -r requirements.txt
```

Este comando requiere que el archivo `backend/requirements.txt` exista y contenga las dependencias del proyecto.

### 5. Configurar PostgreSQL

Asegúrate de que PostgreSQL esté ejecutándose y crea la base de datos:

```bash
createdb dogdex_db
```

Si la base de datos ya existe, no es necesario volver a crearla.

### 6. Configurar las variables de entorno

Crea el archivo `backend/.env`:

```env
DATABASE_URL=postgresql+psycopg://TU_USUARIO@localhost:5432/dogdex_db
```

Reemplaza `TU_USUARIO` por tu usuario de PostgreSQL y agrega una contraseña a la URL si tu configuración la requiere.

El archivo `.env` contiene configuración local y no debe subirse a Git.

### 7. Aplicar las migraciones

Desde la carpeta `backend`:

```bash
alembic upgrade head
```

Esto crea o actualiza las tablas necesarias.

### 8. Cargar los datos iniciales

Ejecuta los importadores:

```bash
python -m scripts.import_breeds
python -m scripts.import_breed_images
```

Antes de importar las fotografías, comprueba que los archivos de imagen estén presentes en `backend/static/images/breeds/`.

Los catálogos de países, grupos y tipos de pelaje también deben estar cargados previamente. Consulta los scripts de inicialización disponibles en el proyecto.

### 9. Iniciar el servidor

Desde `backend`, con el entorno virtual activo:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

**http://127.0.0.1:8000**

La documentación interactiva de FastAPI estará disponible en:

**http://127.0.0.1:8000/docs**

## Endpoints principales

| Método | Endpoint                          | Descripción                           |
| ------ | --------------------------------- | ------------------------------------- |
| GET    | `/health`                         | Estado de la API                      |
| GET    | `/health/db`                      | Verificación de conexión a PostgreSQL |
| GET    | `/countries`                      | Consulta de países                    |
| GET    | `/breeds`                         | Catálogo de razas                     |
| GET    | `/breeds/{slug}`                  | Detalle de una raza                   |
| GET    | `/static/images/breeds/{archivo}` | Fotografía de una raza                |

### Ejemplos

Consultar el catálogo:

```http
GET http://127.0.0.1:8000/breeds
```

Buscar una raza:

```http
GET http://127.0.0.1:8000/breeds?search=akita
```

Consultar una ficha individual:

```http
GET http://127.0.0.1:8000/breeds/akita
```

Consultar razas de México:

```http
GET http://127.0.0.1:8000/breeds?country=MX
```

La consulta del catálogo también admite filtros por grupo y tamaño, además de los parámetros `limit` y `offset` para paginación.

## Próximos pasos

* Desarrollar el catálogo visual en React.
* Construir las fichas individuales de las razas.
* Incorporar búsqueda y filtros en la interfaz.
* Agregar pruebas automatizadas y preparar el despliegue.

---

DogDex — Proyecto de desarrollo full stack.
