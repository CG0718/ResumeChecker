import pymupdf as pmp  # PyMuPDF
import json

def pdf_to_dict(pdf_path):
    try:
        doc = pmp.open(pdf_path)
        data = {
            "filename": pdf_path,
            "total_pages": len(doc),
            "content": []
        }

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            page_data = {
                "page_number": page_num + 1,
                "text": page.get_text().strip()
            }
            data["content"].append(page_data)

        doc.close()
        return data

    except Exception as e:
        return {"error": str(e)}

# 1. Extract the data
file_path = "resume-sample.pdf"#file path to your PDF
pdf_data = pdf_to_dict(file_path)

# 2. Save to JSON file
# 'ensure_ascii=False' keeps the "special" characters as they are 
# instead of turning them into escaped codes like \u2022
with open('text_content.json', 'w', encoding='utf-8') as f:
    json.dump(pdf_data, f, ensure_ascii=False, indent=4)

print('Content saved to text_content.json')