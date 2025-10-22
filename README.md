
# Proyecto Django: Biblioteca

## Instrucciones para ejecutar localmente

### 1. Crear el entorno virtual
python -m venv venv
venv\Scripts\activate

### 2. Instalar dependencias
pip install django

### 3. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

### 4.Crear superusuario
python manage.py createsuperuser

### 5.Ejecutar el servidor
python manage.py runserver

##Cargar datos iniciales

Ejecuta el script poblar_datos.py para llenar la base de datos:
python manage.py shell
>>> exec(open('poblar_datos.py').read())
[![Captura-de-pantalla-2025-10-21-184756.png](https://i.postimg.cc/Qt9MmT67/Captura-de-pantalla-2025-10-21-184756.png)](https://postimg.cc/gXpdknbc)

##Capturas de pantalla
Panel de administración:
[![Captura-de-pantalla-2025-10-21-183612.png](https://i.postimg.cc/kGP7yhRC/Captura-de-pantalla-2025-10-21-183612.png)](https://postimg.cc/BLNWSpC7)
[![Captura-de-pantalla-2025-10-21-182035.png](https://i.postimg.cc/QtGLLK87/Captura-de-pantalla-2025-10-21-182035.png)](https://postimg.cc/1gH7wtNR)
[![Captura-de-pantalla-2025-10-21-183418.png](https://i.postimg.cc/cJjxvJsx/Captura-de-pantalla-2025-10-21-183418.png)](https://postimg.cc/gwVF5mXQ)
[![Captura-de-pantalla-2025-10-21-183542.png](https://i.postimg.cc/hj9kK4vr/Captura-de-pantalla-2025-10-21-183542.png)](https://postimg.cc/S2xTrhW2)