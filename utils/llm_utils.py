# utils/llm_utils.py

import logging
from config.settings import (
    DEFAULT_LLM,
    OLLAMA_SERVER_URL,
    OLLAMA_MODEL,
    OPENAI_API_KEY,
    OPENAI_MODEL,
    CLAUDE_API_KEY,
    CLAUDE_MODEL,
    GROQ_API_KEY,
    GROQ_MODEL,
)
import requests

logger = logging.getLogger(__name__)

def query_llm(prompt: str, llm: str = None) -> str:
    """Queries the selected LLM with the given prompt.

    Args:
        prompt: The prompt to send to the LLM.
        llm: The LLM to use ('ollama', 'openai', 'claude', 'groq'). If None, uses DEFAULT_LLM.

    Returns:
        The response from the LLM as a string.
    """
    llm = llm or DEFAULT_LLM
    llm = llm.lower()

    if llm == 'ollama':
        return query_ollama(prompt)
    elif llm == 'openai':
        return query_openai(prompt)
    elif llm == 'claude':
        return query_claude(prompt)
    elif llm == 'groq':
        return query_groq(prompt)
    else:
        logger.error("Unsupported LLM specified: %s", llm)
        raise ValueError(f"Unsupported LLM specified: {llm}")

def query_ollama(prompt: str) -> str:
    """Queries the Ollama LLM."""
    url = f"{OLLAMA_SERVER_URL}/generate"
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt
    }
    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get('response', '')
    except requests.exceptions.RequestException as e:
        logger.error("Error communicating with Ollama: %s", e)
        raise

def query_openai(prompt: str) -> str:
    """Queries the OpenAI LLM."""
    import openai
    if not OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY not found.")
        raise ValueError("OPENAI_API_KEY not found.")
    openai.api_key = OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        logger.error("Error communicating with OpenAI: %s", e)
        raise

def query_claude(prompt: str) -> str:
    """Queries the Claude LLM."""
    # Note: As of 2023-10, the Claude API is available via Anthropic.
    import anthropic
    if not CLAUDE_API_KEY:
        logger.error("CLAUDE_API_KEY not found.")
        raise ValueError("CLAUDE_API_KEY not found.")
    client = anthropic.Client(api_key=CLAUDE_API_KEY)
    try:
        response = client.completion(
            prompt=f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}",
            model=CLAUDE_MODEL,
            max_tokens_to_sample=500,
            temperature=0.7,
        )
        return response['completion'].strip()
    except Exception as e:
        logger.error("Error communicating with Claude: %s", e)
        raise

def query_groq(prompt: str) -> str:
    """Queries the Groq LLM."""
    # Placeholder implementation, as the Groq API details are not specified.
    # Replace with actual API calls to Groq when available.
    if not GROQ_API_KEY:
        logger.error("GROQ_API_KEY not found.")
        raise ValueError("GROQ_API_KEY not found.")
    logger.error("Groq LLM integration is not yet implemented.")
    raise NotImplementedError("Groq LLM integration is not yet implemented.")
