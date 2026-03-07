#!/usr/bin/env python3
"""
Script para corregir los captions de longtable que tienen } \\ en lugar de }} \\
"""

import re

def fix_captions(content):
    """
    Corrige los captions de longtable mal formados.
    Busca: \caption{...}\label{...} \\
    Reemplaza por: \caption{...}\label{...}} \\
    """
    
    # Patrón para encontrar captions mal formados
    # Busca: \caption{texto}\label{id} \\
    # Debe ser: \caption{texto}\label{id}} \\
    pattern = r'(\\caption\{[^}]+\}\\label\{[^}]+\}) \\\\'
    
    def replace_caption(match):
        caption_and_label = match.group(1)
        return caption_and_label + '} \\\\'
    
    # Aplicar corrección
    fixed = re.sub(pattern, replace_caption, content)
    
    return fixed


def process_file(filename):
    """Procesa un archivo .tex y corrige los captions."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        fixed_content = fix_captions(content)
        
        # Guardar el archivo corregido
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✓ Archivo {filename} corregido exitosamente")
        return True
        
    except Exception as e:
        print(f"✗ Error procesando {filename}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python fix_captions.py <archivo.tex>")
        sys.exit(1)
    
    filename = sys.argv[1]
    process_file(filename)
