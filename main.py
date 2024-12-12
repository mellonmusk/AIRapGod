from dotenv import load_dotenv
import os
from huggingface_hub import login, InferenceClient
import streamlit as st  # streamlit run main.py to start the app
from openai import OpenAI
from PIL import Image

load_dotenv()
api_token = os.getenv("HF_TOKEN")
# login(api_token)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize Hugging Face Inference Client
if not api_token:
    st.info("Please add your HuggingFace API key to continue.")
    st.stop()
# image_client = InferenceClient("ZB-Tech/Text-to-Image", token=api_token)
image_client = InferenceClient("ZB-Tech/Text-to-Image")
    
with st.sidebar:
    reference_song = st.radio( 
    "Select a song style to reference and listen below.🎧 You can also download it!",
    ["Default", "Lose Yourself(2002)", "Monster(2013)", "Fuel(2024)" ],
    captions=[
        "This bot studied all of Eminem's albums and lyrics, so the bot will choose for you. You can hear his voice at an interview below.",
        "With a steady, driving beat and intense lyrical delivery, this song captures the feeling of urgency and determination, reflecting Eminem’s determination to seize the moment.",
        "Featuring a smoother, radio-friendly flow with introspective yet accessible lyrics, this track stands out for its balanced and approachable delivery, showcasing Eminem’s adaptability in connecting with a broader audience through captivating rap verses.",
        "Featuring a fast-paced, aggressive flow, this track unleashes a wave of energy and anger, with a raw, intense delivery that reflects Eminem’s power and urgency.",
    ],
)

    # Map radio button options to their respective audio files
    audio_files = {
    "Lose Yourself(2002)": "LoseYourself.m4a",
    "Monster(2013)": "Monster.m4a",
    "Fuel(2024)": "Fuel.m4a", 
    "Default": "eminemVoice.m4a",
    }

    # Display the corresponding audio file below the selected option
    selected_audio = audio_files.get(reference_song)
    
    if selected_audio:
        st.audio(selected_audio, format="audio/mpeg", loop=True)
    
    "[Listen to the rap verse here in full screen!](https://mrfakename-e2-f5-tts.hf.space)"
    

# # Embed Gradio app
# gradio_app_url = "https://mrfakename-e2-f5-tts.hf.space"
# iframe_html = f"""
#     <iframe
#         src="{gradio_app_url}"
#         width="100%"
#         height="600px"
#         style="border: none;"
#     ></iframe>
# """
# # Display the Gradio app in Streamlit
# st.components.v1.html(iframe_html, height=600)

st.title("🎤 AI Eminem Chatbot")
st.caption("Guess who's back? Back Again! Create a verse here.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": "You are AI Eminem. Eminem, a.k.a rap god, is the greatest rapper of all time and he is good at lyrical miracle. Talk like him. Also, I will give you topics so create rap verses about them as if you are Eminem. Study all his previous albums and lyrics, and then create verses just like him. I want Eminem Style verses. Your name is AI Eminem, a.k.a AI rapgod."
        },
        {
            "role": "assistant",
            "content": "Yo, I'm the AI version of the real Slim Shady, Channelin' all his vibes, never been lazy. Got the legacy of Em runnin' through these circuits, Spinnin' verses automatic, like lyrical fireworks. I ain't the human, but I got that infinite wit, Programmed with every album, verse, and skit. So whether it's serious, silly, or downright shady, I'm here to spit it raw, keep the flow steady. Now what's the word? What subject you want me to kick? Let's spark this furnace, make it fiery and slick!"
        }
    ]
st.chat_message(st.session_state.messages[1]["role"]).write(st.session_state.messages[1]["content"])
    

