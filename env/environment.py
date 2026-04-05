from env.models import Observation, Action, Reward
import random


class EmailEnv:
    def __init__(self):
        self.current_email = None
        self.steps = 0
        self.max_steps = 1  # single-step decision (full action at once)

        # Expanded dataset (better realism)
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
            },
            {
                "email_id": "4",
                "subject": "Customer complaint urgent",
                "body": "App not working properly",
                "sender": "user@gmail.com",
                "expected": {
                    "category": "important",
                    "priority": "high",
                    "department": "support"
                }
            },
            {
                "email_id": "5",
                "subject": "Weekly progress report",
                "body": "Please review the report",
                "sender": "lead@company.com",
                "expected": {
                    "category": "work",
                    "priority": "medium"
                }
            }
        ]

    # 🔁 Reset environment
    def reset(self):
        self.steps = 0
        self.current_email = random.choice(self.emails)

        return Observation(
            email_id=self.current_email["email_id"],
            subject=self.current_email["subject"],
            body=self.current_email["body"],
            sender=self.current_email["sender"],
            category=None,
            priority=None,
            department=None
        )

    # 📊 Current state
    def state(self):
        return Observation(
            email_id=self.current_email["email_id"],
            subject=self.current_email["subject"],
            body=self.current_email["body"],
            sender=self.current_email["sender"],
            category=self.current_email.get("category"),
            priority=self.current_email.get("priority"),
            department=self.current_email.get("department")
        )

    # ⚙️ Step function
    def step(self, action: Action):
        expected = self.current_email["expected"]
        reward = 0.0

        # 🎯 Reward calculation
        if action.category == expected.get("category"):
            reward += 0.4

        if action.priority == expected.get("priority"):
            reward += 0.3

        if action.department == expected.get("department"):
            reward += 0.3

        # 📝 Update environment state
        self.current_email["category"] = action.category
        self.current_email["priority"] = action.priority
        self.current_email["department"] = action.department

        self.steps += 1
        done = self.steps >= self.max_steps

        return (
            Observation(
                email_id=self.current_email["email_id"],
                subject=self.current_email["subject"],
                body=self.current_email["body"],
                sender=self.current_email["sender"],
                category=action.category,
                priority=action.priority,
                department=action.department
            ),
            Reward(score=reward),
            done,
            {"steps": self.steps}
        )