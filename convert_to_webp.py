#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from PIL import Image

def get_image_files(directory):
    """
    Retorna la lista de archivos que se consideran imágenes
    por su extensión y no son .webp.
    """
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}
    image_files = []
    for file_name in os.listdir(directory):
        _, ext = os.path.splitext(file_name.lower())
        if ext in valid_extensions:
            image_files.append(file_name)
    return image_files

def convert_images_to_webp(directory):
    """
    Convierte todos los archivos de imagen soportados a formato WebP
    sin pérdida de calidad, usando Pillow.
    """
    image_files = get_image_files(directory)
    if not image_files:
        print("No se encontraron imágenes para convertir.")
        return

    for file_name in image_files:
        try:
            input_path = os.path.join(directory, file_name)
            output_name = os.path.splitext(file_name)[0] + ".webp"
            output_path = os.path.join(directory, output_name)

            with Image.open(input_path) as img:
                # Convertir a modo que soporte WebP si es necesario (ej. RGBA)
                img = img.convert("RGBA")
                # Guardar como WebP en modo sin pérdida
                img.save(output_path, "webp", lossless=True)
                print(f"Convertido: {file_name}  ->  {output_name}")
        except Exception as e:
            # Manejo robusto de errores, continúa con el siguiente archivo
            print(f"Ocurrió un error al procesar {file_name}: {e}")

def main():
    """
    Función principal que llama a la conversión de imágenes en el directorio actual.
    """
    current_directory = os.path.abspath(os.path.dirname(__file__))
    convert_images_to_webp(current_directory)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        sys.exit(1)
