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

    # 🔴 HARD TASKS (IMPROVED)
    {
        "id": "hard_1",
        "description": "Ambiguous urgent infrastructure issue affecting users",
        "input": {
            "subject": "URGENT: Server issue affecting payments",
            "body": "Customers unable to complete transactions due to system instability",
            "sender": "ops@company.com"
        },
        "expected": {
            "category": "important",
            "priority": "high",
            "department": "engineering"
        }
    },
    {
        "id": "hard_2",
        "description": "Customer complaint with urgency and support handling required",
        "input": {
            "subject": "App not working - urgent help needed",
            "body": "I am unable to login and losing access to my data",
            "sender": "customer@gmail.com"
        },
        "expected": {
            "category": "important",
            "priority": "high",
            "department": "support"
        }
    }
]