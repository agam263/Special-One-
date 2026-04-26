import os
import random
import datetime
from datetime import timedelta
import subprocess

# Number of commits to generate
NUM_COMMITS = 995

# Start date (e.g., 6 months ago)
end_date = datetime.datetime.now()
start_date = end_date - timedelta(days=180)

messages = [
    "chore: update configuration",
    "fix: resolve minor bug",
    "feat: improve performance",
    "refactor: code cleanup",
    "style: format code",
    "docs: update documentation",
    "chore: dependency updates",
    "fix: typo in comments",
    "test: add unit tests",
    "chore: tweak build script"
]

print(f"Generating {NUM_COMMITS} commits...")

for i in range(NUM_COMMITS):
    # Random date between start_date and end_date
    random_days = random.randint(0, 180)
    random_seconds = random.randint(0, 86400)
    commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    
    date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
    
    msg = f"{random.choice(messages)} (iteration {i})"
    
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    
    subprocess.run(['git', 'commit', '--allow-empty', '-m', msg], env=env, stdout=subprocess.DEVNULL)

print("Pushing to GitHub...")
subprocess.run(['git', 'push', 'origin', 'main'])
print("Done!")
