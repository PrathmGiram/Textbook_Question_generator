# 📚 Textbook-to-Quiz Generator (AI-Powered)

A lightweight web application that transforms textbook chapters (PDFs) into **intelligent quiz questions** using NLP and Hugging Face's T5 model. Designed for educators, students, and EdTech innovators.

---

## 🚀 Features

- 📄 Upload any textbook chapter (PDF)
- 🤖 Automatically generate relevant questions
- 🎨 Clean and responsive Gradio UI
- 🧠 NLP pipeline powered by Hugging Face Transformers
- 📦 Portable & easy to extend for MCQs, tagging, or export

---

## 🛠 Tech Stack

- Python 3.8+
- [Gradio](https://gradio.app/) - for interactive web UI
- [Hugging Face Transformers](https://huggingface.co/models)
- PDF parsing with PyMuPDF or pdfplumber
- Regex and text preprocessing

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/textbook-to-quiz-ai.git
cd textbook-to-quiz-ai
pip install -r requirements.txt
