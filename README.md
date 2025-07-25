# Prodigy InfoTech Internship - Task 03: Text Generation with Markov Chains

## 🎯 Task Objective

Build a simple **text generation algorithm using Markov Chains**. This project involves creating a statistical model that learns word sequences from existing literature and generates new, coherent sentences based on those patterns.

---

## 📄 What I Did

- Used **Markovify** to generate text from classical literature
- Cleaned and preprocessed text using **NLTK**, **spaCy**, and **Regex**
- Loaded Shakespeare plays from the NLTK Gutenberg corpus
- Created a Markov model with a state size of 3
- Generated full and short sentences based on learned patterns

---

## 📚 Dataset Used

- `shakespeare-hamlet.txt`
- `shakespeare-macbeth.txt`
- `shakespeare-caesar.txt`

(All three sourced from the NLTK Gutenberg Corpus)

---

## ⚙️ How It Works

1. Load Shakespeare texts using `nltk.corpus.gutenberg`
2. Clean and preprocess text using regex
3. Segment text into sentences using spaCy
4. Train a Markov chain model (`state_size=3`) using Markovify
5. Generate new text based on learned sentence structure

---

## 🧠 Example Output

📜 Full Sentences:
- He comes before you with the king!
- My father is dead?

✂️ Short Sentences:
- They are but toys.
- Farewell, my lord.

> *(Results will vary with each run)*

---

## 🛠️ Tech Stack

- Python
- Markovify
- NLTK
- spaCy
- Regex
- Google Colab or local Python environment

---

## 📁 Folder Structure
