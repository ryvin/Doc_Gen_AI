# agents/virtual_tester_agent.py

import logging
from utils.llm_utils import query_llm

logger = logging.getLogger(__name__)

class VirtualTesterAgent:
    """Agent that simulates following the documentation."""

    def __init__(self, llm: str = None):
        self.llm = llm  # Allows specifying a different LLM for this agent

    def test_documentation(self, documentation: str, audience_level: str) -> str:
        """Simulates testing the documentation.

        Args:
            documentation: The documentation to test.
            audience_level: The target audience level.

        Returns:
            A string containing the testing feedback.
        """
        logger.info("Testing documentation for audience level: %s", audience_level)

        prompt = f"""
You are simulating a {audience_level} user following the process documentation.

Documentation:
{documentation}

Simulate following each step and provide detailed feedback on the success and clarity of each step.

Highlight any issues or points of confusion.
"""

        testing_feedback = query_llm(prompt, llm=self.llm)
        return testing_feedback.strip()
