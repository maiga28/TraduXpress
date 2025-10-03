import os
from django.shortcuts import render
from googletrans import Translator
from .forms import UploadFileForm
from PyPDF2 import PdfReader
import docx

def extract_text_from_file(file):
    ext = os.path.splitext(file.name)[1].lower()
    text = ""

    if ext == ".txt":
        text = file.read().decode("utf-8")

    elif ext == ".docx":
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif ext == ".pdf":
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

    elif ext == ".doc":
        text = "⚠️ Format .doc non supporté directement. Convertis-le en .docx."
    else:
        text = "❌ Format non supporté."

    return text


def translate_file(request):
    translated_text = None
    original_text = None

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            target_lang = form.cleaned_data["target_lang"]

            # Extraire le texte
            original_text = extract_text_from_file(file)

            # Traduire
            translator = Translator()
            translated = translator.translate(original_text, dest=target_lang)
            translated_text = translated.text

    else:
        form = UploadFileForm()

    return render(request, "translator/translate.html", {
        "form": form,
        "original_text": original_text,
        "translated_text": translated_text
    })
