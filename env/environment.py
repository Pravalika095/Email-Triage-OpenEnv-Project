from env.models import Observation, Action, Reward
import random


class EmailEnv:
    def __init__(self):
        self.current_email = None
        self.steps = 0
        self.max_steps = 3

        # Sample email dataset
        self.emails = [
            {
                "email_id": "1",
                "subject": "Win a free iPhone!!!",
                "body": "Click here to claim your prize",
                "sender": "spam@promo.com",
                "expected": {
                    "category": "spam"
                }
            },
            {
                "email_id": "2",
                "subject": "Meeting at 5 PM",
                "body": "Team meeting scheduled today",
                "sender": "manager@company.com",
                "expected": {
                    "category": "work",
                    "priority": "medium"
                }
            },
            {
                "email_id": "3",
                "subject": "URGENT: Server Down",
                "body": "Production server crashed",
                "sender": "admin@company.com",
                "expected": {
                    "category": "important",
                    "priority": "high",
                    "department": "engineering"
                }
            }
        ]

    def reset(self):
        self.steps = 0
        self.current_email = random.choice(self.emails)

        return Observation(
            email_id=self.current_email["email_id"],
            subject=self.current_email["subject"],
            body=self.current_email["body"],
            sender=self.current_email["sender"]
        )

    def state(self):
        return self.current_email

    def step(self, action: Action):
        reward = 0.0
        done = False

        expected = self.current_email["expected"]

        # Reward logic
        if action.action_type == "classify":
            if action.value == expected.get("category"):
                reward += 0.4
            else:
                reward -= 0.2

        elif action.action_type == "set_priority":
            if action.value == expected.get("priority"):
                reward += 0.3
            else:
                reward -= 0.2

        elif action.action_type == "route":
            if action.value == expected.get("department"):
                reward += 0.3
            else:
                reward -= 0.2

        self.steps += 1

        if self.steps >= self.max_steps:
            done = True

        return (
            Observation(
                email_id=self.current_email["email_id"],
                subject=self.current_email["subject"],
                body=self.current_email["body"],
                sender=self.current_email["sender"]
            ),
            Reward(score=reward),
            done,
            {"steps": self.steps}
        )