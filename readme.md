Certainly! Below is the updated `README.md` for **Doc_Gen_AI**, now using the **Apache License 2.0**. All references to the previous MIT License have been updated accordingly.

---

# Doc_Gen_AI

**Doc_Gen_AI** is a Python-based application that implements a multi-agent system designed to generate, test, improve, and refine **process documentation** using AI agents and Large Language Models (LLMs). It allows users to create documentation based on existing files, online research, and user-defined processes. The system utilizes **virtual testers** to simulate following the documentation, provide feedback, and iteratively improve the documentation until it is accurate and clear.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up the Environment](#set-up-the-environment)
  - [Install Dependencies](#install-dependencies)
  - [Install and Run Ollama](#install-and-run-ollama)
  - [Set Up API Keys and LLM Configurations](#set-up-api-keys-and-llm-configurations)
- [How to Use](#how-to-use)
  - [Running the Program](#running-the-program)
  - [Interactive CLI](#interactive-cli)
  - [Process Documentation Generation](#process-documentation-generation)
  - [Output](#output)
- [How It Works](#how-it-works)
  - [Agents Overview](#agents-overview)
  - [Workflow](#workflow)
  - [Project Structure](#project-structure)
- [Configuration](#configuration)
  - [LLM Selection](#llm-selection)
  - [Environment Variables](#environment-variables)
- [Requirements](#requirements)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Contributing](#contributing)

---

## Features

1. **Multiple LLM Support**:
   - Supports various LLMs: **Ollama**, **OpenAI**, **Claude**, and **Groq**.
   - Users can select which LLM to use for each task or agent.

2. **Input Handling**:
   - Users specify the process to document and provide relevant files (PDF, DOCX, MD, TXT, images) as reference material.
   - The system lists available files in a directory and allows users to select which files to include.

3. **Process Documentation Generation**:
   - Generates documentation based on reference files, online research, and business requirements.
   - Users can improve existing documentation or reference previous documentation to generate new documents.

4. **Testing & Iteration**:
   - The Virtual Tester Agent simulates following the documentation, provides feedback, and suggests improvements.
   - The system iteratively refines the documentation based on feedback until it is accurate and complete.

5. **Feedback Loop**:
   - The Overall Documentation Manager evaluates feedback and determines if further revisions are necessary, creating an ongoing feedback loop.

6. **Process History**:
   - Tracks all previously generated documentation, allowing users to rerun the process for improvements or reference existing documentation.

7. **Interactive CLI**:
   - An interactive command-line interface with auto-completion for easy task creation and process management.

---

## Installation

### Prerequisites

- **Python 3.9 or higher**
- **Conda** (optional, for environment management)
- **Ollama** (for running local LLMs)
- **SerpAPI API Key** (for online research capabilities)
- **API Keys for other LLMs** (if you plan to use OpenAI, Claude, or Groq)

### Clone the Repository

```bash
git clone <repository-url>
cd Doc_Gen_AI
```

### Set Up the Environment

You can use either a **virtual environment** or a **Conda** environment.

#### Using Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Using Conda

```bash
conda create -n doc_gen_ai_env python=3.9
conda activate doc_gen_ai_env
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install and Run Ollama

Ollama is used to run LLMs locally. Follow the instructions from the [Ollama GitHub repository](https://github.com/jmorganca/ollama).

#### Install Ollama

- **macOS (via Homebrew)**:

  ```bash
  brew install ollama/tap/ollama
  ```

- **Linux**:

  Download the latest release from the [releases page](https://github.com/jmorganca/ollama/releases) and follow the installation instructions.

#### Pull the LLM Model

```bash
ollama pull llama2
```

#### Start Ollama Server

```bash
ollama serve
```

> **Note**: The server runs on port `11434` by default.

### Set Up API Keys and LLM Configurations

Create a `.env` file in the root directory by copying `EXAMPLE.env`:

```bash
cp EXAMPLE.env .env
```

Open the `.env` file and fill in your API keys and settings:

- **General LLM Settings**:
  - `DEFAULT_LLM`: Set to `ollama`, `openai`, `claude`, or `groq`.

- **Ollama Settings**:
  - `OLLAMA_SERVER_URL`: Default is `http://localhost:11434`.
  - `OLLAMA_MODEL`: Default is `llama2`.

- **OpenAI Settings**:
  - `OPENAI_API_KEY`: Your OpenAI API key.
  - `OPENAI_MODEL`: e.g., `gpt-3.5-turbo`, `gpt-4`.

- **Claude Settings**:
  - `CLAUDE_API_KEY`: Your Claude API key.
  - `CLAUDE_MODEL`: e.g., `claude-v1`.

- **Groq Settings**:
  - `GROQ_API_KEY`: Your Groq API key.
  - `GROQ_MODEL`: The Groq model name.

- **SerpAPI API Key**:
  - `SERPAPI_API_KEY`: Required for online research capabilities.

> **Important**: Keep your `.env` file secure and do not commit it to version control.

---

## How to Use

### Running the Program

Ensure that the Ollama server is running:

```bash
ollama serve
```

Run the main program:

```bash
python main.py
```

### Interactive CLI

The system provides an interactive CLI for creating new tasks or rerunning previous processes.

**Available Commands**:

- `new`: Create a new process documentation task.
- `rerun`: Rerun a previously generated process.
- `exit`: Quit the CLI.

Example:

```bash
Enter a command (type 'exit' to quit): new
```

### Process Documentation Generation

1. **Create a New Task**:

   - **Process Name**: Enter the name of the process you want to document.
   - **Audience Level**: Specify the target audience level (e.g., beginner, intermediate, expert).
   - **Reference Files Directory**: Provide the directory path containing reference files.
   - **Select Reference Files**: Choose which files to include as references.

2. **Select LLM**:

   - When prompted, select the LLM to use for this task.
   - Options: `ollama`, `openai`, `claude`, `groq`.
   - If left blank, the default LLM specified in the `.env` file will be used.

3. **Provide Business Requirements**:

   - The Requirements Agent will prompt you to enter any business requirements, compliance needs, or constraints.

4. **Documentation Generation**:

   - The system performs online research on the process topic.
   - Generates initial documentation based on research, requirements, and reference materials.

5. **Review and Testing**:

   - The Reviewer Agent evaluates the documentation for completeness and clarity.
   - The Virtual Tester Agent tests the documentation and provides feedback.

6. **Feedback Loop**:

   - The Overall Documentation Manager assesses feedback.
   - If revisions are needed, the system iterates to improve the documentation.

### Output

- The final documentation is saved in the `output_documentation` directory.
- The documentation file is named `<process_name>_documentation.txt`.
- Process history is stored in `process_history.json`.

---

## How It Works

### Agents Overview

1. **Research Agent**:
   - Performs online research using SerpAPI.
   - Gathers information to become a Subject Matter Expert.
   - Uses the selected LLM for generating research summaries.

2. **Requirements Agent**:
   - Collects business requirements, compliance needs, and constraints.

3. **Documentation Agent**:
   - Generates and revises process documentation.
   - Uses inputs from research, requirements, and reference materials.
   - Uses the selected LLM for content generation.

4. **Reviewer Agent**:
   - Reviews documentation for accuracy and clarity.
   - Provides feedback for improvements.
   - Uses the selected LLM for analysis.

5. **Virtual Tester Agent**:
   - Simulates following the documentation.
   - Provides detailed feedback on each step.
   - Uses the selected LLM for simulation.

6. **Overall Documentation Manager**:
   - Oversees the entire process.
   - Evaluates feedback and determines if further revisions are needed.

### Workflow

1. **Initialization**:
   - User initiates a new task or reruns an existing one.

2. **Research and Requirements Gathering**:
   - Research Agent performs online research.
   - Requirements Agent gathers business requirements.

3. **Documentation Generation**:
   - Documentation Agent creates initial documentation.

4. **Review and Testing**:
   - Reviewer Agent reviews the documentation.
   - Virtual Tester Agent tests the documentation.

5. **Feedback Evaluation**:
   - Overall Documentation Manager evaluates feedback.
   - Determines if revisions are necessary.

6. **Iteration**:
   - If needed, the system revises and retests the documentation.
   - The loop continues until the documentation is satisfactory.

### Project Structure

```
Doc_Gen_AI/
├── agents/
│   ├── __init__.py
│   ├── documentation_agent.py        # Generates process documentation
│   ├── overall_manager_agent.py      # Oversees feedback and documentation improvements
│   ├── requirements_agent.py         # Gathers business requirements and constraints
│   ├── research_agent.py             # Performs online research
│   ├── reviewer_agent.py             # Reviews the documentation for accuracy and clarity
│   └── virtual_tester_agent.py       # Simulates following the process and provides feedback
├── tasks/
│   ├── __init__.py
│   └── create_tasks.py               # Manages task creation and reruns
├── utils/
│   ├── __init__.py
│   ├── file_utils.py                 # File parsing utilities
│   ├── history_utils.py              # Manages process history
│   ├── llm_utils.py                  # LLM abstraction layer
│   ├── search_utils.py               # Performs web searches using SerpAPI
├── tests/
│   ├── __init__.py
│   └── test_agents.py                # Placeholder for unit tests
├── config/
│   └── settings.py                   # Configuration settings
├── main.py                           # Main entry point
├── requirements.txt                  # Project dependencies
├── process_history.json              # Stores process history
├── README.md                         # Project documentation
├── EXAMPLE.env                       # Example environment variables file
├── .gitignore                        # Git ignore file
└── .env                              # Environment variables (API keys)
```

---

## Configuration

### LLM Selection

You can choose which LLM to use for generating documentation. Options include:

- **Ollama**: Local LLM server.
- **OpenAI**: Requires OpenAI API key.
- **Claude**: Requires Claude API key.
- **Groq**: Requires Groq API key (implementation placeholder).

### Environment Variables

All configurations are managed via the `.env` file.

- **DEFAULT_LLM**: Sets the default LLM to use.
- **API Keys and Model Names**: Set the API keys and model names for the LLMs you intend to use.

---

## Requirements

- **Python Packages**:
  - `PyPDF2`
  - `python-docx`
  - `prompt_toolkit`
  - `requests`
  - `serpapi`
  - `python-dotenv`
  - `openai` (if using OpenAI)
  - `anthropic` (if using Claude)

- **External Tools**:
  - **Ollama**: For running local LLMs.
  - **SerpAPI API Key**: For online research capabilities.
  - **OpenAI API Key**: If using OpenAI LLM.
  - **Claude API Key**: If using Claude LLM.
  - **Groq API Key**: If using Groq LLM.

---

## Future Enhancements

- **Unit Testing**: Implement comprehensive unit tests for all modules.
- **Continuous Integration**: Set up CI/CD pipelines for automated testing and deployment.
- **Dockerization**: Containerize the application using Docker for easier deployment.
- **Advanced CLI**: Use libraries like `click` or `typer` for a more advanced CLI interface.
- **Performance Optimization**: Profile the application to optimize performance.
- **Caching**: Implement caching for web search results to reduce API calls.
- **User Authentication**: Add authentication mechanisms for multi-user support.
- **GUI Interface**: Develop a graphical user interface for better user experience.
- **Groq Integration**: Complete the implementation for Groq LLM when API details are available.

---

## License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for more information.

---

## Contact

For questions or suggestions, please open an issue or contact the project maintainer.

---

**Enjoy using Doc_Gen_AI to automate your process documentation!**

---

## Additional Notes

- **Security**: Remember to keep your `.env` file secure and never share your API keys publicly.
- **API Usage Limits**: Be aware of the usage limits and policies of the APIs you use (OpenAI, Claude, SerpAPI, etc.).
- **LLM Compatibility**: Ensure that the prompts used are compatible with the LLM you select. You may need to adjust prompts for optimal performance with different models.

---

Feel free to let me know if you need any further assistance or have additional requests!