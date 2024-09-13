# agents/requirements_agent.py

import logging

logger = logging.getLogger(__name__)

class RequirementsAgent:
    """Agent responsible for gathering business requirements and constraints."""

    def __init__(self):
        pass

    def gather_requirements(self) -> str:
        """Gathers business requirements from the user.

        Returns:
            A string containing the business requirements and constraints.
        """
        logger.info("Gathering business requirements.")
        requirements = input("Please enter any business requirements, compliance needs, or constraints: ")
        return requirements.strip()
