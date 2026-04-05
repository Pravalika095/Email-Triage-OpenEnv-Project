import os
from openai import OpenAI
from env.tasks import tasks
from env.grader import grade

# Optional API usage
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


# MAIN EXECUTION
if __name__ == "__main__":

    TASK_NAME = "email_triage"
    MODEL_NAME = os.getenv("MODEL_NAME", "rule_based")

    print(f"[START] task={TASK_NAME} env=openenv model={MODEL_NAME}")

    rewards = []
    steps = 0

    for i, task in enumerate(tasks, 1):

        # Get prediction
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

        # Grade
        score = grade(prediction, task["expected"])
        reward = float(score)
        done = i == len(tasks)

        rewards.append(reward)
        steps = i

        # Action string (for logging)
        action_str = str(prediction)

        print(
            f"[STEP] step={i} action={action_str} reward={reward:.2f} done={str(done).lower()} error=null"
        )

    # Final success
    success = sum(rewards) / len(rewards) > 0.5

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}"
    )