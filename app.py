import gradio as gr
from utils import extract_text_from_pdf
from qa_generator import generate_questions, parse_questions

def generate_from_pdf(file):
    pdf_text = extract_text_from_pdf(file.name)
    questions = generate_questions(pdf_text)
    formatted = "\n\n".join([f"👉 **Q{idx+1}:** {q}" for idx, q in enumerate(questions)])
    return formatted

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1 style='text-align: center; color: #2E86C1;'>📚 Textbook-to-Question Generator</h1>")
    gr.Markdown("<p style='text-align: center; font-size: 16px;'>Upload a chapter PDF and generate questions using a Hugging Face model 🤖</p>")

    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="📁 Upload Chapter PDF", file_types=[".pdf"])
        with gr.Column(scale=2):
            output_box = gr.Textbox(label="📝 Generated Questions", lines=20, interactive=False)

    generate_btn = gr.Button("🚀 Generate Questions", variant="primary")

    generate_btn.click(fn=generate_from_pdf, inputs=file_input, outputs=output_box)

demo.launch(share=True)
