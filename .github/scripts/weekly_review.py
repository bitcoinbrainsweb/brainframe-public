import json, base64, urllib.request, os, datetime

PAT = os.environ["GH_PAT"]
CLAUDE_KEY = os.environ["CLAUDE_API_KEY"]
REPO = "bitcoinbrainsweb/brainframe-public"
today = datetime.date.today().isoformat()

def gh_get(path):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {PAT}",
        "Accept": "application/vnd.github+json"
    })
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read())
        return base64.b64decode(d["content"]).decode(), d["sha"]

def gh_put(path, content, sha, message):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    payload = {"message": message, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), method="PUT",
        headers={"Authorization": f"token {PAT}", "Accept": "application/vnd.github+json",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

try:
    admin_log, _ = gh_get("docs/admin/ADMIN_LOG.md")
except:
    admin_log = "No ADMIN_LOG.md found."

try:
    admin_state, _ = gh_get("docs/admin/ADMIN_STATE.md")
except:
    admin_state = "No ADMIN_STATE.md found."

prompt = (
    f"You are running the weekly Brainframe self-improvement review for Dave Bradley.\n\n"
    f"Today is {today}. Review the last 7 days of ADMIN_LOG.md entries.\n\n"
    f"ADMIN_LOG.md (last 6000 chars):\n{admin_log[-6000:]}\n\n"
    f"ADMIN_STATE.md:\n{admin_state[:2000]}\n\n"
    "Scan for friction patterns:\n"
    "- Rules skipped or re-stated mid-session\n"
    "- Tasks requiring multiple attempts or corrections\n"
    "- Fallback-to-memory incidents (SHA errors, stale reads, 409 conflicts)\n"
    "- Repeated re-explanations of context Dave already provided\n"
    "- Quitchat skipped or incomplete\n"
    "- ASSUMED labels later corrected\n"
    "- Skills triggered late or missed\n\n"
    "Produce max 5 suggestions ranked by impact. Each must:\n"
    "- Name the specific pattern observed with log entry date if possible\n"
    "- Target a named rule, skill, file, or workflow (no generic advice)\n"
    "- Propose a concrete specific change\n"
    "- Estimate effort: Low / Medium / High\n\n"
    "Return ONLY this markdown, no preamble:\n\n"
    f"## Week of {today} -- Sunday Review\n\n"
    "| # | Pattern Observed | Proposed Change | Effort |\n"
    "|---|-----------------|-----------------|--------|\n"
    "| 1 | ... | ... | Low |\n\n"
    f"Generated: {today}\n"
)

payload = json.dumps({
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 1500,
    "messages": [{"role": "user", "content": prompt}]
}).encode()

req = urllib.request.Request(
    "https://api.anthropic.com/v1/messages",
    data=payload,
    headers={
        "x-api-key": CLAUDE_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
    suggestion = data["content"][0]["text"]

print("Claude response:")
print(suggestion)

try:
    current, sha = gh_get("docs/admin/IMPROVEMENT_SUGGESTIONS.md")
except:
    current = "# Brainframe Improvement Suggestions\nWeekly self-improvement review log.\n\n---\n"
    sha = None

updated = current.rstrip() + "\n\n" + suggestion + "\n\n---\n"
gh_put("docs/admin/IMPROVEMENT_SUGGESTIONS.md", updated, sha,
       f"chore: weekly self-improvement review {today}")
print("Done. Written to IMPROVEMENT_SUGGESTIONS.md")
