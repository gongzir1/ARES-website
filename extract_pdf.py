import sys
try:
    from pypdf import PdfReader
    reader = PdfReader("final.pdf")
    text = ""
    # Extract the first 5 pages to get the title, authors, abstract, and introduction
    for i in range(min(5, len(reader.pages))):
        text += reader.pages[i].extract_text() + "\n"
    with open("pdf_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully extracted first 5 pages.")
except Exception as e:
    print(f"Error: {e}")
