from google.adk.agents import ParallelAgent, LlmAgent, SequentialAgent

sentiment_classifier = LlmAgent(
    name="SentimentClassifier",
    instruction="Classify whether input data is positive, neutral, negative.",
    output_key="sentiment_results"
)

credibility_classifier = LlmAgent(
    name="CredibilityClassifier",
    instruction="Classify whether the credibility of the input data is high, medium, low.",
    output_key="credibility_results"
)

community_classifier = LlmAgent(
    name="CommunityClassifier",
    instruction="Assign each post to an online community or group.",
    output_key="community_results"
)

classification_agent = ParallelAgent(
    name="ClassificationAgent",
    sub_agents=[sentiment_classifier,
               credibility_classifier,
               community_classifier]
)

echo_chamber_agent = LlmAgent(
    name="EchoChamberAgent",
    instruction=(
        "Cluster posts into echo chambers based on ideology, subreddit, or network."
    ),
    output_key="echo_chamber_results"
)

# wrap everything into a sequential agent
classification_echo_pipeline = SequentialAgent(
    name="ClassificationandEchoPipeline",
    sub_agents=[
        classification_agent,
        echo_chamber_agent
    ]
)

class ClassificationAgent:
    def __init__(self):
        self.agent = classification_agent

    def run(self, input_data: dict) -> dict:
        """Run the classification pipeline on input data."""
        return self.agent.run(input_data)

class EchoChamberAgent:
    def __init__(self):
        self.agent = classification_echo_pipeline

    def run(self, input_data: dict) -> dict:
        """Run classification and echo chamber clustering sequentially."""
        return self.agent.run(input_data)

