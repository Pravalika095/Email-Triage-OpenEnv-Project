import os
from openai import OpenAI
from env.tasks import tasks
from env.grader import grade

print("[START]")

results = []

# Try to use API (optional)
use_api = os.getenv("OPENAI_API_KEY") is not None

if use_api:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def simple_agent(task):
    subject = task["input"]["subject"].lower()
    prediction = {}

    if "free" in subject or "win" in subject:
        prediction["category"] = "spam"

    elif "meeting" in subject:
        prediction["category"] = "work"
        prediction["priority"] = "medium"

    elif "urgent" in subject or "server" in subject:
        prediction["category"] = "important"
        prediction["priority"] = "high"
        prediction["department"] = "engineering"

    return prediction


for task in tasks:
    print(f"[STEP] Running task: {task['id']}")

    if use_api:
        try:
            response = client.chat.completions.create(
                model=os.getenv("MODEL_NAME"),
                messages=[{"role": "user", "content": str(task)}]
            )
            prediction = eval(response.choices[0].message.content)
        except:
            prediction = simple_agent(task)
    else:
        prediction = simple_agent(task)

    score = grade(prediction, task["expected"])
    results.append(score)

    print(f"[STEP] Score: {score}")

final_score = sum(results) / len(results)

print(f"[END] Final Score: {final_score}")