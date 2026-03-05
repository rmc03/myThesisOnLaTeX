import fitz

def extract():
    doc = fitz.open("tesis_capitulos_1_2.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    extract()
