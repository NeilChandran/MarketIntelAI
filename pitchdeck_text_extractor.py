import os
import PyPDF2
from gensim.summarization import summarize

class PitchDeckTextExtractor:
    def __init__(self, directory):
        self.directory = directory
        self.texts = {}

    def extract_text_from_pdf(self, path):
        text = ""
        try:
            with open(path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""
        except Exception as e:
            print(f"Failed on {path}: {e}")
        return text

    def extract_all(self):
        for filename in os.listdir(self.directory):
            if filename.endswith('.pdf'):
                filepath = os.path.join(self.directory, filename)
                text = self.extract_text_from_pdf(filepath)
                if text:
                    self.texts[filename] = text

    def summarize_texts(self):
        summaries = {}
        for fname, text in self.texts.items():
            try:
                summary = summarize(text, word_count=100)
                summaries[fname] = summary
            except Exception as e:
                print(f"Could not summarize {fname}: {e}")
                summaries[fname] = text[:500]
        return summaries

    def save_summaries(self, filename):
        summaries = self.summarize_texts()
        with open(filename, 'w') as f:
            for fname, summary in summaries.items():
                f.write(f"===== {fname} =====\n{summary}\n\n")
        print(f"Saved summaries to {filename}")

if __name__ == "__main__":
    extractor = PitchDeckTextExtractor("pdfs")
    extractor.extract_all()
    extractor.save_summaries("summaries.txt")

