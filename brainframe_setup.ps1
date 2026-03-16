# Brainframe Setup Script
# Run this from inside your brainframe-public folder
# Right-click PowerShell -> Run as Administrator if needed

# Create folder structure
New-Item -ItemType Directory -Force -Path "templates"
New-Item -ItemType Directory -Force -Path ".github\workflows"

# Move template files into templates folder
$templateFiles = @("BRAINFILE_TEMPLATE.md", "COINBEAST_BRAINFILE.md", "MASTER_TEMPLATE.md")
foreach ($file in $templateFiles) {
    if (Test-Path $file) {
        Move-Item -Force $file "templates\$file"
        Write-Host "Moved $file to templates/"
    } else {
        Write-Host "WARNING: $file not found - skipping"
    }
}

# Download sync.yml directly from Claude outputs
# Since we can't fetch from Claude, create it here directly
$syncYml = @'
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
            brainframe-public/ nightwatch/brainframe/

      - name: Commit and push to nightwatch
        run: |
          cd nightwatch
          git config user.name "Brainframe Sync"
          git config user.email "brainframe@noreply.github.com"
          git add brainframe/
          git diff --staged --quiet || git commit -m "sync: brainframe-public updated $(date +%Y-%m-%d)"
          git push
'@

$syncYml | Out-File -FilePath ".github\workflows\sync.yml" -Encoding utf8
Write-Host "Created .github/workflows/sync.yml"

# Update COINBEAST_BRAINFILE.md with correct username
if (Test-Path "templates\COINBEAST_BRAINFILE.md") {
    (Get-Content "templates\COINBEAST_BRAINFILE.md") -replace 'YOUR_GITHUB_USERNAME', 'bitcoinbrainsweb' | Set-Content "templates\COINBEAST_BRAINFILE.md"
    Write-Host "Updated COINBEAST_BRAINFILE.md with correct username"
}

# Update SETUP_INSTRUCTIONS.md with correct username
if (Test-Path "SETUP_INSTRUCTIONS.md") {
    (Get-Content "SETUP_INSTRUCTIONS.md") -replace 'YOUR_GITHUB_USERNAME', 'bitcoinbrainsweb' -replace 'YOUR_USERNAME', 'bitcoinbrainsweb' | Set-Content "SETUP_INSTRUCTIONS.md"
    Write-Host "Updated SETUP_INSTRUCTIONS.md with correct username"
}

Write-Host ""
Write-Host "Done. Your folder structure is ready."
Write-Host ""
Write-Host "Next: open PowerShell in this folder and run the git commands to push to GitHub."
