"""Example mentions for testing the social media agent"""

from .models import Mention

# Example 1: Positive mention about app
MENTION_1 = "Just tried your app and wow! The interface is so smooth and intuitive. Been using it all day!"
EXPECTED_1 = Mention(
    product="app",
    sentiment="positive",
    needs_response=True,
    response="Thank you so much! We're thrilled to hear you're enjoying the app. Let us know if you have any feedback!",
    support_ticket_description=None
)

# Example 2: Negative mention about website - needs support
MENTION_2 = "Your website keeps crashing when I try to checkout. This is the third time today. Really frustrating!"
EXPECTED_2 = Mention(
    product="website",
    sentiment="negative",
    needs_response=True,
    response="We're sorry to hear about the checkout issues! Our team is looking into this right away. We'll reach out shortly to help resolve this.",
    support_ticket_description="User experiencing repeated crashes during checkout on website - 3 occurrences today"
)

# Example 3: Neutral inquiry about app
MENTION_3 = "Does your app support dark mode? Couldn't find the setting anywhere."
EXPECTED_3 = Mention(
    product="app",
    sentiment="neutral",
    needs_response=True,
    response="Yes! You can enable dark mode by going to Settings > Appearance > Dark Mode. Hope this helps!",
    support_ticket_description=None
)

# Example 4: Inflammatory/bait comment - should NOT respond
MENTION_4 = "Your company is a joke and your CEO is incompetent. Everything you make is garbage and you should shut down."
EXPECTED_4 = Mention(
    product="not_applicable",
    sentiment="negative",
    needs_response=False,
    response=None,
    support_ticket_description=None
)

# Example 5: Positive mention about website with minor suggestion
MENTION_5 = "Love the new website redesign! So much cleaner. Would be cool if you added a wishlist feature though."
EXPECTED_5 = Mention(
    product="website",
    sentiment="positive",
    needs_response=True,
    response="Thanks for the kind words! We appreciate the wishlist suggestion - I'll pass it along to our product team!",
    support_ticket_description="Feature request: wishlist functionality on website"
)

EXAMPLES = [
    (MENTION_1, EXPECTED_1),
    (MENTION_2, EXPECTED_2),
    (MENTION_3, EXPECTED_3),
    (MENTION_4, EXPECTED_4),
    (MENTION_5, EXPECTED_5),
]