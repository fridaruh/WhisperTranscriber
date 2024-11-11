import streamlit as st
import os
from utils import process_audio, is_valid_audio_file
from styles import apply_custom_styles
import time

# Page configuration
st.set_page_config(
    page_title="Audio Transcription Dashboard",
    page_icon="🎙️",
    layout="wide"
)

# Apply custom styles
apply_custom_styles()

def main():
    st.title("🎙️ Audio Transcription Dashboard")
    st.markdown("### Convert your audio files to text using OpenAI's Whisper API")

    # Initialize session state
    if 'transcription' not in st.session_state:
        st.session_state.transcription = None
    if 'processing' not in st.session_state:
        st.session_state.processing = False

    # File upload section
    st.markdown("### Upload Audio File")
    st.markdown("Supported formats: MP3, WAV, M4A")
    
    uploaded_file = st.file_uploader(
        "Choose an audio file",
        type=["mp3", "wav", "m4a"],
        help="Maximum file size: 25MB"
    )

    if uploaded_file:
        if not is_valid_audio_file(uploaded_file):
            st.error("Please upload a valid audio file under 25MB")
            return

        if not st.session_state.processing and not st.session_state.transcription:
            if st.button("Transcribe Audio", type="primary"):
                st.session_state.processing = True
                
                # Progress indication
                with st.spinner("Processing your audio file..."):
                    try:
                        # Process the audio file
                        transcription = process_audio(uploaded_file)
                        st.session_state.transcription = transcription
                        st.session_state.processing = False
                    except Exception as e:
                        st.error(f"An error occurred during transcription: {str(e)}")
                        st.session_state.processing = False
                        return

        # Display transcription results
        if st.session_state.transcription:
            st.markdown("### Transcription Result")
            st.markdown("---")
            st.markdown(st.session_state.transcription)
            
            # Download button for transcription
            st.download_button(
                label="Download Transcription",
                data=st.session_state.transcription,
                file_name="transcription.txt",
                mime="text/plain"
            )

            # Reset button
            if st.button("Clear and Start Over"):
                st.session_state.transcription = None
                st.experimental_rerun()

    # Information section
    with st.expander("ℹ️ About this app"):
        st.markdown("""
        This application uses OpenAI's Whisper API to transcribe audio files into text.
        
        **Features:**
        - Supports MP3, WAV, and M4A audio formats
        - Maximum file size: 25MB
        - Accurate transcription powered by OpenAI
        - Download transcription as text file
        
        **Note:** The processing time depends on the length of your audio file.
        """)

if __name__ == "__main__":
    main()
