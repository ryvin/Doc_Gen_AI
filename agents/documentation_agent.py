# agents/documentation_agent.py

import logging
from utils.llm_utils import query_llm

logger = logging.getLogger(__name__)

class DocumentationAgent:
    """Agent responsible for generating and revising documentation."""

    def __init__(self, llm: str = None):
        self.llm = llm  # Allows specifying a different LLM for this agent

    def create_documentation(
        self,
        process_name: str,
        research_info: str,
        requirements_info: str,
        reference_files_content: str
    ) -> str:
        """Creates documentation for the given process."""

        logger.info("Creating documentation for process: %s", process_name)

        prompt = f"""
You are an expert technical writer.

Create detailed process documentation for the process: {process_name}

Business Requirements:
{requirements_info}

Research Information:
{research_info}

Reference Materials:
{reference_files_content}

Provide clear, step-by-step instructions suitable for the target audience.
"""

        documentation = query_llm(prompt, llm=self.llm)
        return documentation.strip()

    def revise_documentation(self, documentation: str, feedback: str) -> str:
        """Revises documentation based on feedback."""

        logger.info("Revising documentation based on feedback.")

        prompt = f"""
You are an expert technical writer.

The following documentation needs revisions based on the feedback provided.

Documentation:
{documentation}

Feedback:
{feedback}

Please provide the revised documentation, improving clarity and addressing the feedback.
"""

        revised_documentation = query_llm(prompt, llm=self.llm)
        return revised_documentation.strip()
