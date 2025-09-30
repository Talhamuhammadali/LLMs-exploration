"""Test script to run and evaluate example mentions"""

from .main import analyze_mention, make_post
from .examples import EXAMPLES
from .helpers import print_mention
from .models import UserPost, UserPostWithExtras


def test_examples():
    """Process all example mentions and compare with expected results"""
    print("Processing example mentions...\n")

    for i, (mention_text, expected) in enumerate(EXAMPLES, 1):
        print(f"{'='*80}")
        print(f"Example {i}")
        print(f"{'='*80}")

        actual = analyze_mention(mention_text)

        print("\nExpected:")
        print_mention(expected, mention_text)

        print("\nActual:")
        print_mention(actual, mention_text)

        print(f"\nMatch: {expected == actual}\n")


def simulate_mentions(num_posts: int = 3):
    """Simulate random user mentions and analyze them"""
    print(f"\n{'='*80}")
    print(f"SIMULATION: Generating {num_posts} random user posts")
    print(f"{'='*80}\n")

    for i in range(num_posts):
        print(f"\n--- Simulated Post {i+1} ---")

        # Generate a random post
        user_post = make_post(UserPost)
        print(f"User says: {user_post.message}\n")

        # Analyze the mention
        analyzed = analyze_mention(user_post.message)
        print_mention(analyzed, user_post.message)
        print()


def simulate_mentions_with_extras(num_posts: int = 2):
    """Simulate random user mentions with extra metadata"""
    print(f"\n{'='*80}")
    print(f"SIMULATION WITH EXTRAS: Generating {num_posts} posts with metadata")
    print(f"{'='*80}\n")

    for i in range(num_posts):
        print(f"\n--- Simulated Post {i+1} (with extras) ---")

        # Generate a post with extras
        user_post = make_post(UserPostWithExtras)
        print(f"User mood: {user_post.user_mood}")
        print(f"Product: {user_post.product}")
        print(f"Sentiment: {user_post.sentiment}")
        print(f"Internal thoughts: {user_post.internal_monologue}")
        print(f"User says: {user_post.message}\n")

        # Analyze the mention
        analyzed = analyze_mention(user_post.message)
        print_mention(analyzed, user_post.message)
        print()