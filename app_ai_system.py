import streamlit as st
from transformers import pipeline


st.set_page_config(page_title="Restaurant Review Analyzer", layout="centered")
st.title("Restaurant Review Analyzer")
st.write("Analyze restaurant reviews by AI models")

@st.cache_resource
def load_models():
    sentiment_model=pipeline("text-classification",model="karimbkh/BERT_fineTuned_Sentiment_Classification_Yelp")
    topic_model=pipeline("zero-shot-classification",model="facebook/bart-large-mnli")
    return sentiment_model,topic_model

sentiment_model, topic_model=load_models()

candidate_labels=["Food Quality","Service","Price","Cleanliness","Atmosphere","Location","Waiting Time"]

st.subheader("Enter a Restaurant Review")

review=st.text_area("Write your review:",placeholder="Enter your restaurant review here...")

analyze=st.button("Analyze Review")


if analyze:
    if review.strip() == "":
        st.warning("Please enter a restaurant review.")
    else:
        sentiment_result = sentiment_model(review)[0]
        topic_result = topic_model(
            review,
            candidate_labels=candidate_labels
        )

        sentiment_label = sentiment_result["label"]

        if sentiment_label == "LABEL_1":
            sentiment_label = "POSITIVE"
        elif sentiment_label == "LABEL_0":
            sentiment_label = "NEGATIVE"

        st.subheader("Analysis Results")
        st.write("**Sentiment:**", sentiment_label)
        st.write("**Confidence:**", round(sentiment_result["score"] * 100, 2), "%")
        st.write("**Top 3 Review Topics:**")
        for label, score in zip(
            topic_result["labels"][:3],
            topic_result["scores"][:3]
        ):
            st.write(f"- **{label}:** {round(score * 100, 2)}%")
