import os
import requests
import streamlit as st

st.set_page_config(page_title="Ghost Story Generator", page_icon="👻")
st.title("👻 Ghost Story Generator")
st.write("Create a spooky story using an open-weight AI model.")

topic = st.text_input("What should your story be about?", placeholder="A haunted house near the sea")
length = st.selectbox("Story length", ["Short", "Medium", "Long"])

if st.button("Generate Story"):
    token = os.getenv("HF_TOKEN", "").strip()
    if not token:
        st.error("Add your Hugging Face access token as the HF_TOKEN environment variable.")
        st.info("Get a token from https://huggingface.co/settings/tokens. Keep it private.")
    elif not topic.strip():
        st.warning("Please enter a story topic first.")
    else:
        prompt = (
            f"Write a {length.lower()} spooky Halloween ghost story about: {topic}. "
            "Use simple English, build suspense, and keep it fictional. "
            "Do not claim the story is real."
        )
        url = "https://router.huggingface.co/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "Qwen/Qwen2.5-3B-Instruct",
            "messages": [
                {"role": "system", "content": "You are a creative spooky fiction writer."},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 600,
            "temperature": 0.8,
        }
        with st.spinner("Writing your story..."):
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=90)
                if response.ok:
                    result = response.json()
                    story = result["choices"][0]["message"]["content"]
                    st.subheader("Your Ghost Story")
                    st.write(story)
                else:
                    st.error(f"The AI service returned status {response.status_code}.")
                    st.caption("Check that your Hugging Face token has access and that this model is available to your account.")
            except requests.RequestException:
                st.error("Could not reach the AI service. Check your internet connection and try again.")
