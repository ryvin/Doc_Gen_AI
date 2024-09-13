import os
from dotenv import load_dotenv

load_dotenv()

# General LLM Settings
DEFAULT_LLM = os.getenv('DEFAULT_LLM', 'ollama').lower()

# Ollama Configuration
OLLAMA_SERVER_URL = os.getenv('OLLAMA_SERVER_URL', 'http://localhost:11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama2')

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')

# Claude Configuration
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
CLAUDE_MODEL = os.getenv('CLAUDE_MODEL', 'claude-v1')

# Groq Configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_MODEL = os.getenv('GROQ_MODEL', 'groq-model-name')

# SerpAPI Configuration
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

# Logging Configuration
import logging

LOGGING_CONFIG = {
    'level': logging.INFO,
    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    'handlers': [
        logging.StreamHandler()
    ]
}
