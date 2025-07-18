import os
import re

def extract_keywords(text):
    stopwords = set(['the', 'and', 'a', 'in', 'of', 'to', 'is', 'for', 'on', 'that'])
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}
    for w in words:
        if w not in stopwords:
            freq[w] = freq.get(w, 0) + 1
    return sorted(freq.items(), key=lambda x: -x[1])[:10]

def organize_notes(directory, output_file):
    results = []
    for fname in os.listdir(directory):
        if fname.endswith('.txt'):
            with open(os.path.join(directory, fname), 'r') as f:
                text = f.read()
            keywords = [k[0] for k in extract_keywords(text)]
            results.append({
                'filename': fname,
                'keywords': ', '.join(keywords),
                'summary': text[:500]
            })
    with open(output_file, 'w') as f:
        for entry in results:
            f.write(f"File: {entry['filename']}\n")
            f.write(f"Keywords: {entry['keywords']}\n")
            f.write(f"Summary: {entry['summary']}\n\n")

if __name__ == "__main__":
    organize_notes('meeting_notes', 'organized_notes.txt')

