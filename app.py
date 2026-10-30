import streamlit as st
from groq import Groq

st.set_page_config(page_title="Ghost Story Generator", page_icon="👻")
st.title("👻 Ghost Story Generator")
st.write("Create spooky stories using an open-weight AI model.")

topic = st.text_input("Story topic", "A haunted house near the sea")
length = st.selectbox("Story length", ["Short", "Medium", "Long"])

if st.button("Generate my ghost story"):
    if not topic.strip():
        st.warning("Please enter a story topic.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            words = {
                "Short": "150-200 words",
                "Medium": "300-400 words",
                "Long": "500-650 words"
            }[length]

            with st.spinner("Writing your story..."):
                result = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a creative storyteller. Write original spooky ghost stories."
                        },
                        {
                            "role": "user",
                            "content": f"Write a ghost story about {topic}. Make it {words} and give it a title."
                        }
                    ],
                    temperature=0.8,
                    max_completion_tokens=1200
                )

            st.subheader("Your Story")
            st.write(result.choices[0].message.content)

        except Exception as error:
            st.error("Story generation failed.")
            st.caption(str(error))
