# CourseWork_Text_Readability

This project focuses on predicting the **readability level of English texts** using linguistic features and machine learning models. The goal is to approximate the **Lexile Band** score with open data and calculated text metrics.

---

## Overview

The project analyzes English text complexity based on linguistic characteristics such as:

* Average sentence and word length
* Vocabulary richness
* Syllables per word
* Ratios of nouns, verbs, and adjectives
* Punctuation and conjunction frequency
* Classical readability indices (Flesch, SMOG, Dale–Chall, Gunning Fog, etc.)

These features are used to train models that estimate the text’s readability level.

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/BL-IMPO/CourseWork_Text_Readability.git
cd CourseWork_Text_Readability
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate       # Windows  
# or  
source .venv/bin/activate    # macOS/Linux  
pip install -r requirements.txt
```

3. Download NLTK data:

```bash
python src/nltk_downloads.py
```

---

## Models

The following models were trained and compared:

* Linear Regression
* Random Forest
* XGBoost
* Multilayer Perceptron (NN)

| Model             | MAE  | RMSE | R²   |
| ----------------- | ---- | ---- | ---- |
| Linear Regression | 0.34 | 0.20 | 0.80 |
| Random Forest     | 0.31 | 0.17 | 0.83 |
| XGBoost           | 0.31 | 0.17 | 0.83 |
| Neural Network    | 0.31 | 0.41 | 0.83 |

The **XGBoost** model achieved the best performance overall.

---

## Dataset

The project is based on the **CLEAR Corpus (CommonLit Ease of Readability)**, which contains text excerpts labeled with readability scores, including Lexile Band.

---

## Author

**Durnev Nikita Alekseevich**
GitHub: [BL-IMPO](https://github.com/BL-IMPO)

---
