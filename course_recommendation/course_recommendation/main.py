COURSE_RULES = {
    "AI": {
        "GenAI": ["Prompt Engineering", "LLM Basics"],
        "ML": ["Python", "Statistics", "ML Algorithms"],
        "DL": ["Neural Networks", "Deep Learning"],
        "CV": ["Image Processing", "OpenCV"],
        "Agentic AI": ["Decision Systems", "Tool-Using Agents"]
    },

    "Engineering": {
        "Mechanical": {
            "Automotive": ["CAD", "CFD"],
            "Aerospace": ["CFD", "FEA"],
            "Manufacturing": ["CAM", "Process Planning"],
            "Robotics": ["CAD", "AI", "Autonomy"]
        }
    },

    "Software": {
        "DSA": ["Data Structures", "Algorithms"],
        "Development": ["Backend", "APIs", "Projects"],
        "System Design": ["Scalability", "Architecture"],
        "CP": ["Problem Solving", "Timed Practice"]
    },

    "Research": {
        "Analyst": ["Research Methods", "Data Analysis"],
        "Open": ["Paper Reading", "Domain Exploration"]
    }
}


def get_user_inputs():
    print("\n--- Course Recommendation System ---")

    goal = input("Enter your career goal (AI / Engineering / Software / Research): ")
    year = int(input("Enter your year of study (1-4): "))
    math_level = input("Math comfort level (Low / Medium / High): ")
    time_available = int(input("Weekly time availability (hours): "))

    return {
        "goal": goal,
        "year": year,
        "math_level": math_level,
        "time_available": time_available
    }


def apply_constraints(recommendations, inputs):
    filtered = recommendations.copy()

    if inputs["year"] == 1:
        filtered = filtered[:2]

    if inputs["math_level"] == "Low":
        filtered = [course for course in filtered if "Statistics" not in course]

    if inputs["time_available"] < 10:
        filtered = filtered[:2]

    return filtered


def goal_based_routing(inputs):
    goal = inputs["goal"]

    if goal not in COURSE_RULES:
        print("Invalid goal selected.")
        return

    print("\nAvailable specializations:")
    specializations = COURSE_RULES[goal].keys()
    for s in specializations:
        print("-", s)

    specialization = input("Choose a specialization: ")

    try:
        if goal == "Engineering":
            sub_domains = COURSE_RULES[goal][specialization]
            print("\nAvailable sub-domains:")
            for sd in sub_domains:
                print("-", sd)

            sub_choice = input("Choose a sub-domain: ")
            recommendations = sub_domains[sub_choice]

        else:
            recommendations = COURSE_RULES[goal][specialization]

    except KeyError:
        print("Invalid selection.")
        return

    final_recommendations = apply_constraints(recommendations, inputs)

    print("\n--- Recommended Learning Path ---")
    for course in final_recommendations:
        print("•", course)


def main():
    user_inputs = get_user_inputs()

    if user_inputs["time_available"] < 5:
        print("\nRecommendation: Focus on fundamentals only.")

    if user_inputs["math_level"] == "Low" and user_inputs["goal"] == "AI":
        print("Pre-requisite suggested: Math & Python Basics")

    goal_based_routing(user_inputs)


if __name__ == "__main__":
    main()
