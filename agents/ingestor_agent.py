from google.adk.agents import SequentialAgent, ParallelAgent, LlmAgent
from tools.reddit_scrapper import fetch_reddit_posts

"""
TODO: 
- fix up instructions so that they are more elaborate and clear
"""

# sub-agents for fetching data
fetch_reddit_api = LlmAgent(
    name="RedditAPIFetcher",
    instruction="Fetch data from Reddit API.",
    input_key=["topic"],
    output_key="reddit_data",
)
fetch_threads_api = LlmAgent(
    name="ThreadsAPIFetcher",
    instruction="Fetch data from Threads API.",
    input_key=["topic"],
    output_key="threads_data",
)

# parallel agent for concurrent API calls
fetch_concurrently = ParallelAgent(
    name="ConcurrentFetch", subagents=[fetch_reddit_api, fetch_threads_api]
)

# agent to synthesize fetched data
synthesize = LlmAgent(
    name="Synthesize",
    instruction="Combine results from state keys 'reddit_data' and 'threads_data'.",
)

ingestor = SequentialAgent(
    name="FetchAndSynthesize",
    sub_agents=[
        fetch_concurrently,
        synthesize,
    ],  # run parallel fetch, then synthesize data
)


class IngestorAgent:
    def __init__(self):
        self.agent = ingestor

    def run(self, input: dict) -> dict:
        """
        Runs the agent to fetch and synthesize data from Reddit and Threads.
        Args:
            input (dict): The topic to search for on Reddit and Threads.
        Returns:
            dict: Synthesized data from both sources.
        """
        self.agent.run(input)
