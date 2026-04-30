# Impact_Analyser

## C Quest Academy (V1 Prototype)

Single-file web app prototype for a gamified C-learning experience focused on college beginners.

### Included in this build
- MCQ traps
- Parsons puzzle interaction
- Debug Detective challenge
- Mini code lab challenge
- Adaptive concept targeting using mastery scores
- 3-level Socratic hints
- XP, level, streak, and daily quest counter
- Light/Dark fantasy-like UI
- Guest mode persistence via localStorage
- Export/Import progress backup code

### Run locally
1. Start a local server:
   ```bash
   python3 -m http.server 8000
   ```
2. Open: `http://localhost:8000/index.html`

### GitHub Pages fix (important)
If the hosted URL still shows old `+` / `-` diff text, the Pages source is likely stale.

1. In GitHub repo settings, set **Pages → Build and deployment → Source = GitHub Actions**.
2. Push this branch so `.github/workflows/pages.yml` deploys the current `index.html`.
3. After deployment completes, hard refresh (`Ctrl+Shift+R` or `Cmd+Shift+R`).
