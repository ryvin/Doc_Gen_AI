# tasks/create_tasks.py

import os
import logging
from agents import (
    RequirementsAgent,
    ResearchAgent,
    DocumentationAgent,
    ReviewerAgent,
    VirtualTesterAgent,
    OverallManagerAgent,
)
from utils.file_utils import parse_reference_files
from utils.history_utils import save_history, load_history
from config.settings import DEFAULT_LLM

logger = logging.getLogger(__name__)

def create_new_task():
    """Creates a new process documentation task."""
    try:
        process_name = input("Enter the name of the process to document: ").strip()
        audience_level = input("Enter the target audience level (e.g., beginner, intermediate, expert): ").strip()

        reference_dir = input("Enter the directory containing reference files: ").strip()
        files = os.listdir(reference_dir)
        if not files:
            logger.warning("No files found in the specified directory.")
            return
        print("Available files:")
        for idx, file in enumerate(files):
            print(f"{idx+1}. {file}")
        selected_files_indices = input("Enter the numbers of the files to include as references (comma-separated): ")
        selected_indices = [int(idx.strip()) - 1 for idx in selected_files_indices.split(",")]
        selected_files = [files[idx] for idx in selected_indices if 0 <= idx < len(files)]

        reference_files_content = parse_reference_files(reference_dir, selected_files)

        # Allow user to specify LLM or use default
        llm_choice = input(f"Enter LLM to use (ollama, openai, claude, groq) [default: {DEFAULT_LLM}]: ").strip().lower()
        llm = llm_choice if llm_choice else DEFAULT_LLM

        requirements_agent = RequirementsAgent()
        research_agent = ResearchAgent(llm=llm)
        documentation_agent = DocumentationAgent(llm=llm)
        reviewer_agent = ReviewerAgent(llm=llm)
        virtual_tester_agent = VirtualTesterAgent(llm=llm)
        overall_manager_agent = OverallManagerAgent()

        requirements_info = requirements_agent.gather_requirements()
        research_info = research_agent.perform_research(process_name)
        documentation = documentation_agent.create_documentation(
            process_name, research_info, requirements_info, reference_files_content)
        review_feedback = reviewer_agent.review_documentation(documentation)
        testing_feedback = virtual_tester_agent.test_documentation(documentation, audience_level)
        needs_revision = overall_manager_agent.evaluate_feedback(documentation, review_feedback, testing_feedback)

        iteration = 1
        while needs_revision:
            logger.info("Revision iteration: %d", iteration)
            documentation = documentation_agent.revise_documentation(documentation, testing_feedback)
            review_feedback = reviewer_agent.review_documentation(documentation)
            testing_feedback = virtual_tester_agent.test_documentation(documentation, audience_level)
            needs_revision = overall_manager_agent.evaluate_feedback(documentation, review_feedback, testing_feedback)
            iteration += 1

        output_dir = "output_documentation"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{process_name}_documentation.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(documentation)
        logger.info("Documentation saved to %s", output_file)

        history_entry = {
            "process_name": process_name,
            "audience_level": audience_level,
            "reference_files": selected_files,
            "documentation_file": output_file,
            "llm": llm,
        }
        save_history(history_entry)
    except Exception as e:
        logger.exception("An error occurred while creating a new task: %s", e)

def rerun_task():
    """Reruns a previously generated process documentation task."""
    try:
        history = load_history()
        if not history:
            logger.warning("No process history found.")
            print("No process history found.")
            return

        print("Previously documented processes:")
        for idx, entry in enumerate(history):
            print(f"{idx+1}. {entry['process_name']} (LLM used: {entry.get('llm', 'N/A')})")

        selected_idx = input("Enter the number of the process to rerun: ").strip()
        if not selected_idx.isdigit() or int(selected_idx) < 1 or int(selected_idx) > len(history):
            logger.error("Invalid selection.")
            print("Invalid selection.")
            return

        selected_entry = history[int(selected_idx) - 1]
        process_name = selected_entry['process_name']
        audience_level = selected_entry['audience_level']
        selected_files = selected_entry['reference_files']
        llm = selected_entry.get('llm', DEFAULT_LLM)

        reference_dir = input("Enter the directory containing reference files (press Enter to use previous): ").strip()
        if not reference_dir:
            reference_dir = os.path.dirname(selected_entry['documentation_file'])
        files = os.listdir(reference_dir)
        if not files:
            logger.warning("No files found in the specified directory.")
            return
        print("Available files:")
        for idx, file in enumerate(files):
            print(f"{idx+1}. {file}")
        selected_files_indices = input("Enter the numbers of the files to include as references (comma-separated, press Enter to use previous selection): ").strip()
        if not selected_files_indices:
            # Use previous selection
            pass
        else:
            selected_indices = [int(idx.strip()) - 1 for idx in selected_files_indices.split(",")]
            selected_files = [files[idx] for idx in selected_indices if 0 <= idx < len(files)]

        reference_files_content = parse_reference_files(reference_dir, selected_files)

        # Allow user to specify LLM or use previous
        llm_choice = input(f"Enter LLM to use (ollama, openai, claude, groq) [default: {llm}]: ").strip().lower()
        llm = llm_choice if llm_choice else llm

        requirements_agent = RequirementsAgent()
        research_agent = ResearchAgent(llm=llm)
        documentation_agent = DocumentationAgent(llm=llm)
        reviewer_agent = ReviewerAgent(llm=llm)
        virtual_tester_agent = VirtualTesterAgent(llm=llm)
        overall_manager_agent = OverallManagerAgent()

        requirements_info = requirements_agent.gather_requirements()
        research_info = research_agent.perform_research(process_name)
        documentation = documentation_agent.create_documentation(
            process_name, research_info, requirements_info, reference_files_content)
        review_feedback = reviewer_agent.review_documentation(documentation)
        testing_feedback = virtual_tester_agent.test_documentation(documentation, audience_level)
        needs_revision = overall_manager_agent.evaluate_feedback(documentation, review_feedback, testing_feedback)

        iteration = 1
        while needs_revision:
            logger.info("Revision iteration: %d", iteration)
            documentation = documentation_agent.revise_documentation(documentation, testing_feedback)
            review_feedback = reviewer_agent.review_documentation(documentation)
            testing_feedback = virtual_tester_agent.test_documentation(documentation, audience_level)
            needs_revision = overall_manager_agent.evaluate_feedback(documentation, review_feedback, testing_feedback)
            iteration += 1

        output_dir = "output_documentation"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{process_name}_documentation_rerun.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(documentation)
        logger.info("Documentation saved to %s", output_file)

        # Update history
        history_entry = {
            "process_name": process_name,
            "audience_level": audience_level,
            "reference_files": selected_files,
            "documentation_file": output_file,
            "llm": llm,
        }
        save_history(history_entry)
    except Exception as e:
        logger.exception("An error occurred while rerunning the task: %s", e)
