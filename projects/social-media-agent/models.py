"""Models for """
from pydantic import BaseModel
from typing import Optional, Literal

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
    
    
class Mention(BaseModel):
    # The sentiment and product email is for
    product: Literal['app', 'website', 'not_applicable']
    sentiment: Literal['positive', 'negative', 'neutral']

    # Model can choose to respond to the user
    needs_response: bool
    response: Optional[str]

    # If a support ticket is needed
    support_ticket_description: Optional[str]