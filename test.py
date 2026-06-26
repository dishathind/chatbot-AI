
import google.generativeai as genai

genai.configure(api_key=AQ.Ab8RN6J9jP1UNwTQUyi8utUCbqjXujR9rKJPOwUTd3ywmPKPNA)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"✅ {m.name}")
