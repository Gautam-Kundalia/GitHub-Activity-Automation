import os
import datetime
import random

# Set repository path (update this to your cloned repo location)
repo_path = "C:\Users\gauta\OneDrive\Desktop\GitHub-Activity-Automation"

# Move to the repository directory
os.chdir(repo_path)

# Generate a random message and update a file
with open("activity.txt", "a") as file:
    file.write(f"Commit on {datetime.datetime.now()}\n")

# Run Git commands
os.system("git add activity.txt")
os.system(f'git commit -m "Automated commit: {datetime.datetime.now()}"')
os.system("git push origin main")
