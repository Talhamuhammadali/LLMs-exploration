"""Models for """
from pydantic import BaseModel
from typing import Optional, Literal, List

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
    
    
class Mention(BaseModel):
    product: Literal['app', 'website', 'not_applicable']
    sentiment: Literal['positive', 'negative', 'neutral']
    needs_response: bool
    response: Optional[str]
    support_ticket_description: Optional[str]

class UserPost(BaseModel):
    message: str
class UserPostWithExtras(BaseModel):
    user_mood: Literal["awful", "bad", "evil"]
    product: Literal['app', 'website', 'not_applicable']
    sentiment: Literal['positive', 'negative', 'neutral']
    internal_monologue: List[str]
    message: str