"""Helpers for social media agent."""
import os

def print_mention(processed_mention, mention):
    if processed_mention.needs_response:
        print(f"Responding to {processed_mention.sentiment} {processed_mention.product} feedback")
        print(f"  User: {mention}")
        print(f"  Response: {processed_mention.response}")
    else:
        print(f"Not responding to {processed_mention.sentiment} {processed_mention.product} post")
        print(f"  User: {mention}")

    if processed_mention.support_ticket_description:
        print(f"  Adding support ticket: {processed_mention.support_ticket_description}")
 