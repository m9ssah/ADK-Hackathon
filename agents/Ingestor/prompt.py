"""Prompts for the Ingestor agent and its sub-agents."""

INGESTOR_AGENT_INSTR = "Fetch and synthesize data from Reddit and Threads APIs."

SYNTHESIZE_AGENT_INSTR = (
    "Combine results from state keys 'reddit_data' and 'threads_data'."
)
