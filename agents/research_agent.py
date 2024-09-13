# agents/research_agent.py

import logging
from utils.llm_utils import query_llm
from utils.search_utils import perform_web_search

logger = logging.getLogger(__name__)

class ResearchAgent:
    """Agent responsible for performing research on the given topic."""

    def __init__(self, llm: str = None):
        self.llm = llm  # Allows specifying a different LLM for this agent

    def perform_research(self, topic: str) -> str:
        """Performs research on the given topic.

        Args:
            topic: The topic to research.

        Returns:
            A string containing the research summary.
        """
        logger.info("Performing research on: %s", topic)
        web_search_results = perform_web_search(topic)
        prompt = f"""
You are an expert researcher.

Based on the following web search results, provide a detailed summary about {topic}.

Web Search Results:
{web_search_results}
"""
        research_summary = query_llm(prompt, llm=self.llm)
        return research_summary.strip()
