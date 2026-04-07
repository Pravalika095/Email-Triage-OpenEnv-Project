from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action
import uvicorn

app = FastAPI()
env = EmailEnv()


# ✅ Root endpoint (fixes 404)
@app.get("/")
def home():
    return {
        "project": "Email Triage OpenEnv",
        "status": "running",
        "endpoints": {
            "reset": "/reset",
            "step": "/step",
            "state": "/state"
        },
        "description": "RL environment for email classification, prioritization, and routing"
    }


# 🔁 Reset environment
@app.api_route("/reset", methods=["GET", "POST"])
def reset():
    obs = env.reset()
    return obs.dict()


# ⚙️ Step execution (SAFE VERSION)
@app.api_route("/step", methods=["POST"])
def step(action: dict):
    try:
        act = Action(**action)
    except Exception as e:
        return {"error": f"Invalid action format: {str(e)}"}

    obs, reward, done, info = env.step(act)

    return {
        "observation": obs.dict(),
        "reward": reward.score,
        "done": done,
        "info": info
    }


# 📊 Get current state
@app.get("/state")
def state():
    return env.state().dict()


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()