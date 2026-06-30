def repo_score(repo_count):
    if repo_count >= 20:
        return 20
    elif repo_count >= 10:
        return 15
    elif repo_count >= 5:
        return 10
    return 5


def language_score(language_count):
    if language_count >= 5:
        return 15
    elif language_count >= 3:
        return 10
    return 5


def star_score(stars):
    if stars >= 50:
        return 15
    elif stars >= 10:
        return 10
    elif stars > 0:
        return 5
    return 0


def fork_score(forks):
    if forks >= 20:
        return 10
    elif forks >= 5:
        return 7
    elif forks > 0:
        return 4
    return 0


def description_score(with_description, total_repos):
    if total_repos == 0:
        return 0
    if with_description == total_repos:
        return 10
    elif with_description >= total_repos // 2:
        return 7
    return 0


def activity_score(active_repos):

    if active_repos >= 5:
        return 10
    elif active_repos >= 2:
        return 7
    return 0


def popular_language_score(language_counter):
    popular = 0
    if "Python" in language_counter:
        popular += 1
    if "JavaScript" in language_counter:
        popular += 1
    if "Java" in language_counter:
        popular += 1
    if popular == 3:
        return 10
    elif popular == 2:
        return 7
    elif popular == 1:
        return 5
    return 0