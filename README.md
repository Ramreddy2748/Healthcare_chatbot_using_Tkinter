## Healthcare Chatbot 

This is a Python-based project for dealing with human symptoms and predicting their possible outcomes.

#### Project Goal
The primary goal of this project is to forecast the disease so that patients can get the desired output according to their primary symptoms. 

## Technology used
We used **[TKinter](https://docs.python.org/3/library/tkinter.html)** to create a **desktop-based application** and **[Spacy](https://spacy.io/)** for NLP-based processes like ***text sentence tokenization and lemmatization***, and we used a **[Huggingface](https://huggingface.co/)** pretrained model to extrat disease names from a given sentence ***( or ner processing)***.


#### Huggingface
Downloading pre-trained model from [Huggingface Model](https://huggingface.co/raynardj/ner-disease-ncbi-bionlp-bc5cdr-pubmed)


#### Spacy  [[for NLP-based processes]]

Download [spacy](https://spacy.io/usage) For window, Linux, MacOS

```bash
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```


## Installation Steps

--> Navigate to Project Directory

## create a new environment
--> python3.9 -m venv myenv

## activate environment
--> source myenv/bin/activate

## install the requirements
--> pip install -r requirements.txt 



## Output images








