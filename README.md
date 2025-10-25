# Reports-summarization-using-ai
This app uses the Gemini API to summarize Reports
you can test the app in:https://reports-summarization.streamlit.app/

Technical Skills & Project Implementation
This project is a strong example of building a working AI web app, showing good skills in frontend design, linking to APIs, and handling errors correctly.

1. Frontend & UI Development (Streamlit)
Fast Development and Design: Successfully built and launched a simple, single-page application using the Streamlit Python library.
Smart Component Use: Used key Streamlit tools like st.columns, st.expander, and st.text_area (set to height=300) to make a clean, easy-to-use input area for long texts.
Better Look and Feel: Used st.markdown with simple Inline HTML/CSS to improve the look (e.g., adding custom colored text for user tips).

2. Gemini API Integration & AI Backend
API Connection: Set up a safe and working link to Google's AI models using the google-genai Python SDK.
Data Setup: Made sure the user's text was correctly formatted for the API by using Part.from_text.
Model Choice: Used the gemini-2.5-flash model to make sure the summarization task is quick and gives accurate results.

3. Strong Error Handling & Security
Checking API Keys: Created a custom check to make sure the user's API key is valid before running the AI model.
Handling Connection Errors: Added specific code to catch the google.genai.errors.ClientError. This is important because it:
Stops the confusing technical error log (Traceback) from showing.
Shows a clear, simple warning to the user if their API key is invalid (HTTP 400).
Control over App Flow: Used st.stop() to stop the app immediately if the API key is missing or wrong, saving resources and preventing unnecessary API calls.

4. User Experience (UX) Flow
Clear Updates: Added simple status messages (st.info, st.success) to tell the user what the app is doing while it waits for the AI (e.g., "Inputs received," "Sending request").
Better Input: Changed the small default input box to a large, dedicated text area to make it easier for users to paste long reports.
