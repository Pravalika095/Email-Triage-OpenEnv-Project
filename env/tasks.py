tasks = [

    # 🟢 EASY TASKS
    {
        "id": "easy_1",
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
        "id": "easy_2",
        "description": "Detect promotional spam",
        "input": {
            "subject": "Congratulations! You won a lottery",
            "body": "Claim your prize now",
            "sender": "lottery@spam.com"
        },
        "expected": {
            "category": "spam"
        }
    },

    # 🟡 MEDIUM TASKS
    {
        "id": "medium_1",
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
        "id": "medium_2",
        "description": "Work-related email with normal urgency",
        "input": {
            "subject": "Weekly progress report",
            "body": "Please review the attached report",
            "sender": "lead@company.com"
        },
        "expected": {
            "category": "work",
            "priority": "medium"
        }
    },

    # 🔴 HARD TASKS
    {
        "id": "hard_1",
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
    },
    {
        "id": "hard_2",
        "description": "Customer complaint requiring support handling",
        "input": {
            "subject": "App not working - urgent help needed",
            "body": "I am unable to login to my account",
            "sender": "customer@gmail.com"
        },
        "expected": {
            "category": "important",
            "priority": "high",
            "department": "support"
        }
    }
]