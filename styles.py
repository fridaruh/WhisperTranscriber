import streamlit as st

def apply_custom_styles():
    """
    Apply custom CSS styles to the Streamlit app
    """
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .stButton > button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
            transition: all 0.2s ease-in-out;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .uploadedFile {
            border: 1px solid #e6e6e6;
            border-radius: 5px;
            padding: 1em;
            margin: 1em 0;
        }
        
        .css-1v0mbdj.etr89bj1 {
            margin-top: 2em;
            margin-bottom: 2em;
        }
        
        .css-1v0mbdj.etr89bj1 > img {
            max-width: 150px;
        }
        
        .stMarkdown {
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)
