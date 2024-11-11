import os
import tempfile
from openai import OpenAI
import streamlit as st

def is_valid_audio_file(uploaded_file):
    """
    Validate the uploaded audio file
    """
    # Check file size (25MB limit)
    MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB in bytes
    
    if uploaded_file.size > MAX_FILE_SIZE:
        return False
    
    # Check file type
    allowed_types = ['audio/mpeg', 'audio/wav', 'audio/x-m4a', 'audio/mp3']
    if uploaded_file.type not in allowed_types:
        return False
    
    return True

def process_audio(uploaded_file):
    """
    Process the audio file using OpenAI's Whisper API
    """
    try:
        # Create a temporary file to store the uploaded audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        # Initialize OpenAI client with API key from environment
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        # Open and transcribe the audio file
        with open(tmp_file_path, 'rb') as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )

        # Clean up the temporary file
        os.unlink(tmp_file_path)

        return transcription

    except Exception as e:
        # Clean up the temporary file in case of error
        if 'tmp_file_path' in locals():
            os.unlink(tmp_file_path)
        raise Exception(f"Transcription failed: {str(e)}")
