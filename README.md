
# Audio Transcription Dashboard 🎙️

The **Audio Transcription Dashboard** is a Streamlit application that allows users to transcribe audio files into text using OpenAI's Whisper API. The app supports various audio formats and provides options to export the transcription in different formats.

## Features

- **Audio File Support**: Upload files in MP3, WAV, and M4A formats.
- **Language Detection**: Automatically detects the language of the audio file or allows manual selection.
- **Transcription Accuracy**: Powered by OpenAI's Whisper API for reliable transcription.
- **Export Options**: Download transcriptions in TXT, JSON, or CSV formats.
- **File Size Limit**: Supports files up to 25MB.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/audio-transcription-dashboard.git
   cd audio-transcription-dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Add your OpenAI API key to `.env` or set it in your environment as `OPENAI_API_KEY`.

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Upload Audio File**: Supported formats include MP3, WAV, and M4A. Maximum size is 25MB.
2. **Select Language**: Choose a language from the dropdown list or allow auto-detection.
3. **Transcribe**: Click on the "Transcribe Audio" button to start processing.
4. **View Results**: See the transcription along with the detected language.
5. **Export**: Choose an export format (TXT, JSON, CSV) and download the transcription.
6. **Reset**: Use the "Clear and Start Over" button to process a new file.

## File Structure

- **app.py**: Main application file.
- **utils.py**: Utility functions for audio processing and transcription export.
- **styles.py**: Custom styling functions for the app.
- **requirements.txt**: List of dependencies.

## Dependencies

- **Streamlit**: Frontend for creating the web interface.
- **OpenAI**: Whisper API for transcription services.

Install dependencies with:
```bash
pip install -r requirements.txt
```

## About This App

This dashboard leverages OpenAI’s Whisper API to convert audio into text, supporting multiple languages and formats. The process is straightforward, with export options and a reset functionality for multiple uses.

**Note**: Processing times may vary based on audio file length.

---
