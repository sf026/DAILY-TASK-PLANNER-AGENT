from flask import Flask, render_template, request
from crewai import Agent, Task, Crew, LLM

app = Flask(__name__)

# ---------- LLM ----------
llm = LLM(
    model=" ",
    api_key=" "
)

# ---------- AGENT ----------
planner_agent = Agent(
    role="Productivity Planner",
    goal="Organize daily tasks efficiently into a realistic plan",
    backstory="You are an expert in time management and productivity planning.",
    llm=llm,
    allow_delegation=False,
    verbose=False
)

# ---------- TASK ----------
daily_plan_task = Task(
    description=(
        "Create a simple and realistic daily plan for the following tasks:\n"
        "{tasks}\n\n"
        "Rules:\n"
        "- Arrange tasks logically\n"
        "- Assign approximate time slots\n"
        "- Keep the plan simple and practical\n"
        "- Output only the daily plan"
    ),
    expected_output="A clear daily schedule with time slots.",
    agent=planner_agent
)

# ---------- CREW ----------
daily_planner_crew = Crew(
    agents=[planner_agent],
    tasks=[daily_plan_task],
    verbose=False
)

# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def index():
    plan = None
    if request.method == "POST":
        user_tasks = request.form["tasks"]

        result = daily_planner_crew.kickoff(
            inputs={"tasks": user_tasks}
        )
        plan = result.raw

    return render_template("index.html", plan=plan)

if __name__ == "__main__":
    app.run(debug=True)
