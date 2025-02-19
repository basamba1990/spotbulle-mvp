import speech_recognition as sr

# Initialisation du recognizer
recognizer = sr.Recognizer()

# Utilisation du micro pour capter l'audio
def convertir_audio_en_texte():
    with sr.Microphone() as source:
        print("⏺️ Parlez maintenant...")
        recognizer.adjust_for_ambient_noise(source)  # Ajuste le bruit ambiant
        audio = recognizer.listen(source)  # Capture l'audio
        print("📝 Traitement de l'audio...")
        
        try:
            # Conversion de l'audio en texte avec l'API Google
            texte = recognizer.recognize_google(audio, language="fr-FR")
            print("🎤 Texte converti : ", texte)
            return texte
        except sr.UnknownValueError:
            print("🤔 Je n'ai pas pu comprendre ce que vous avez dit.")
        except sr.RequestError:
            print("⚠️ Impossible de se connecter au service Speech Recognition.")
        return None

# Fonction d'analyse du pitch
def analyser_pitch(pitch):
    print(f"📢 **Analyse du Pitch :** {pitch}")
    
    # Exemple d'analyse du ton et de la clarté :
    if "révolutionne" in pitch or "innovant" in pitch:
        print("🔊 Ton : Positif")
    elif "problème" in pitch or "difficulté" in pitch:
        print("🔊 Ton : Négatif")
    else:
        print("🔊 Ton : Neutre")
        
    # Plus d'analyses peuvent être ajoutées ici : 
    # - Analyse de la structure
    # - Suggestions d'amélioration sur la clarté
    print("✅ Analyse terminée.")

# Fonction principale pour tester la conversion Speech-to-Text et analyser le pitch
def test_speech_to_text():
    texte_converti = convertir_audio_en_texte()
    
    if texte_converti:
        # Envoie le texte à l'IA pour analyse
        analyser_pitch(texte_converti)
    else:
        print("❌ Aucun texte n'a été généré.")

# Tester l'intégration Speech-to-Text
test_speech_to_text()
