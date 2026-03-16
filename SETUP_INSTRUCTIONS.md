# BRAINFRAME V2 — SETUP INSTRUCTIONS

Step by step. Do these in order.

---

## STEP 1 — Create the GitHub repos

Create four repos on GitHub:

1. `brainframe-public` — **public**
2. `brainframe-private` — **private**
3. `coinbeast` — **private** (may already exist)
4. `nightwatch` — **private** (may already exist)

No README, no license, no .gitignore — start empty.

---

## STEP 2 — Push the public repo files

The brainframe-public folder contains these files. Push them to your `brainframe-public` repo:

```
brainframe-public/
  GLOBAL_RULES.md
  STYLE_RULES.md
  MODEL_ROUTING.md
  ANTI_PATTERNS.md
  ENTRY_SCHEMAS.md
  FILE_CONVENTIONS.md
  CHANGELOG.md
  templates/
    BRAINFILE_TEMPLATE.md
    MASTER_TEMPLATE.md
    COINBEAST_BRAINFILE.md
  .github/
    workflows/
      sync.yml
```

Terminal commands:
```bash
cd brainframe-public
git init
git add .
git commit -m "init: Brainframe v2.0"
git branch -M main
git remote add origin https://github.com/bitcoinbrainsweb/brainframe-public.git
git push -u origin main
```

---

## STEP 3 — Edit the sync workflow

Before the GitHub Action will work, update two things in `.github/workflows/sync.yml`:

Replace both instances of `bitcoinbrainsweb` with your actual GitHub username.

Then commit and push the change:
```bash
git add .github/workflows/sync.yml
git commit -m "config: add github username to sync workflow"
git push
```

---

## STEP 4 — Create a GitHub Personal Access Token

The sync workflow needs permission to push to your private repos.

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Click "Generate new token"
3. Name it: `brainframe-sync`
4. Expiration: 1 year
5. Repository access: Select repositories → coinbeast, nightwatch
6. Permissions: Contents → Read and write
7. Generate and copy the token — you won't see it again

---

## STEP 5 — Add the token as a secret

1. Go to your `brainframe-public` repo on GitHub
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `SYNC_TOKEN`
5. Value: paste the token from Step 4
6. Save

---

## STEP 6 — Set up project repo structure

In your `coinbeast` repo, create the brainframe directory:

```bash
cd coinbeast
mkdir -p brainframe/specs brainframe/archive
```

Copy the Coinbeast brainfile from templates:
```bash
cp path/to/brainframe-public/templates/COINBEAST_BRAINFILE.md brainframe/brainfile.md
```

Update the raw URL in brainfile.md — replace `bitcoinbrainsweb` with your actual username.

Create the project files:
```bash
touch brainframe/MASTER.md
touch brainframe/DECISIONS.md
touch brainframe/KNOWN_UNKNOWNS.md
touch brainframe/SESSION_LOG.md
touch brainframe/HEALTH_CHECK.md
touch brainframe/TAXONOMY.md
touch brainframe/PROMPT_LOG.md
```

Copy content from the v1 Brainframe files we built earlier into these files — they already have the Coinbeast seed content.

Commit and push:
```bash
git add brainframe/
git commit -m "init: add Brainframe v2 project files"
git push
```

---

## STEP 7 — Test the GitHub Actions sync

Make a small change to any file in `brainframe-public` and push to main.

Go to the Actions tab in `brainframe-public` on GitHub. You should see the sync workflow run. After it completes, check that `coinbeast/brainframe/` was updated.

If it fails, check:
- The SYNC_TOKEN secret is set correctly
- The username in sync.yml matches your GitHub username
- The coinbeast and nightwatch repos exist

---

## STEP 8 — Set up Make automation

Make handles AI-proposed file updates → staging branch → Dave approves → merges to main.

1. Create a Make account at make.com if you don't have one
2. Create a new scenario
3. Build this flow:

```
Trigger: Webhook (receives AI session end payload)
  ↓
Parse payload (extract file updates, new entries, status changes)
  ↓
GitHub: Create branch "brainframe-update-YYYY-MM-DD" in brainframe-public
  ↓
GitHub: Update each file listed in payload
  ↓
GitHub: Create pull request to main with session summary as PR description
  ↓
Notify Dave (email or push notification): "Brainframe update ready for review"
```

4. Copy the webhook URL from Make
5. Add it to your AI session workflow — at session end, paste the payload into the webhook

When Dave receives the notification:
- Review the PR on GitHub
- Merge if correct
- GitHub Actions syncs to project repos automatically

---

## STEP 9 — Update brainfile URLs

In `brainframe/brainfile.md` in both coinbeast and nightwatch, update the raw URLs to point to your actual public repo:

```
https://raw.githubusercontent.com/YOUR_ACTUAL_USERNAME/brainframe-public/main/GLOBAL_RULES.md
```

---

## STEP 10 — First session test

Start a new Claude session. Paste the full contents of:
1. `coinbeast/brainframe/brainfile.md`
2. `coinbeast/brainframe/MASTER.md`

Claude should orient immediately without additional explanation. At the end of the session, run `summarize session` and use the output as the Make webhook payload.

---

## ONGOING WORKFLOW

**Starting a session:**
1. Paste brainfile.md contents
2. Paste MASTER.md contents
3. Load any spec files needed for the session topic
4. State what you want to accomplish

**During a session:**
- "remember this" → saves to correct file
- "load [file]" → brings in a spec file
- "status" → shows health check
- "refresh rules" → reloads global rules anytime

**Ending a session:**
1. Run "summarize session"
2. Run "what changed"
3. Copy the Make payload output
4. Paste into Make webhook
5. Review and merge the PR on GitHub

---

## NIGHTWATCH SETUP

When you are ready to add Brainframe to Nightwatch:

1. Create `nightwatch/brainframe/` directory structure (same as Step 6)
2. Use BRAINFILE_TEMPLATE.md as the base
3. Add Nightwatch-specific rules from the preserved rules file
4. The GitHub Actions sync will already be configured from Step 3

---

## RAW FILE URLS FOR AI SESSIONS

Bookmark these. Paste them when an AI asks for the global files:

```
GLOBAL_RULES:
https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/GLOBAL_RULES.md

STYLE_RULES:
https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/STYLE_RULES.md

MODEL_ROUTING:
https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/MODEL_ROUTING.md
```

Replace bitcoinbrainsweb once and save the updated URLs somewhere accessible.
