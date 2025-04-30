# app/reviewer.py

def analyze_code(code: str) -> str:
    """
    Dummy code analysis function.
    Just returns basic suggestions.
    """
    if not code.strip():
        return "No code provided."

    suggestions = []

    if "print" in code:
        suggestions.append("Consider using logging instead of print statements for production code.")

    if "==" in code and "if" in code:
        suggestions.append("Make sure to handle edge cases in conditionals.")

    if not suggestions:
        suggestions.append("The code looks fine.")

    return " ".join(suggestions)



