param(
  [string]$SourcePath = "C:\Users\Lucas\.codex\skills",
  [string]$TargetPath = "skills"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

if (-not (Test-Path $SourcePath)) {
  throw "Source path not found: $SourcePath"
}

if (-not (Test-Path $TargetPath)) {
  New-Item -ItemType Directory -Path $TargetPath | Out-Null
}

# Mirror source skills to repository folder.
robocopy $SourcePath $TargetPath /MIR /R:2 /W:1 /NFL /NDL /NJH /NJS /NP | Out-Null

git add -A

git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
  Write-Output "No changes to commit."
  exit 0
}

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "sync skills $timestamp"
git push origin main

Write-Output "Skills synchronized and pushed."
