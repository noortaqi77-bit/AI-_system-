 # Restaurant Review Analyzer

## 1. Problem Definition

The goal of this project is to analyze restaurant reviews using pretrained AI models.

The system performs two tasks:

- **Sentiment Classification:** Classifies each review as Positive or Negative.
- **Topic Classification:** Identifies the main topic of each review from seven categories: Food Quality, Service, Price, Cleanliness, Atmosphere, Location, and Waiting Time.

The project investigates and compares pretrained models to determine their suitability for analyzing restaurant reviews.

## APP :

(https://ml4prrvmelmy4appk3aadqm.streamlit.app/)

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


### 2.5 Initial Inference Results
Model 1 labels are LABEL_0 (negative) and LABEL_1 (positive). On “The food was amazing but the service was awful.” Model 1 predicted LABEL_0 (0.62), Model 2 predicted NEGATIVE (0.99) and Model 3 predicted negative (0.92). On “Okay.” Model 1 predicted LABEL_1 (0.57), Model 2 predicted POSITIVE (0.9998) and Model 3 predicted neutral (0.48). I think binary models are forced to pick a side on neutral text.

### 2.6 Evaluation

The models were evaluated using the following metrics: (Accuracy, Macro Precision, Macro Recall, Macro F1-score, Inference Time)

These metrics were used to compare classification performance and prediction speed across the three models.

### 2.7 Error Analysis

Ten failure cases were selected to compare the three models and understand their classification errors.

| Model | Main Failure Patterns |
|---|---|
| Model 1 – Yelp BERT | Struggled with indirect negative reviews and sometimes predicted Positive with high confidence. |
| Model 2 – DistilBERT | Misclassified positive expressions within negative reviews, sometimes with very high confidence. |
| Model 3 – XLM-RoBERTa | Struggled with short reviews and sometimes predicted Neutral on the binary dataset. |

Only one review (row 51) was misclassified by all three models, suggesting that some reviews are difficult to classify because of their wording and context.

The analysis showed that high confidence does not always mean a correct prediction.

### 2.8 Model Comparison

| Model | Accuracy | Negative F1 | Positive F1 | Macro F1 (POS/NEG) | Errors | Inference Time |
|---|---:|---:|---:|---:|---:|---:|
| Yelp BERT | 93% | 0.923 | 0.936 | 0.929 | 7 | 31.37s |
| DistilBERT | 92% | 0.918 | 0.922 | 0.920 | 8 | 12.25s |
| XLM-RoBERTa | 90% | 0.909 | 0.935 | 0.922 | 10 | 11s |


## 3. Task B – Zero Shot Classification

### 3.1 Data Collection

The dataset `bahrain_restaurant_reviews_balanced_35.csv` contains 35 English restaurant reviews from Bahrain.

The reviews are divided equally into seven categories, with 5 reviews per category: Food Quality, Service, Price , Cleanliness , Atmosphere, Location , Waiting Tim

### 3.2 Model Selection

Two pretrained models were selected for zero-shot classification:

1. `facebook/bart-large-mnli`: Selected to classify reviews into the seven categories without additional training.
2. `MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli`: Selected to compare BART with a smaller multilingual model.

### 3.3 Model Card Investigation

| Information | BART-large-MNLI | Multilingual MiniLM |
|---|---|---|
| Architecture | BART-large | Multilingual MiniLMv2 |
| Training Data | MultiNLI | MultiNLI and XNLI |
| Language | English | 100+ languages |
| Parameters | 400M | Approximately 117M |
| License | MIT | MIT |

Both models were tested using the review "Found this great place while walking the back streets of Manama. It’s near or in the souk." BART predicted Location with 57% confidence, while MiniLM predicted Location with 72% confidence. Both models identified the correct topic, but MiniLM gave a higher confidence score.

### 3.4 Model Evaluation

| Model | Accuracy | Macro F1 | Errors |
|---|---:|---:|---:|
| BART-large-MNLI | 77.14% | 74.4% | 8 |
| Multilingual MiniLM | 65.71% | 60.7% | 12 |

### 3.5 Model Comparison

BART achieved better results than MiniLM, with 77.14% accuracy and 74.4% Macro F1, compared to 65.71% accuracy and 60.7% Macro F1. MiniLM was faster (4.75 seconds) and smaller, but BART classified restaurant reviews more accurately. Since this project focuses on English restaurant reviews in Bahrain, I recommend BART because classification performance is more important than multilingual support.

### 3.6 Error Analysis

BART made 8 classification errors out of 35 reviews. It mainly confused Atmosphere with Location and Service with Waiting Time. It also struggled with reviews that mentioned more than one topic, such as food quality and service. For example, a review about friendly staff and good food was classified as Food Quality instead of Service.

## Limitations

The project has some limitations. The datasets are small, with only 100 reviews for Task A and 35 reviews for Task B. The models may also struggle with short reviews, indirect expressions, mixed sentiments, and reviews that mention multiple topics. The models were tested only on English reviews, so their performance on Arabic reviews is unknown.

## Final Recommendation

For Task A, I recommend Yelp BERT because it achieved the highest accuracy (93%). For Task B, I recommend BART-large-MNLI because it achieved the highest accuracy is 77.14% and Macro F1-score 74.4%. Both models are suitable starting points for the restaurant review analyzer, but more testing is needed before real-world use.

##  Future Work / Fine-Tuning Proposal

In the future, I would collect more restaurant reviews, including Arabic and Bahrain-specific reviews. I would fine-tune the models using domain-specific data to improve their performance. For Task A, I would train the models on more reviews with positive and negative labels. For Task B, I would use reviews labeled with the seven restaurant categories. I would then compare the fine-tuned models with the original models using the same evaluation metrics.
