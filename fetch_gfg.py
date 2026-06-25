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

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "x-requested-with": "XMLHttpRequest",
    "x-csrftoken": GFG_CSRF_TOKEN,
    "Referer": f"https://www.geeksforgeeks.org/{GFG_USERNAME}/",
    "Origin": "https://www.geeksforgeeks.org",
})
SESSION.cookies.set("csrftoken", GFG_CSRF_TOKEN, domain=".geeksforgeeks.org")
SESSION.cookies.set("sessionid", GFG_SESSION_TOKEN, domain=".geeksforgeeks.org")

def sanitize(name):
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "-", name.strip())
    return name.lower()

def get_all_submissions():
    submissions = []
    page = 1
    while True:
        url = f"https://www.geeksforgeeks.org/api/v1/user/problems/submissions/?page={page}&user={GFG_USERNAME}&page_size=20"
        print(f"Fetching page {page}...")
        resp = SESSION.get(url)
        print(f"Status: {resp.status_code} | Content-Type: {resp.headers.get('Content-Type','')}")

        if resp.status_code != 200:
            print(f"Error: {resp.status_code}")
            break

        if "text/html" in resp.headers.get("Content-Type", ""):
            print("Got HTML response — trying profile API instead...")
            break

        try:
            data = resp.json()
            print(f"Keys in response: {list(data.keys())}")
        except Exception as e:
            print(f"JSON error: {e} | Response: {resp.text[:500]}")
            break

        results = data.get("results", [])
        if not results:
            print("No results on this page.")
            break

        submissions.extend(results)
        print(f"Page {page}: {len(results)} submissions (total: {len(submissions)})")

        if not data.get("next"):
            break
        page += 1
        time.sleep(1)

    return submissions

def get_submissions_via_profile():
    """Fallback: scrape submissions from public profile API"""
    submissions = []
    page = 1
    while True:
        url = f"https://www.geeksforgeeks.org/api/v1/user/{GFG_USERNAME}/practice-tracks/?page={page}"
        print(f"Trying profile API page {page}: {url}")
        resp = SESSION.get(url)
        print(f"Status: {resp.status_code} | CT: {resp.headers.get('Content-Type','')}")
        if resp.status_code != 200 or "text/html" in resp.headers.get("Content-Type", ""):
            print(f"Response: {resp.text[:300]}")
            break
        try:
            data = resp.json()
            print(f"Keys: {list(data.keys())}")
            results = data.get("results", data.get("data", []))
            if not results:
                break
            submissions.extend(results)
            if not data.get("next"):
                break
            page += 1
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e} | {resp.text[:300]}")
            break
    return submissions

def get_solved_problems():
    """Get list of solved problems from user profile"""
    url = f"https://www.geeksforgeeks.org/api/v1/user/{GFG_USERNAME}/problems-solved/"
    print(f"Fetching solved problems: {url}")
    resp = SESSION.get(url)
    print(f"Status: {resp.status_code} | CT: {resp.headers.get('Content-Type','')}")
    if resp.status_code == 200 and "application/json" in resp.headers.get("Content-Type", ""):
        try:
            data = resp.json()
            print(f"Keys: {list(data.keys())}")
            print(f"Preview: {str(data)[:500]}")
            return data
        except Exception as e:
            print(f"JSON error: {e}")
    print(f"Response: {resp.text[:500]}")
    return {}

def save_submissions(submissions):
    saved = 0
    for sub in submissions:
        verdict = sub.get("verdict") or sub.get("status") or sub.get("result") or ""
        if str(verdict) not in ("Accepted", "AC", "1", "Correct"):
            continue

        problem_name = sub.get("problem_name") or sub.get("title") or sub.get("question_title") or "unknown"
        topic = sub.get("topic_tag") or sub.get("topic") or sub.get("category") or "misc"
        language = sub.get("language") or sub.get("lang") or "cpp"
        sub_id = sub.get("id") or sub.get("submission_id")
        problem_slug = sub.get("slug") or sub.get("problem_slug") or sanitize(problem_name)
        code = sub.get("code") or sub.get("solution") or ""

        if not code and sub_id:
            code_resp = SESSION.get(f"https://www.geeksforgeeks.org/api/v1/submissions/{sub_id}/")
            if code_resp.status_code == 200:
                try:
                    code = code_resp.json().get("code", "")
                except Exception:
                    pass
            time.sleep(0.3)

        if not code:
            print(f"No code for: {problem_name}")
            continue

        ext = LANG_EXT.get(language, "txt")
        topic_dir = sanitize(str(topic))
        filename = f"{sanitize(problem_name)}.{ext}"
        filepath = os.path.join("solutions", topic_dir, filename)

        if os.path.exists(filepath):
            print(f"Skipping (exists): {filepath}")
            continue

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"// Problem: {problem_name}\n")
            f.write(f"// Language: {language}\n")
            f.write(f"// GFG: https://www.geeksforgeeks.org/problems/{problem_slug}/\n\n")
            f.write(code)

        print(f"Saved: {filepath}")
        saved += 1

    print(f"\nDone! Saved {saved} submissions.")

if __name__ == "__main__":
    print(f"=== Fetching submissions for: {GFG_USERNAME} ===")

    # Try primary submissions API
    subs = get_all_submissions()

    # Fallback: try profile API
    if not subs:
        print("\n--- Trying profile API fallback ---")
        subs = get_submissions_via_profile()

    # Fallback: try solved problems endpoint
    if not subs:
        print("\n--- Trying solved problems endpoint ---")
        data = get_solved_problems()

    print(f"\nTotal submissions found: {len(subs)}")
    if subs:
        print(f"Sample keys: {list(subs[0].keys())}")
        print(f"Sample entry: {subs[0]}")
        save_submissions(subs)
    else:
        print("No submissions retrieved. Check logs above for the correct API response structure.")
