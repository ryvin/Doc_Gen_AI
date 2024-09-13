# agents/reviewer_agent.py

import logging
from utils.llm_utils import query_llm

logger = logging.getLogger(__name__)

class ReviewerAgent:
    """Agent responsible for reviewing the documentation."""

    def __init__(self, llm: str = None):
        self.llm = llm  # Allows specifying a different LLM for this agent

    def review_documentation(self, documentation: str) -> str:
        """Reviews the documentation for completeness and clarity.

        Args:
            documentation: The documentation to review.

        Returns:
            A string containing the review feedback.
        """
        logger.info("Reviewing documentation.")

        prompt = f"""
You are an expert reviewer.

Review the following documentation for completeness, clarity, and accuracy.

Documentation:
{documentation}

Provide feedback on any issues found and suggestions for improvement.
"""

        review_feedback = query_llm(prompt, llm=self.llm)
        return review_feedback.strip()
