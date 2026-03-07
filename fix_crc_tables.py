#!/usr/bin/env python3
# Script para arreglar el formato de las tarjetas CRC

with open('Chapter2.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplazar el patrón problemático
old_pattern = r'''\end{tabular}
\vspace{-\baselineskip}
\begin{tabular}{|p{0.25\textwidth}|p{0.64\textwidth}|}
\hline
\textbf{Clase:}'''

new_pattern = r'''\end{tabular}
\begin{tabular}{|p{0.25\textwidth}|p{0.64\textwidth}|}
\textbf{Clase:}'''

content = content.replace(old_pattern, new_pattern)

with open('Chapter2.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("Tarjetas CRC arregladas correctamente")
