# Convertidor de Imágenes a WebP

## Índice

1. [Descripción](https://www.notion.so/1906597925398043a0ace4749dd45eff?pvs=21)
2. [Características](https://www.notion.so/1906597925398043a0ace4749dd45eff?pvs=21)
3. [Requisitos](https://www.notion.so/1906597925398043a0ace4749dd45eff?pvs=21)
4. [Instalación](https://www.notion.so/1906597925398043a0ace4749dd45eff?pvs=21)
5. [Dependencias de Python](https://www.notion.so/1906597925398043a0ace4749dd45eff?pvs=21)
6. [Uso](https://www.notion.so/1906597925398043a0ace4749dd45eff?pvs=21)
7. [Contribuciones](https://www.notion.so/1906597925398043a0ace4749dd45eff?pvs=21)
8. [Licencia](https://www.notion.so/1906597925398043a0ace4749dd45eff?pvs=21)

---

## Descripción

Este script **Open-Source** convierte automáticamente todas las imágenes de un directorio (soportadas por Pillow) al formato **WebP** sin pérdida de calidad. Ideal para optimizar imágenes manteniendo la calidad original.

El script escanea el directorio actual, identifica archivos con extensiones comunes (como `.jpg`, `.png`, `.bmp`, etc.) y los convierte a WebP (excepto aquellos que ya están en este formato).

> Repositorio: convertidor-imagenes-webp
> 
> 
> *(MIT License)*
> 

---

## Características

1. **Detección Automática de Imágenes**
    - Identifica archivos de imagen por sus extensiones válidas (jpg, jpeg, png, bmp, gif, tiff).
2. **Conversión a WebP sin Pérdida**
    - Utiliza Pillow para convertir las imágenes al formato WebP en modo lossless, manteniendo la calidad original.
3. **Manejo Robusto de Errores**
    - Si ocurre un error durante la conversión de alguna imagen, el script lo reporta y continúa con las demás.
4. **Fácil de Ejecutar**
    - Se ejecuta sobre el directorio actual sin necesidad de argumentos adicionales.

---

## Requisitos

### Dependencias de Python

- **Python 3** (versión >= 3.6)
- **Pillow**

---

## Instalación

### 1. Clonar el Repositorio

```bash
git clone <https://github.com/tu-usuario/convertidor-imagenes-webp.git>
cd convertidor-imagenes-webp
```

### 2. Crear y Activar un Entorno Virtual (Opcional pero Recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias de Python

```
pip install Pillow
```

Luego, instala las dependencias:

---

## Uso

1. **Ubica el Script en el Directorio Deseado**
    
    El script procesará todas las imágenes del directorio actual.
    
2. **Ejecuta el Script**
    
    ```bash
    python convert_to_webp.py
    ```
    
3. **Resultado**
    
    Cada imagen soportada se convertirá a formato WebP, y se guardará en el mismo directorio con la extensión `.webp`.
    

---

## Contribuciones

¡Contribuciones son bienvenidas! Si deseas mejorar este proyecto, por favor sigue estos pasos:

1. **Fork** el repositorio.
2. Crea una nueva **rama** (`git checkout -b feature/nueva-característica`).
3. **Commit** tus cambios (`git commit -m 'Añadir nueva característica'`).
4. **Push** a la rama (`git push origin feature/nueva-característica`).
5. Abre un **Pull Request**.

Asegúrate de seguir las mejores prácticas de código y documentación.
