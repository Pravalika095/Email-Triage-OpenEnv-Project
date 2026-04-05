from pydantic import BaseModel
from typing import Optional


# Observation (State)
class Observation(BaseModel):
    email_id: str
    subject: str
    body: str
    sender: str
    
    # Agent-filled fields
    category: Optional[str] = None
    priority: Optional[str] = None
    department: Optional[str] = None


# Action (What agent does)
class Action(BaseModel):
    category: Optional[str] = None
    priority: Optional[str] = None
    department: Optional[str] = None


# Reward (Feedback)
class Reward(BaseModel):
    score: float