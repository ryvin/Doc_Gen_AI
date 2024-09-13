# agents/overall_manager_agent.py

import logging

logger = logging.getLogger(__name__)

class OverallManagerAgent:
    """Agent that oversees the documentation process and evaluates feedback."""

    def __init__(self):
        pass

    def evaluate_feedback(
        self,
        documentation: str,
        review_feedback: str,
        testing_feedback: str
    ) -> bool:
        """Evaluates feedback to determine if documentation needs revision.

        Args:
            documentation: The current documentation.
            review_feedback: Feedback from the reviewer agent.
            testing_feedback: Feedback from the virtual tester agent.

        Returns:
            A boolean indicating whether the documentation needs revision.
        """
        logger.info("Evaluating feedback for possible revisions.")
        needs_revision = False

        # Simple heuristic to determine if revision is needed
        if "issues found" in review_feedback.lower() or "unclear" in testing_feedback.lower():
            needs_revision = True

        return needs_revision
