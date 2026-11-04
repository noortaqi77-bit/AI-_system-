 Restaurant Review Analyzer

## 1. Problem Definition

The goal of this project is to analyze restaurant reviews using pretrained AI models.

The system performs two tasks:

- **Sentiment Classification:** Classifies each review as Positive or Negative.
- **Topic Classification:** Identifies the main topic of each review from seven categories: Food Quality, Service, Price, Cleanliness, Atmosphere, Location, and Waiting Time.

The project investigates and compares pretrained models to determine their suitability for analyzing restaurant reviews.

## 2. Task A – Sentiment Classification

### 2.1 Data Collection

- Dataset:restaurant_reviews_100_huggingface.csv,Contains 100 English restaurant reviews.
- It contain: 53 Positive reviews and 47 Negative reviews.

### 2.2 Data Preparation

The sentiment labels were converted to uppercase (POSITIVE and NEGATIVE) to match the model outputs.

### 2.3 Model Selection

Three pretrained models were selected based on their relevance to sentiment classification:
Three pretrained models: (1) karimbkh/BERT_fineTuned_Sentiment_Classification_Yelp, (2) distilbert/distilbert-base-uncased-finetuned-sst-2-english, (3) cardiffnlp/twitter-xlm-roberta-base-sentiment.
The models were evaluated to identify the most suitable model for restaurant review sentiment classification.

### 2.4 Model Card Investigation

| Model | Architecture | Training Data | Languages | Parameters | License |
|---|---|---|---|---|---|
| BERT Yelp | BERT-base-uncased | Yelp Reviews | English | 110M | MIT |
| DistilBERT SST-2 | DistilBERT-base-uncased | SST-2 | English | 67M | Apache 2.0 |
| Twitter XLM-RoBERTa | XLM-RoBERTa-base | 198M multilingual tweets | 8 languages | 278M | Not specified |









**Task B – Topic Classification:**
- Dataset:bahrain_restaurant_reviews_balanced_35.csv , Contains 35 English restaurant reviews related to restaurants in Bahrain.
- Includes 7 categories, with five reviews per category  ["Food Quality","Service","Price","Cleanliness","Atmosphere","Location","Waiting Time"]
- The dataset was collected and prepared for this experiment.

