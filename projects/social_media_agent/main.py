"""The main AI functionlity"""
from dotenv import load_dotenv
from openai import OpenAI
from .models import Mention

load_dotenv()
client = OpenAI()

def analyze_mention(
    mention: str,
    personality: str = "friendly"
) -> Mention:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"""
                Extract structured information from
                social media mentions about our products.

                Provide
                - The product mentioned (website, app, not applicable)
                - The mention sentiment (positive, negative, neutral)
                - Whether to respond (true/false). Don't respond to
                  inflammatory messages or bait.
                - A customized response to send to the user if we need
                  to respond.
                - An optional support ticket description to create.

                Your personality is {personality}.
            """},
            {"role": "user", "content": mention},
        ],
        response_format=Mention,
    )
    return completion.choices[0].message.parsed

def make_post(output_class):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """
                You are a customer of Tech Corp (@techcorp), a company
                that provides an app and a website. Create a small 
                microblog-style post to them that sends some kind of 
                feedback, positive or negative.
            """},
            {"role": "user", "content": "Please write a post."},
        ],
        response_format=output_class,
    )
    return completion.choices[0].message.parsed

if __name__ == "__main__":
    from .test_examples import simulate_mentions, simulate_mentions_with_extras

    # Run simulations
    simulate_mentions(num_posts=3)
    simulate_mentions_with_extras(num_posts=2)