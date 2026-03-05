import fitz

def extract(filename, outfile):
    doc = fitz.open(filename)
    text = ""
    for page in doc:
        text += f"\n=== PAGE {page.number + 1} ===\n"
        text += page.get_text()
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Done: {outfile}")

if __name__ == "__main__":
    extract("Latex con el aval.pdf", "extracted_aval.txt")
    extract("TD_Oscar_Pacheco - Videojuego de Estrategia en Tiempo Real para Contribuir a la Promoción de los ODS.pdf", "extracted_oscar.txt")
