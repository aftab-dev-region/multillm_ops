from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_NAMES= [
        "openai:gpt-4o-mini",
        "gpt-5-nano-2025-08-07"
    ]

settings=Settings()