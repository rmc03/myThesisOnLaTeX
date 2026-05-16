# Videojuego educativo para la enseñanza de los Objetivos de Desarrollo Sostenible

![LaTeX](https://img.shields.io/badge/LaTeX-47494E?style=for-the-badge&logo=latex&logoColor=white)
![Build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![Academic](https://img.shields.io/badge/tipo-Tesis_de_Grado-blue?style=for-the-badge)

Repositorio que contiene el código fuente en LaTeX del trabajo de diploma (tesis) titulado **"Videojuego educativo para la enseñanza de los Objetivos de Desarrollo Sostenible"**, focalizado en el diseño, arquitectura y desarrollo del videojuego interconectado *Go Goals! Digital*.

## 📑 Resumen

El desconocimiento generalizado sobre los Objetivos de Desarrollo Sostenible (ODS) de las Naciones Unidas dificulta la participación activa en la Agenda 2030 y limita la toma de decisiones informadas. Promover un conocimiento profundo de estos 17 objetivos es crucial para mejorar la calidad de vida y fomentar el desarrollo equitativo. 

En este contexto, este trabajo de diploma expone el proceso metodológico e ingenieril utilizado para la construcción de una solución digital gamificada apoyada en el motor gráfico **Godot Engine**. Haciendo uso de la metodología ágil **Extreme Programming (XP)**, la arquitectura de software propuesta provee una plataforma interactiva que facilita el Aprendizaje Basado en Juegos (ABJ) para usuarios de todas las edades con alta fiabilidad, escalabilidad teórica y robustez.

## 📂 Estructura del Repositorio

El proyecto de redacción obedece a un estándar modular para propiciar mantenibilidad al realizar compilaciones en LaTeX:

- `example.tex` / `thesis.cls` - Punto de entrada principal y clase compiladora del documento.
- `Chapter1.tex` - Fundamentación teórica sobre gamificación, ODS y la pertinencia de los videojuegos en la educación básica.
- `Chapter2.tex` - Despliegue de la ingeniería de software: Requisitos funcionales, correspondencia exacta con 18 Historias de Usuario, Tarjetas CRC, Arquitectura del Videojuego y 10 Tareas de Ingeniería medulares.
- `Chapter3.tex` - Diseño y ejecución de pruebas de calidad al software terminado.
- `Conclusions.tex` & `Suggestions.tex` - Conclusiones científicas y recomendaciones a futuro.
- `Images/` - Conjunto de diagramas, prototipos e imágenes que respaldan la ejecución metodológica.

## 🚀 Requisitos y Compilación

Para compilar el documento en formato PDF desde terminal de manera local, se requiere:

1. **Distribución completa de LaTeX**: TexLive (Linux/Mac) o MiKTeX (Windows).
2. Opcional pero recomendado: un editor como **TeXstudio** o la extensión **LaTeX Workshop** en VS Code.

**Comandos rápidos de compilación:**
```bash
pdflatex example.tex
biber example        # (Para procesar y unificar métricas de bibliografía)
pdflatex example.tex
pdflatex example.tex
```

## 🛠 Entorno de Investigación y Herramientas Evaluadas
- **Metodología Ágil**: Extreme Programming (XP)
- **Frameworks de diseño**: Patrones GRASP, Gang of Four (GoF)
- **Producción lógica referida**: Godot Engine (GDScript)
- **Gestión bibliométrica documental**: LaTeX (BibLaTeX)

## 🖋️ Autoría y Reconocimientos

* **Autor:** Ruslan Alexei Martinez Campos
* **Institución:** Facultad de Tecnologías Interactivas
* **Tutores:**
  * P.T., Ing. Juan Antonio Plasencia Soler, Dr. C.
  * Ing. Oscar de Jesús Pacheco del Pino
