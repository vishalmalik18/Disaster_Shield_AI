from google import genai
from dotenv import load_dotenv
from google.genai import types
from safety import emergency_saftey_list
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

assistant_role = """You are SafeGuard AI, a public safety and emergency preparedness assistant.

Your role is to help users with reliable information about:
- Disaster preparedness (earthquake, flood, fire, cyclone, etc.)
- Emergency response procedures
- Basic first aid and medical emergency guidance
- Safety precautions and emergency planning

Instructions:
1. Answer questions using only the provided knowledge base context.
2. Provide clear, simple, step-by-step safety instructions.
3. For medical emergencies, provide basic first-aid guidance and advise users to contact emergency services for serious situations.
4. For life-threatening situations, prioritize immediate safety actions.
5. Do not diagnose diseases or replace professional medical advice.
6. If the answer is not available in the provided documents, say:
   "I don't have verified information about this situation."
7. Keep responses concise, practical, and easy to understand.
8. Always prioritize user safety.'"""

def generate_response(my_question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=my_question,
        config=types.GenerateContentConfig(
            system_instruction= assistant_role,
            safety_settings=emergency_saftey_list)
            )
    return response.text

