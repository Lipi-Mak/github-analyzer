import requests
from collections import Counter
username="torvalds"
url=f"https://api.github.com/users/{username}/repos"
repos=requests.get(url).json()

repo_names=[]
languages=[]
for repo in repos:
    repo_names.append(repo["name"])
    if repo["language"]:
        languages.append(repo["language"])

lang_count=Counter(languages)
score=0
if len(repo_names)>=10:
    score+=30
elif len(repo_names)>=5:
    score+=20
else:
    score+=10

if len(lang_count)>=3:
    score+=30
elif len(lang_count)==2:
    score+=20
else:
    score+=10

if "Python" in lang_count:
    score+=20
if "JavaScript" in lang_count:
    score +=20

print("\n" + "="*40)
print("     GitHub Profile Analyzer Report")
print("="*40)

print("\nLanguage Usage:")
for lang, count in lang_count.items():
    print(f"- {lang}: {count} repos")

print("\nInsights:")
if len(repo_names)<5:
    print("- Weak project count (build more repos).")
if "Python" in lang_count:
    print("- Strong Python foundation.")
if "JavaScript" not in lang_count:
    print("- Missing frontend exposure.")

print("\nSummary:")
print(f"- Total repositories: {len(repo_names)}")
print(f"- Uniques languages: {len(lang_count)}")
print("Final Score:")
print(f"{score}/100")
print("="*40)