# utils/history_utils.py

import json
import os
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

history_file = "process_history.json"

def load_history() -> List[Dict[str, Any]]:
    """Loads the process history from a JSON file.

    Returns:
        A list of history entries.
    """
    if os.path.exists(history_file):
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except Exception as e:
            logger.error("Failed to load history: %s", e)
            history = []
    else:
        history = []
    return history

def save_history(entry: Dict[str, Any]) -> None:
    """Saves a history entry to the JSON file.

    Args:
        entry: The history entry to save.
    """
    history = load_history()
    history.append(entry)
    try:
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        logger.error("Failed to save history: %s", e)
