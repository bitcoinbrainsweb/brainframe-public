# PENDING: sync.yml update required

The updated sync.yml below cannot be committed via API (GitHub platform restriction on .github/workflows/ for public repos with fine-grained PATs).

**One-time action required:** Copy the content below and paste it at:
https://github.com/bitcoinbrainsweb/brainframe-public/edit/main/.github/workflows/sync.yml

---

```yaml
name: Sync Brainframe Public to Projects

on:
  push:
    branches:
      - main

jobs:
  sync-to-coinbeast:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout brainframe-public
        uses: actions/checkout@v3
        with:
          path: brainframe-public

      - name: Checkout coinbeast
        uses: actions/checkout@v3
        with:
          repository: bitcoinbrainsweb/coinbeast
          token: ${{ secrets.SYNC_TOKEN }}
          path: coinbeast

      - name: Sync brainframe files to coinbeast
        run: |
          rsync -av --delete \
            --exclude='.git' \
            --exclude='.github' \
            --exclude='templates/' \
            --exclude='MASTER.md' \
            --exclude='SESSION_LOG.md' \
            --exclude='DECISIONS.md' \
            --exclude='KNOWN_UNKNOWNS.md' \
            --exclude='HEALTH_CHECK.md' \
            --exclude='TAXONOMY.md' \
            --exclude='PROMPT_LOG.md' \
            brainframe-public/ coinbeast/brainframe/

      - name: Commit and push to coinbeast
        run: |
          cd coinbeast
          git config user.name "Brainframe Sync"
          git config user.email "brainframe@noreply.github.com"
          git add brainframe/
          git diff --staged --quiet || git commit -m "sync: brainframe-public updated $(date +%Y-%m-%d)"
          git push

  sync-to-nightwatch:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout brainframe-public
        uses: actions/checkout@v3
        with:
          path: brainframe-public

      - name: Checkout nightwatch
        uses: actions/checkout@v3
        with:
          repository: bitcoinbrainsweb/great-horn-aml-nightwatch
          token: ${{ secrets.SYNC_TOKEN }}
          path: nightwatch

      - name: Sync brainframe files to nightwatch
        run: |
          rsync -av --delete \
            --exclude='.git' \
            --exclude='.github' \
            --exclude='templates/' \
            --exclude='MASTER.md' \
            --exclude='SESSION_LOG.md' \
            --exclude='DECISIONS.md' \
            --exclude='KNOWN_UNKNOWNS.md' \
            --exclude='HEALTH_CHECK.md' \
            --exclude='TAXONOMY.md' \
            --exclude='PROMPT_LOG.md' \
            brainframe-public/ nightwatch/brainframe/

      - name: Commit and push to nightwatch
        run: |
          cd nightwatch
          git config user.name "Brainframe Sync"
          git config user.email "brainframe@noreply.github.com"
          git add brainframe/
          git diff --staged --quiet || git commit -m "sync: brainframe-public updated $(date +%Y-%m-%d)"
          git push

  sync-to-axiom:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout brainframe-public
        uses: actions/checkout@v3
        with:
          path: brainframe-public

      - name: Checkout axiom
        uses: actions/checkout@v3
        with:
          repository: bitcoinbrainsweb/axiom
          token: ${{ secrets.SYNC_TOKEN }}
          path: axiom

      - name: Sync brainframe files to axiom
        run: |
          mkdir -p axiom/brainframe
          rsync -av --delete \
            --exclude='.git' \
            --exclude='.github' \
            --exclude='templates/' \
            --exclude='MASTER.md' \
            --exclude='SESSION_LOG.md' \
            --exclude='DECISIONS.md' \
            --exclude='KNOWN_UNKNOWNS.md' \
            --exclude='HEALTH_CHECK.md' \
            --exclude='TAXONOMY.md' \
            --exclude='PROMPT_LOG.md' \
            brainframe-public/ axiom/brainframe/

      - name: Commit and push to axiom
        run: |
          cd axiom
          git config user.name "Brainframe Sync"
          git config user.email "brainframe@noreply.github.com"
          git add brainframe/
          git diff --staged --quiet || git commit -m "sync: brainframe-public updated $(date +%Y-%m-%d)"
          git push

  sync-to-web:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout brainframe-public
        uses: actions/checkout@v3
        with:
          path: brainframe-public

      - name: Checkout web
        uses: actions/checkout@v3
        with:
          repository: bitcoinbrainsweb/web
          token: ${{ secrets.SYNC_TOKEN }}
          path: web

      - name: Sync brainframe files to web
        run: |
          mkdir -p web/brainframe
          rsync -av --delete \
            --exclude='.git' \
            --exclude='.github' \
            --exclude='templates/' \
            --exclude='MASTER.md' \
            --exclude='SESSION_LOG.md' \
            --exclude='DECISIONS.md' \
            --exclude='KNOWN_UNKNOWNS.md' \
            --exclude='HEALTH_CHECK.md' \
            --exclude='TAXONOMY.md' \
            --exclude='PROMPT_LOG.md' \
            brainframe-public/ web/brainframe/

      - name: Commit and push to web
        run: |
          cd web
          git config user.name "Brainframe Sync"
          git config user.email "brainframe@noreply.github.com"
          git add brainframe/
          git diff --staged --quiet || git commit -m "sync: brainframe-public updated $(date +%Y-%m-%d)"
          git push

```
