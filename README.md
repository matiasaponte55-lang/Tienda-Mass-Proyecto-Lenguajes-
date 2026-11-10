# Tienda Mass - Avance de Proyecto

Sistema web de comercio electrónico y control de pedidos para **Tiendas Mass** desarrollado en **Python** y **Django**, conectado a base de datos **PostgreSQL**.

---

## 📋 Requisitos Previos

- **Python 3.10** o superior
- **PostgreSQL 14** o superior con la base de datos `MassTienda` configurada
- Dependencias indicadas en `requirements.txt`

---

## 🚀 Puesta en Marcha Rápida

### 1. (Opcional) Crear y activar entorno virtual:
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 3. Base de Datos:
En la carpeta `backup_BD/` encontrarás los respaldos de la base de datos:
- `MassTienda_backup.sql` (volcado SQL completo para pgAdmin o psql)
- `backup_MassTienda.json` (respaldo en formato JSON de Django)

Si ya tienes la BD `MassTienda` creada en PostgreSQL:
```bash
python manage.py migrate
```

### 4. Iniciar el Servidor:
```bash
python manage.py runserver
```
Accede desde tu navegador en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👤 Credenciales de Acceso

- **Administrador:**
  - **Usuario:** `admin`
  - **Contraseña:** `admin123`
  - *(Acceso directo al panel de control, inventario, reportes y entregas)*

- **Clientes:**
  - Registro libre desde la página web o usando el login unificado.
