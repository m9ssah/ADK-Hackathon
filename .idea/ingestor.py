from google.adk.agents import SequentialAgent, ParallelAgent, LlmAgent

# sub-agents for fetching data
fetch_reddit_api = LlmAgent(name="RedditAPIFetcher", instruction="Fetch data from Reddit API.", output_key="reddit_data")
fetch_threads_api = LlmAgent(name="ThreadsAPIFetcher", instruction="Fetch data from Threads API.", output_key="threads_data")

# parallel agent for concurrent API calls
fetch_concurrently = ParallelAgent(
    name="ConcurrentFetch",
    subagents=[fetch_reddit_api, fetch_threads_api]
)

# agent to synthesize fetched data
synthesize = LlmAgent(
    name="Synthesize",
    instruction="Combine results from state keys 'reddit_data' and 'threads_data'."
)

ingestor = SequentialAgent(
    name="FetchAndSynthesize",
    sub_agents=[fetch_concurrently, synthesize]  # run parallel fetch, then synthesize data
)
