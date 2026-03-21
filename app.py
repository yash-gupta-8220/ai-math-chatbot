import streamlit as st
import os
from groq import Groq

# 🔑 Add your API key here
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("API key not found")
    st.stop()
client = Groq(api_key=api_key)

# Page settings
st.set_page_config(page_title="Yash AI Math Chatbot", page_icon="🧮")

# Title
st.title("🧮 AI Numerical Math Solver")
st.write("Solve math problems with proper step-by-step calculations 🚀")
st.write("Developed by Yash Gupta")

# Sidebar
st.sidebar.title("About Project")
st.sidebar.info(
    "This AI chatbot solves mathematical problems using proper numerical methods. "
    "It shows full calculations like a student solving on paper."
)

# Input
user_input = st.text_input("Enter your math question:")

# Button
if st.button("Solve"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a question")
    else:
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",   # ✅ FINAL CORRECT MODEL
                messages=[
                    {
                        "role": "system",
                        "content": """Solve the given mathematical problem step by step.

Rules:
- Show full calculations
- Do not skip steps
- Solve like a student
- At the end write:

Final Answer:
x = ?, y = ?
"""
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )

            answer = response.choices[0].message.content

            st.success("✅ Solution:")
            st.code(answer)

        except Exception as e:
            st.error(f"❌ Error: {e}")

# Footer
st.write("---")
st.write("📌 Future Scope: Can be extended to Engineering Maths and AI learning assistant.")
