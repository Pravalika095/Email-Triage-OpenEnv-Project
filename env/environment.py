from env.models import Observation, Action, Reward
import random


class EmailEnv:
    def __init__(self):
        self.current_email = None
        self.steps = 0
        self.max_steps = 1  # single-step decision

        # 🔥 Expanded realistic dataset (10 emails)
        self.emails = [
            {
                "email_id": "1",
                "subject": "Win a free iPhone!!!",
                "body": "Click here to claim your prize",
                "sender": "spam@promo.com",
                "expected": {"category": "spam"}
            },
            {
                "email_id": "2",
                "subject": "Meeting at 5 PM",
                "body": "Team meeting scheduled today",
                "sender": "manager@company.com",
                "expected": {"category": "work", "priority": "medium"}
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
                "expected": {"category": "work", "priority": "medium"}
            },
            {
                "email_id": "6",
                "subject": "Huge discount just for you",
                "body": "Buy now and save big!",
                "sender": "offers@deals.com",
                "expected": {"category": "spam"}
            },
            {
                "email_id": "7",
                "subject": "Bug in production system",
                "body": "Users reporting login failure",
                "sender": "devops@company.com",
                "expected": {
                    "category": "important",
                    "priority": "high",
                    "department": "engineering"
                }
            },
            {
                "email_id": "8",
                "subject": "Team outing plans",
                "body": "Let’s plan for weekend outing",
                "sender": "hr@company.com",
                "expected": {"category": "work", "priority": "low"}
            },
            {
                "email_id": "9",
                "subject": "Payment failed issue",
                "body": "Customer unable to complete transaction",
                "sender": "support@company.com",
                "expected": {
                    "category": "important",
                    "priority": "high",
                    "department": "support"
                }
            },
            {
                "email_id": "10",
                "subject": "Free coupons available",
                "body": "Grab your free coupons now",
                "sender": "promo@ads.com",
                "expected": {"category": "spam"}
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

        # 🎯 Reward calculation (strong + meaningful)
        if action.category == expected.get("category"):
            reward += 0.5

        if action.priority == expected.get("priority"):
            reward += 0.25

        if action.department == expected.get("department"):
            reward += 0.25

        # ❌ Slight penalty for totally wrong prediction
        if reward == 0:
            reward = -0.1

        # 📝 Update state
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