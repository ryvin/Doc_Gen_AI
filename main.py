# main.py

import sys
import logging
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from tasks.create_tasks import create_new_task, rerun_task
from config.settings import LOGGING_CONFIG

logging.basicConfig(**LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def main():
    """Main entry point of the application."""
    logger.info("Starting Process Documentation Generator with AI Agents (Using Ollama)")
    commands = ['new', 'rerun', 'exit']
    command_completer = WordCompleter(commands, ignore_case=True)
    
    try:
        while True:
            user_input = prompt("Enter a command (type 'exit' to quit): ", completer=command_completer)
            user_input = user_input.strip().lower()
            
            if user_input == 'new':
                create_new_task()
            elif user_input == 'rerun':
                rerun_task()
            elif user_input == 'exit':
                logger.info("Exiting application.")
                sys.exit()
            else:
                print("Invalid command. Please enter 'new', 'rerun', or 'exit'.")
    except KeyboardInterrupt:
        logger.info("Application interrupted by user.")
        sys.exit()
    except Exception as e:
        logger.exception("An unexpected error occurred: %s", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
