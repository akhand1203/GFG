import os
import re
import json
import time
import requests

GFG_USERNAME = os.environ["GFG_USERNAME"]
GFG_CSRF_TOKEN = os.environ["GFG_CSRF_TOKEN"]
GFG_SESSION_TOKEN = os.environ["GFG_SESSION_TOKEN"]

LANG_EXT = {
    "C": "c", "C++": "cpp", "C++14": "cpp", "C++17": "cpp",
    "Java": "java", "Python": "py", "Python3": "py",
    "JavaScript": "js", "PHP": "php", "Kotlin": "kt",
    "Swift": "swift", "R": "r", "Go": "go",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.geeksforgeeks.org/",
    "x-csrftoken": GFG_CSRF_TOKEN,
}

COOKIES = {
    "csrftoken": GFG_CSRF_TOKEN,
    "sessionid": GFG_SESSION_TOKEN,
}

def sanitize(name):
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "-", name.strip())
    return name.lower()

def get_all_submissions():
    submissions = []
    page = 1
    while True:
        url = f"https://www.geeksforgeeks.org/api/v1/user/problems/submissions/?page={page}&user={GFG_USERNAME}"
        resp = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if resp.status_code != 200:
            print(f"Failed at page {page}: {resp.status_code}")
            break
        data = resp.json()
        results = data.get("results", [])
        if not results:
            break
        submissions.extend(results)
        print(f"Fetched page {page} — {len(results)} submissions")
        if not data.get("next"):
            break
        page += 1
        time.sleep(0.5)
    return submissions

def get_submission_code(problem_slug, submission_id):
    url = f"https://www.geeksforgeeks.org/api/v1/submissions/{submission_id}/"
    resp = requests.get(url, headers=HEADERS, cookies=COOKIES)
    if resp.status_code == 200:
        return resp.json().get("code", "")
    return None

def save_submissions(submissions):
    saved = 0
    for sub in submissions:
        if sub.get("verdict") not in ("Accepted", "AC"):
            continue

        problem_name = sub.get("problem_name", "unknown")
        topic = sub.get("topic_tag", "misc") or "misc"
        language = sub.get("language", "C++")
        sub_id = sub.get("id") or sub.get("submission_id")
        problem_slug = sub.get("slug", sanitize(problem_name))

        ext = LANG_EXT.get(language, "txt")
        topic_dir = sanitize(topic)
        filename = f"{sanitize(problem_name)}.{ext}"
        filepath = os.path.join("solutions", topic_dir, filename)

        if os.path.exists(filepath):
            print(f"Skipping (exists): {filepath}")
            continue

        code = get_submission_code(problem_slug, sub_id)
        if not code:
            code = sub.get("code", "")
        if not code:
            print(f"No code for: {problem_name}")
            continue

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"// Problem: {problem_name}\n")
            f.write(f"// Language: {language}\n")
            f.write(f"// GFG Link: https://www.geeksforgeeks.org/problems/{problem_slug}/\n\n")
            f.write(code)

        print(f"Saved: {filepath}")
        saved += 1
        time.sleep(0.3)

    print(f"\nDone! Saved {saved} accepted submissions.")

if __name__ == "__main__":
    print(f"Fetching submissions for: {GFG_USERNAME}")
    subs = get_all_submissions()
    print(f"Total submissions found: {len(subs)}")
    save_submissions(subs)
