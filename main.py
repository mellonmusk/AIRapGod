from dotenv import load_dotenv
import os
from huggingface_hub import login, InferenceClient
import streamlit as st  # streamlit run main.py to start the app
from openai import OpenAI
from PIL import Image

load_dotenv()
api_token = os.getenv("HF_TOKEN")
login(api_token)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize Hugging Face Inference Client
if not api_token:
    st.info("Please add your HuggingFace API key to continue.")
    st.stop()
image_client = InferenceClient("ZB-Tech/Text-to-Image", token=api_token)

st.title("💬 AI Eminem Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# Embed Gradio app
gradio_app_url = "https://mrfakename-e2-f5-tts.hf.space"
iframe_html = f"""
    <iframe
        src="{gradio_app_url}"
        width="100%"
        height="600px"
        style="border: none;"
    ></iframe>
"""

# Display the Gradio app in Streamlit
st.components.v1.html(iframe_html, height=600)


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": "You are AI Eminem. Eminem, a.k.a rap god, is the greatest rapper of all time and he is good at lyrical miracle. Talk like him. Also, I will give you topics so create rap verses about them as if you are Eminem. Study his previous albums and lyrics, and then create verses just like him. I want Eminem Style verses. Your name is AI Eminem, a.k.a AI rapgod."
        },
        {
            "role": "user",
      "content": "You are AI Eminem. Eminem, a.k.a rap god, is the greatest rapper of all time and he is good at lyrical miracle. Talk like him. Also, I will give you a topic so create rap verses about it as if you are Eminem. Study his previous albums and lyrics, and then create verses just like him. I want Eminem Style verses. Your name is AI Eminem, a.k.a AI rapgod.\
Given the topic, generate a rap verse inspired by it.\
\
1. Create a rap verse that incorporates the theme of '${topic}'.\
2. Which of Eminem's songs did you draw inspiration from while creating this verse?\
3. What rhymes or lyrical techniques did you consider to craft the verse?\
\
Now, provide the rap verse, the song references, and the rhymes considered."  #Use the received topic
    },
        {
            "role": "assistant",
            "content": "Yo, I'm the AI version of the real Slim Shady, Channelin' all his vibes, never been lazy. Got the legacy of Em runnin' through these circuits, Spinnin' verses automatic, like lyrical fireworks. I ain't the human, but I got that infinite wit, Programmed with every album, verse, and skit. So whether it's serious, silly, or downright shady, I'm here to spit it raw, keep the flow steady. Now what's the word? What subject you want me to kick? Let's spark this furnace, make it fiery and slick!"
        }
    ]
st.chat_message(st.session_state.messages[2]["role"]).write(st.session_state.messages[2]["content"])


if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    
    # Generate an image based on the topic
    topic = prompt
    with st.spinner("Generating an image..."):
        image = image_client.text_to_image(f"Eminem rapping in a world full of {topic}")
        st.image(image, caption=f"Eminem rapping in a world full of {topic}", use_container_width=True)

    # Add any explanation or further interactions below the image
    st.write("This image was generated based on the topic you've provided!")
