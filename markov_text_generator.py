import nltk
import spacy
import re
import markovify
from nltk.corpus import gutenberg
import warnings

warnings.filterwarnings("ignore")

# Download necessary data
nltk.download('gutenberg')
nlp = spacy.load("en_core_web_sm")

# Load Shakespeare's texts
hamlet = gutenberg.raw('shakespeare-hamlet.txt')
macbeth = gutenberg.raw('shakespeare-macbeth.txt')
caesar = gutenberg.raw('shakespeare-caesar.txt')

# Clean text
def text_cleaner(text):
    text = re.sub(r'--', ' ', text)
    text = re.sub(r'\[\[.*?\]\]', '', text)
    text = re.sub(r'(b|s+-?|^-?)(\d+|\d*\.\d+)\b', '', text)
    text = ' '.join(text.split())
    return text

hamlet = re.sub(r'Chapter \d+', '', hamlet)
macbeth = re.sub(r'Chapter \d+', '', macbeth)
caesar = re.sub(r'Chapter \d+', '', caesar)

hamlet = text_cleaner(hamlet)
macbeth = text_cleaner(macbeth)
caesar = text_cleaner(caesar)

# Sentence segmentation using spaCy
def extract_sentences(text):
    doc = nlp(text)
    return ' '.join([sent.text for sent in doc.sents if len(sent.text) > 1])

hamlet_sents = extract_sentences(hamlet)
macbeth_sents = extract_sentences(macbeth)
caesar_sents = extract_sentences(caesar)

# Combine all texts
shakespeare_sents = hamlet_sents + macbeth_sents + caesar_sents

# Create the Markov model
generator = markovify.Text(shakespeare_sents, state_size=3)

# Generate full sentences
print("\n📜 Full Sentences:")
for i in range(5):
    print("-", generator.make_sentence())

# Generate short sentences
print("\n✂️ Short Sentences (under 100 chars):")
for i in range(5):
    print("-", generator.make_short_sentence(100))
