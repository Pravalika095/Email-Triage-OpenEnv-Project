tasks = [
    {
        "id": "easy",
        "description": "Classify a spam email",
        "input": {
            "subject": "Win a free iPhone!!!",
            "body": "Click here to claim",
            "sender": "spam@promo.com"
        },
        "expected": {
            "category": "spam"
        }
    },
    {
        "id": "medium",
        "description": "Classify and assign priority",
        "input": {
            "subject": "Meeting at 5 PM",
            "body": "Team sync scheduled",
            "sender": "manager@company.com"
        },
        "expected": {
            "category": "work",
            "priority": "medium"
        }
    },
    {
        "id": "hard",
        "description": "Full triage: classify, priority, route",
        "input": {
            "subject": "URGENT: Server Down",
            "body": "Production system failure",
            "sender": "admin@company.com"
        },
        "expected": {
            "category": "important",
            "priority": "high",
            "department": "engineering"
        }
    }
]