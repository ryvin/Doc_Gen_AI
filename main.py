# main.py

import logging
from tasks import create_new_task, rerun_task
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

def main():
    print("Welcome to Doc_Gen_AI: Process Documentation Generator with AI Agents")
    session = PromptSession()
    commands = ['new', 'rerun', 'exit']
    command_completer = WordCompleter(commands)

    while True:
        try:
            command = session.prompt("Enter a command (type 'exit' to quit): ", completer=command_completer).strip()
            if command == 'new':
                create_new_task()
            elif command == 'rerun':
                rerun_task()
            elif command == 'exit':
                print("Exiting the program.")
                break
            else:
                print("Invalid command. Available commands: new, rerun, exit")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
