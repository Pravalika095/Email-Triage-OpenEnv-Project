import os
from openai import OpenAI
from env.tasks import tasks
from env.grader import grade

# Optional API usage
use_api = os.getenv("OPENAI_API_KEY") is not None

if use_api:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# 🤖 Improved rule-based agent
def simple_agent(task):
    subject = task["input"]["subject"].lower()
    body = task["input"]["body"].lower()

    prediction = {
        "category": None,
        "priority": None,
        "department": None
    }

    # 🟢 Spam detection
    if "free" in subject or "win" in subject or "lottery" in subject:
        prediction["category"] = "spam"

    # 🟡 Work emails
    elif "meeting" in subject or "report" in subject or "progress" in subject:
        prediction["category"] = "work"
        prediction["priority"] = "medium"

    # 🔴 Important / urgent
    elif (
        "urgent" in subject
        or "server" in subject
        or "down" in subject
        or "complaint" in subject
        or "not working" in body
    ):
        prediction["category"] = "important"
        prediction["priority"] = "high"

        # routing logic
        if "server" in subject or "system" in body:
            prediction["department"] = "engineering"
        else:
            prediction["department"] = "support"

    return prediction


# 🚀 MAIN EXECUTION
if __name__ == "__main__":

    TASK_NAME = "email_triage"
    MODEL_NAME = os.getenv("MODEL_NAME", "rule_based")

    print(f"[START] task={TASK_NAME} env=openenv model={MODEL_NAME}")

    rewards = []
    steps = 0

    for i, task in enumerate(tasks, 1):

        # 🔁 Get prediction
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

        # 🎯 Grade prediction
        score = grade(prediction, task["expected"])
        reward = float(score)
        done = i == len(tasks)

        rewards.append(reward)
        steps = i

        # 🧾 Log action (important for evaluation)
        print(
            f"[STEP] step={i} action={prediction} reward={reward:.2f} done={str(done).lower()} error=null"
        )

    # ✅ Final success condition
    success = (sum(rewards) / len(rewards)) >= 0.7

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}"
    )