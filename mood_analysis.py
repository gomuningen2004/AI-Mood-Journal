import ollama

def analyze_mood(text, model='llama3'):
    try:
        valid_moods = [
            'Happy', 'Sad', 'Angry', 'Excited', 'Anxious', 'Calm',
            'Tired', 'Frustrated', 'Grateful', 'Joyful', 'Confused', 'Lonely'
        ]

        prompt = (
            "You are an emotion detection AI.\n"
            "Your job is to read the journal entry and respond with ONLY one word that best describes the mood.\n"
            "Choose ONLY from this list:\n"
            f"{', '.join(valid_moods)}\n\n"
            f"Journal Entry:\n{text}\n\n"
            "Mood:"
        )

        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        raw_output = response['message']['content'].strip().title()

        # Extract the first valid mood found in the response
        for mood in valid_moods:
            if mood in raw_output:
                return mood

        return f"Error: Unexpected mood output: '{raw_output}'"
    except Exception as e:
        return f"Error: {str(e)}"
