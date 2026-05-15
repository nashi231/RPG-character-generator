import streamlit as st
import google.generativeai as genai


client = genai.configure(api_key="AIzaSyBcIjLu4uxIjmt63JznqXr9QpbwAMd5kJg")
#title
st.title("RPG Character Generator")

chartype=st.text_input("Enter a character type: ")


if st.button("Generate Character"):
    #creating a prompt
    prompt =f"""

    Create a detailed RPG character.

    Character Type: {chartype}

    Format EXACTLY like this:

    ## Name:
    ## Class:
    ## Role: 
    ## Weapon:
    ## Ability:
    ## Strengths:
    ## Weaknesses:
    ## Backstory:
    ## Pet:
    ## Pet Ability:

    IMPORTANT RULES:
    Do NOT use markdown (##)
    only one line for the backstory
    class is of the range S>A>B>C>D
    generate clean, simple values only
    
    
    """

    #request AI
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
                       
    result = response.text  
    st.subheader("Your Character")

    #create dict with values
    lines = result.split("\n")
    data = {}

    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()

    #Generate Card
    st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #1e1e2f, #2c2c54);
            padding: 20px;
            border-radius: 15px;
            color: white;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            font-family: Arial;
        ">

        <h2 style="text-align:center; color:#ffd700;">🧙 RPG Character Card</h2>

        <hr>

        <p><b>Name:</b> {data.get('Name', '')}</p>
        <p><b>Class:</b> {data.get('Class', '')}</p>
        <p><b>Role:</b> {data.get('Role', '')}</p>
        <p><b>Weapon:</b> {data.get('Weapon', '')}</p>
        <p><b>Ability:</b> {data.get('Ability', '')}</p>
        <p><b>Strengths:</b> {data.get('Strengths', '')}</p>
        <p><b>Weaknesses:</b> {data.get('Weaknesses', '')}</p>

        <hr>

        <p><b>🧾 Backstory:</b><br>{data.get('Backstory', '')}</p>

        <hr>

        <p><b>🐾 Pet:</b> {data.get('Pet', '')}</p>
        <p><b>Pet Ability:</b> {data.get('Pet Ability', '')}</p>

        </div>
        """, unsafe_allow_html=True)

    







