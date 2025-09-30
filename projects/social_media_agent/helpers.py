"""Helpers for social media agent."""

def print_mention(processed_mention, mention):
    if processed_mention.needs_response:
        print("="*80)
        print(f"Responding to {processed_mention.sentiment} {processed_mention.product} feedback")
        print(f"  User: {mention}")
        print("---")
        print(f"  Response: {processed_mention.response}")
    else:
        print("="*80)
        print(f"Not responding to {processed_mention.sentiment} {processed_mention.product} post")
        print(f"  User: {mention}")

    if processed_mention.support_ticket_description:
        print("\u26A0\uFE0F "*5)
        print(f"  Adding support ticket: {processed_mention.support_ticket_description}")
 