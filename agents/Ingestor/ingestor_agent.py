from google.adk.agents import SequentialAgent, ParallelAgent, LlmAgent
from tools.reddit_scrapper import fetch_reddit_posts
from agents.Ingestor import prompt
"""
TODO: 
- fix up instructions so that they are more elaborate and clear
"""

# sub-agents for fetching data
fetch_reddit_api = LlmAgent(
    model="gemini-2.5-flash",
    name="RedditAPIFetcher",
    instruction="Fetch data from Reddit API.",
    input_key=["topic"],
    output_key="reddit_data",
)
fetch_threads_api = LlmAgent(
    model="gemini-2.5-flash",
    name="ThreadsAPIFetcher",
    instruction="Fetch data from Threads API.",
    input_key=["topic"],
    output_key="threads_data",
)

# parallel agent for concurrent API calls
fetch_concurrently = ParallelAgent(
    model="gemini-2.5-flash",
    name="ConcurrentFetch",
    instruction="Fetch data from both Reddit and Threads APIs concurrently.", 
    subagents=[fetch_reddit_api, fetch_threads_api]
)

# agent to synthesize fetched data
synthesize = LlmAgent(
    model="gemini-2.5-flash",
    name="Synthesize",
    instruction=prompt.SYNTHESIZE_AGENT_INSTR,
)

ingestor = SequentialAgent(
    model="gemini-2.5-flash",
    name="FetchAndSynthesize",
    description="Fetch data from Reddit and Threads APIs, then synthesize the results.",
    instruction=prompt.INGESTOR_AGENT_INSTR,
    sub_agents=[
        fetch_concurrently,
        synthesize,
    ],  # run parallel fetch, then synthesize data
)
