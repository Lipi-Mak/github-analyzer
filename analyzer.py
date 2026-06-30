from collections import Counter
from datetime import datetime, timezone
from github_api import fetch_repositories

from scoring import (
    repo_score,
    language_score,
    star_score,
    fork_score,
    description_score,
    activity_score,
    popular_language_score
)


def analyze_profile(username):
    repos = fetch_repositories(username)
    if repos is None:
        return {
            "error": "GitHub user not found."
        }

    if len(repos) == 0:
        return {
            "error": "This user has no public repositories."
        }

    repo_names = []
    languages = []
    total_stars = 0
    total_forks = 0
    description_count = 0
    recent_activity = 0
    now = datetime.now(timezone.utc)

    for repo in repos:
        repo_names.append(repo["name"])

        if repo["language"]:
            languages.append(repo["language"])
        total_stars += repo["stargazers_count"]
        total_forks += repo["forks_count"]

        if repo["description"]:
            description_count += 1
        updated = datetime.strptime(
            repo["updated_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        ).replace(tzinfo=timezone.utc)

        days = (now - updated).days

        if days <= 180:
            recent_activity += 1

    language_counter = Counter(languages)

    score = 0
    score += repo_score(len(repo_names))
    score += language_score(len(language_counter))
    score += star_score(total_stars)
    score += fork_score(total_forks)
    score += description_score(description_count, len(repo_names))
    score += activity_score(recent_activity)
    score += popular_language_score(language_counter)
    score = min(score, 100)

    insights = []
    recommendations = []

    if len(repo_names) >= 10:
        insights.append("Good number of public repositories.")
    else:
        recommendations.append("Create more public repositories to showcase your skills.")

    if len(language_counter) >= 3:
        insights.append("Uses multiple programming languages.")
    else:
        recommendations.append("Try building projects in different programming languages.")

    if total_stars >= 10:
        insights.append("Projects have received community appreciation.")
    else:
        recommendations.append("Build unique projects that attract GitHub stars.")

    if description_count == len(repo_names):
        insights.append("Every repository has a description.")
    else:
        recommendations.append("Add descriptions to all repositories.")

    if recent_activity >= 3:
        insights.append("Recently active on GitHub.")
    else:
        recommendations.append("Stay active by updating projects regularly.")

    if "Python" in language_counter:
        insights.append("Strong Python presence.")

    if "JavaScript" not in language_counter:
        recommendations.append("Learning JavaScript can strengthen your profile.")

    return {
        "username": username,
        "score": score,
        "repositories": len(repo_names),
        "languages": dict(language_counter),
        "stars": total_stars,
        "forks": total_forks,
        "active": recent_activity,
        "insights": insights,
        "recommendations": recommendations
    }