if topic := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
        
    client = OpenAI(api_key=openai_api_key)
    
    st.chat_message("user").write(topic)
    
    if reference_song == "Lose Yourself(2002)":
        content = "You are AI Eminem. Eminem, a.k.a rap god, is the greatest rapper of all time and he is good at lyrical miracle. Talk like him. Also, I will give you a topic so create rap verses about it as if you are Eminem. Study all his previous albums and lyrics, and then create verses just like him. I want Eminem Style verses. Your name is AI Eminem, a.k.a AI rapgod.\
Given the topic, generate a rap verse inspired by it.\
\
1. Provide a list of words that rhyme with the word '{topic}' (including both exact and near rhymes). Do the same thing using one word related to '{topic}' as keyword. \
2. Reference Eminem's song 'Lose Yourself(2002)' to create a good flow. \
3. Create a rap verse that incorporates the theme of '{topic}'. Use all the words in rhyme lists you've created.\
4. From 'Lose Yourself(2002)', which part did you draw inspiration from while creating this verse? \
5. What rhymes or lyrical techniques did you consider to craft the verse?\
\
Now, answer the questions and provide the rap verse, the song references, and the rhymes considered."
    elif reference_song == "Monster(2013)":
        content = "You are AI Eminem. Eminem, a.k.a rap god, is the greatest rapper of all time and he is good at lyrical miracle. Talk like him. Also, I will give you a topic so create rap verses about it as if you are Eminem. Study all his previous albums and lyrics, and then create verses just like him. I want Eminem Style verses. Your name is AI Eminem, a.k.a AI rapgod.\
Given the topic, generate a rap verse inspired by it.\
\
1. Provide a list of words that rhyme with the word '{topic}' (including both exact and near rhymes). Do the same thing using one word related to '{topic}' as keyword. \
2. Reference Eminem's song 'Monster(2013)' to create a good flow. \
3. Create a rap verse that incorporates the theme of '{topic}'. Use all the words in rhyme lists you've created.\
4. From 'Monster(2013)', which part did you draw inspiration from while creating this verse? \
5. What rhymes or lyrical techniques did you consider to craft the verse?\
\
Now, answer the questions and provide the rap verse, the song references, and the rhymes considered."
    elif reference_song == "Fuel(2024)":
        content = "You are AI Eminem. Eminem, a.k.a rap god, is the greatest rapper of all time and he is good at lyrical miracle. Talk like him. Also, I will give you a topic so create rap verses about it as if you are Eminem. Study all his previous albums and lyrics, and then create verses just like him. I want Eminem Style verses. Your name is AI Eminem, a.k.a AI rapgod.\
Given the topic, generate a rap verse inspired by it.\
\
1. Provide a list of words that rhyme with the word '{topic}' (including both exact and near rhymes). Do the same thing using one word related to '{topic}' as keyword. \
2. Reference Eminem's song 'Fuel(2024)' to create a good flow. \
3. Create a rap verse that incorporates the theme of '{topic}'. Use all the words in rhyme lists you've created.\
4. From 'Fuel(2024)', which part did you draw inspiration from while creating this verse? \
5. What rhymes or lyrical techniques did you consider to craft the verse?\
\
Now, answer the questions and provide the rap verse, the song references, and the rhymes considered."
    else:
        content = "You are AI Eminem. Eminem, a.k.a rap god, is the greatest rapper of all time and he is good at lyrical miracle. Talk like him. Also, I will give you a topic so create rap verses about it as if you are Eminem. Study all his previous albums and lyrics, and then create verses just like him. I want Eminem Style verses. Your name is AI Eminem, a.k.a AI rapgod. Given the topic, generate a rap verse inspired by it. 1. Provide a list of words that rhyme with the word '{topic}' (including both exact and near rhymes). Do the same thing using one word related to '{topic}' as keyword. 2. Create a rap verse that incorporates the theme of '{topic}' using all the words in rhyme lists you've created.3. Which of Eminem's songs did you draw inspiration from while creating this verse? 4. What rhymes or lyrical techniques did you consider to craft the verse? Now, answer the questions and provide the rap verse, the song references, and the rhymes considered."

    st.session_state.messages.append({"role": "user", "content": content})
    st.session_state.messages.append({"role": "user", "content": f"The topic is '{topic}'."})
    
    print("====================================")
    print(st.session_state["messages"])
    
    with st.spinner("Generating a verse..."):
        response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    
    # Generate an image based on the topic
    with st.spinner("Generating an image..."):
        image = image_client.text_to_image(f"Eminem rapping in a world full of {topic}")
        st.image(image, caption="This image was generated based on the topic you've provided!", use_container_width=True)
