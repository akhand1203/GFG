import os
import re
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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": f"https://www.geeksforgeeks.org/{GFG_USERNAME}/",
    "Origin": "https://www.geeksforgeeks.org",
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
        url = f"https://www.geeksforgeeks.org/api/v1/user/problems/submissions/?page={page}&user={GFG_USERNAME}&page_size=20"
        print(f"Fetching: {url}")
        resp = requests.get(url, headers=HEADERS, cookies=COOKIES)
        print(f"Status: {resp.status_code}")
        print(f"Response preview: {resp.text[:300]}")

        if resp.status_code != 200:
            print(f"Failed at page {page}: {resp.status_code}")
            break

        try:
            data = resp.json()
        except Exception as e:
            print(f"JSON parse error: {e}")
            print(f"Full response: {resp.text[:1000]}")
            break

        results = data.get("results", [])
        if not results:
            print("No more results.")
            break

        submissions.extend(results)
        print(f"Page {page}: {len(results)} submissions (total: {len(submissions)})")

        if not data.get("next"):
            break
        page += 1
        time.sleep(1)

    return submissions

def get_submission_code(submission_id):
    url = f"https://www.geeksforgeeks.org/api/v1/submissions/{submission_id}/"
    resp = requests.get(url, headers=HEADERS, cookies=COOKIES)
    if resp.status_code == 200:
        try:
            return resp.json().get("code", "")
        except Exception:
            pass
    return ""

def save_submissions(submissions):
    saved = 0
    for sub in submissions:
        verdict = sub.get("verdict", "") or sub.get("status", "")
        if verdict not in ("Accepted", "AC", "1", 1):
            continue

        problem_name = sub.get("problem_name") or sub.get("title") or "unknown"
        topic = sub.get("topic_tag") or sub.get("topic") or "misc"
        language = sub.get("language") or sub.get("lang") or "C++"
        sub_id = sub.get("id") or sub.get("submission_id")
        problem_slug = sub.get("slug") or sub.get("problem_slug") or sanitize(problem_name)

        ext = LANG_EXT.get(language, "txt")
        topic_dir = sanitize(str(topic))
        filename = f"{sanitize(problem_name)}.{ext}"
        filepath = os.path.join("solutions", topic_dir, filename)

        if os.path.exists(filepath):
            print(f"Skipping (exists): {filepath}")
            continue

        code = sub.get("code", "") or ""
        if not code and sub_id:
            code = get_submission_code(sub_id)
            time.sleep(0.5)

        if not code:
            print(f"No code found for: {problem_name}")
            continue

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"// Problem: {problem_name}\n")
            f.write(f"// Language: {language}\n")
            f.write(f"// GFG Link: https://www.geeksforgeeks.org/problems/{problem_slug}/\n\n")
            f.write(code)

        print(f"Saved: {filepath}")
        saved += 1

    print(f"\nDone! Saved {saved} accepted submissions.")

if __name__ == "__main__":
    print(f"Fetching submissions for: {GFG_USERNAME}")
    subs = get_all_submissions()
    print(f"Total submissions found: {len(subs)}")
    if subs:
        print("Sample submission keys:", list(subs[0].keys()))
        print("Sample submission:", subs[0])
    save_submissions(subs)
