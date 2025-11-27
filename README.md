
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

## Cargar datos iniciales

Ejecuta el script poblar_datos.py para llenar la base de datos:
python manage.py shell
>>> exec(open('poblar_datos.py').read())
[![Captura-de-pantalla-2025-10-21-184756.png](https://i.postimg.cc/Qt9MmT67/Captura-de-pantalla-2025-10-21-184756.png)](https://postimg.cc/gXpdknbc)

## Capturas de pantalla
### Admin:
[![Captura-de-pantalla-2025-10-21-183612.png](https://i.postimg.cc/kGP7yhRC/Captura-de-pantalla-2025-10-21-183612.png)](https://postimg.cc/BLNWSpC7)

### Author
[![Captura-de-pantalla-2025-10-21-182035.png](https://i.postimg.cc/QtGLLK87/Captura-de-pantalla-2025-10-21-182035.png)](https://postimg.cc/1gH7wtNR)

### Book
[![Captura-de-pantalla-2025-10-21-183418.png](https://i.postimg.cc/cJjxvJsx/Captura-de-pantalla-2025-10-21-183418.png)](https://postimg.cc/gwVF5mXQ)

### Review
[![Captura-de-pantalla-2025-10-21-183542.png](https://i.postimg.cc/hj9kK4vr/Captura-de-pantalla-2025-10-21-183542.png)](https://postimg.cc/S2xTrhW2)

### Codigo DRF
[![Captura_de_pantalla_2025_11_27_172623.png](https://i.postimg.cc/gcTXwtHG/Captura_de_pantalla_2025_11_27_172623.png)](https://postimg.cc/w3DTZVrr)

[![Captura_de_pantalla_2025_11_27_172604.png](https://i.postimg.cc/mZ5zcpy2/Captura_de_pantalla_2025_11_27_172604.png)](https://postimg.cc/xqLThRZW)

[![Captura_de_pantalla_2025_11_27_172555.png](https://i.postimg.cc/L6gqjkx6/Captura_de_pantalla_2025_11_27_172555.png)](https://postimg.cc/561NVzcZ)

[![Captura_de_pantalla_2025_11_27_172518.png](https://i.postimg.cc/wTRtD5wz/Captura_de_pantalla_2025_11_27_172518.png)](https://postimg.cc/QHsx37LY)

### API
[![Captura_de_pantalla_2025_11_27_170252.png](https://i.postimg.cc/28Lqnd0Q/Captura_de_pantalla_2025_11_27_170252.png)](https://postimg.cc/9rVFh950)

[![Captura_de_pantalla_2025_11_27_171117.png](https://i.postimg.cc/dV02MZ6K/Captura_de_pantalla_2025_11_27_171117.png)](https://postimg.cc/crVgwHPD)

[![Captura_de_pantalla_2025_11_27_171022.png](https://i.postimg.cc/13zGxVBX/Captura_de_pantalla_2025_11_27_171022.png)](https://postimg.cc/QHR91tRZ)

[![Captura_de_pantalla_2025_11_27_170851.png](https://i.postimg.cc/CxKGyn7K/Captura_de_pantalla_2025_11_27_170851.png)](https://postimg.cc/ykwgcdwq)