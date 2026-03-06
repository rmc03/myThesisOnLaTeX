import fitz
import sys

def extract_pdf(pdf_path, output_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num, page in enumerate(doc, 1):
            text += f"\n\n--- PAGE {page_num} ---\n\n"
            text += page.get_text()
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        
        print(f"Successfully extracted {len(doc)} pages from {pdf_path}")
        print(f"Output saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
        return False

if __name__ == "__main__":
    # Extract both reference PDFs
    print("Extracting 'Latex con el aval.pdf'...")
    extract_pdf("Latex con el aval.pdf", "extracted_latex_aval.txt")
    
    print("\nExtracting 'TD_Oscar_Pacheco - Videojuego de Estrategia en Tiempo Real para Contribuir a la Promoción de los ODS.pdf'...")
    extract_pdf("TD_Oscar_Pacheco - Videojuego de Estrategia en Tiempo Real para Contribuir a la Promoción de los ODS.pdf", "extracted_oscar_thesis.txt")
    
    print("\nExtraction complete!")
