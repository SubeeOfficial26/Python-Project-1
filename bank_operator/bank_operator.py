from rich.console import Console
from rich.prompt import Prompt  # Add this import
from account.user import User

console = Console()

users = []  # This will store all users

def create_user():
    # Ask for user information
    name = Prompt.ask("Enter your name")  # Now this will work
    email = Prompt.ask("Enter your email")

    # Basic email validation
    if not is_valid_email(email):
        console.print("Invalid email format. Please try again.", style="bold red")
        return
    
    # Create a new User instance
    user = User(name, email)
    
    # Add the user to the list (or database)
    users.append(user)
    
    console.print(f"User {name} created successfully!", style="bold green")

def is_valid_email(email):
    # Simple email validation logic
    return "@" in email and "." in email

def list_users():
    if not users:
        console.print("No users found.", style="bold red")
        return

    # List all users
    table = Table(title="User List", title_style="bold magenta")
    table.add_column("Name", style="cyan", justify="center")
    table.add_column("Email", style="white")
    
    for user in users:
        table.add_row(user.name, user.email)
    
    console.print(table)
