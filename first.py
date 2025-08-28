import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyAjxcWvjDxmvyy_bJWh6z54Vgusr3yMh-Y")

model=genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={
        "temperature":0.5,
        "max_output_tokens":5
    }
    
    )

def sentiment_anylsis(text):
    messages=f"You are a sentiment analysis assistant. Your task is to read the user's input text and classify its sentiment as Positive, Negative, or Neutral. Respond only with the sentiment label without extra explanation.: {text}"
    
    response=model.generate_content(
       messages
    )

    response_text=response.text.strip()

    return response_text

# while True:
#     choice = input("Do you want to continue sentiment analysis (yes/no): ").lower()
    
#     if choice == "yes":
#         user_text = input("Enter the text here: ")
#         sentiment =sentiment_anylsis(user_text)
#         print(f"{user_text} --> the sentiment is {sentiment}\n")
#     else:
#         print("Exiting sentiment analysis. Goodbye! 👋")
#         break


st.title("📝 Sentiment Analysis with Gemini")
st.write("Enter text below to analyze sentiment (Positive / Negative / Neutral).")

# Text input
user_text = st.text_area("Enter your text:")

if st.button("Analyze Sentiment"):
    if user_text.strip() != "":
        sentiment = sentiment_anylsis(user_text)
        st.success(f"**Sentiment:** {sentiment}")
    else:
        st.warning("⚠️ Please enter some text first.")

# Optionally allow continuous analysis
st.write("---")
st.write("Tip: You can analyze multiple texts one by one by typing and clicking 'Analyze Sentiment'.")

