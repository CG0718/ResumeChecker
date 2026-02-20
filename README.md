# ResumeChecker
GenAI for GenZ Challenge 2 | Resume Checker

---

# ResumeChecker

**ResumeChecker** is a Python-based tool designed for the **GenAI for GenZ Challenge 2**. It leverages Generative AI to analyze resumes in PDF format, extract their content, and determine how well they match a specific job description.

## 🚀 Features

* **PDF Extraction:** Automatically reads and parses resume content from PDF files.
* **AI-Powered Matching:** Uses GenAI to compare resume skills and experience against job requirements.
* **Text Compression:** Efficiently processes text data for optimized analysis.

## 📂 Project Structure

* `pdfReader.py`: Handles the extraction of text from PDF documents.
* `Compress_and_Match.py`: The core logic for processing text and calculating the match degree.
* `text_content.json`: Stores processed text data.
* `resume-sample.pdf`: A sample file provided for testing.

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/CG0718/ResumeChecker.git
cd ResumeChecker

```


2. **Install dependencies:**
Make sure you have Python installed. You may need to install libraries for PDF processing (like `PyPDF2`) and your chosen GenAI SDK (e.g., `google-generativeai`).
```bash
pip install pymupdf google-generativeai

```



## 💻 Usage

1. **Prepare your files:** Place the resume PDF you wish to scan in the project directory.
2. **Run the PDF Reader:**
```bash
python pdfReader.py

```


3. **Run the Matcher:**
Execute the matching script to get the analysis results.
```bash
python Compress_and_Match.py

```

