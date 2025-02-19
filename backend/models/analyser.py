import google.generativeai as genai

def analyze_text(transcription: str) -> dict:
    """ Analyse le texte avec Gemini et génère des suggestions. """
    genai.configure(api_key="VOTRE_CLE_API_GEMINI")
    model = genai.GenerativeModel("gemini-1.5-flash")

    tone_prompt = f"Analysez le ton de ce texte :\n\n{transcription}"
    tone_response = model.generate_content(tone_prompt)
    
    vocab_prompt = f"Proposez des améliorations de vocabulaire pour ce texte :\n\n{transcription}"
    vocab_response = model.generate_content(vocab_prompt)

    return {
        "tone": tone_response.text,
        "vocab_suggestions": vocab_response.text,
    }
