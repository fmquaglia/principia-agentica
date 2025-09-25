from langchain_core.tools import tool

@tool
def write_email(to: str, subject: str, content: str) -> str:
    """Write and send an email."""
    response = f"[tool write_email] Email sent to {to} with subject '{subject}'"
    print(response)
    return response

@tool
def schedule_meeting(
        attendees: list[str], subject: str, duration_minutes: int, preferred_day: str
) -> str:
    """Schedule a calendar meeting."""
    response = f"[tool schedule_meeting] Meeting '{subject}' scheduled for {preferred_day} with {len(attendees)} attendees"
    print(response)
    return response

@tool
def check_calendar_availability(day: str) -> str:
    """Check calendar availability for a given day."""
    response = f"[tool check_calendar_availability] Available times on {day}: 9:00 AM, 2:00 PM, 4:00 PM"
    print(response)
    return response

def tools():
    return [write_email, schedule_meeting, check_calendar_availability]
