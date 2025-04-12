import ollama
import re

def analyze_mood(entry):
    try:
        prompt = (
            "Analyze the emotional tone of the following journal entry "
            "and respond with only one word (like Happy, Sad, Anxious, Angry, Excited, etc). "
            "Do NOT include any explanation or full sentence.\n\n"
            f"Entry: {entry}"
        )

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response['message']['content'].strip()

        # Use regex to extract first capitalized emotion-like word
        match = re.search(r"\b(Happy|Sad|Angry|Excited|Anxious|Calm|Tired|Frustrated|Grateful|Joyful|Confused|Lonely)\b", content, re.IGNORECASE)
        return match.group(0).capitalize() if match else "Unknown"

    except Exception as e:
        return f"Error: {str(e)}"
