# C Quest: Interactive C Learning Web App Plan

## 1) Product Vision
Build a playful, game-like web app that teaches C programming through active practice (not heavy theory): MCQs, bug hunts, drag-and-drop code ordering, line-by-line execution, and memory visualization.

## 2) Core Learning Principles
- **Learning by doing:** Every concept starts with an activity.
- **Micro-theory only:** 1–3 sentence concept cards when needed.
- **Immediate feedback:** Explain exactly what happened and why.
- **Adaptive mastery:** Track weak concepts and revisit with spaced repetition.
- **Socratic guidance:** Hints in question form before giving answers.

## 3) Learner Journey (Basic → Advanced)
1. Variables, types, I/O
2. Conditions and loops
3. Functions and scope
4. Arrays and strings
5. Pointers and memory model
6. Structs, dynamic memory, file I/O
7. Debugging and optimization challenges

Each level includes:
- Warmup MCQs (fast confidence check)
- Parsons puzzles (reorder shuffled lines)
- Debug Detective exercises (fix logical/semantic bugs)
- Mini boss challenge (combined concept task)

## 4) Feature Set Mapping (Your Requested Features)

### A. Adaptive Difficulty & Spaced Repetition
- Maintain concept mastery score per learner (0–100).
- Use weighted queue for review:
  - wrong/slow answers resurface sooner,
  - mastered concepts decay slower,
  - stale topics reappear periodically.
- Daily challenge generated from weak-topic queue + one stretch concept.

### B. Step-by-Step Code Runner
- Run C code instruction-by-instruction.
- UI timeline controls:
  - **Step In / Next / Continue / Reset**
- Side panels show:
  - current line highlight,
  - variable table before/after each step,
  - output console snapshot.

### C. Live Memory Visualizer
- Real-time diagrams:
  - stack frames,
  - heap allocations,
  - pointer arrows to addresses,
  - array blocks and string buffers.
- Hover reveals byte size, address, and value.

### D. Parsons Puzzles
- Drag-and-drop shuffled lines into correct order.
- Optional distractor lines for harder levels.
- Auto-check with semantic equivalence when possible (not only exact order).

### E. Debug Detective Mode
- Provide buggy programs with realistic mistakes:
  - off-by-one loops,
  - uninitialized pointer,
  - bad `scanf` format,
  - memory leak / double free,
  - logic mismatch in conditionals.
- Score by:
  - correctness,
  - attempts,
  - hint usage,
  - time.

### F. Unlockable Doodle Themes
- XP unlocks visual packs (space, jungle, cyber-lab, notebook doodles).
- Light/dark variants for each theme.
- Cosmetic rewards only (doesn’t impact learning fairness).

### G. Proactive Teacher Nudges
Before run/submit, detect common pitfalls:
- “You used `=` inside `if`. Did you mean `==`?”
- “This pointer may be uninitialized before dereference.”
- “Loop boundary suggests potential out-of-bounds.”

### H. Human-Like Error Explanations
Translate compiler/runtime errors to plain language:
- Technical error
- Human explanation
- Visual analogy
- Suggested next check

Example format:
- **Error:** Segmentation fault
- **Meaning:** Program touched memory it doesn’t own.
- **Analogy:** Entering a locked room without a key.
- **Try this:** Verify pointer init and bounds before dereference.

### I. Socratic Hint System
Three hint levels:
1. Directional question
2. Focused prompt on relevant line/concept
3. Near-solution scaffold

Never reveal full solution immediately unless user explicitly requests.

### J. Browser-Safe C Execution (WASM)
- Compile/execute C in sandboxed WebAssembly runtime.
- Hard limits:
  - CPU time
  - memory cap
  - disabled unsafe host access
- Deterministic, resettable environments per exercise.

### K. Cloud Sync & Progress Tracking
- User profile stores:
  - XP, streak, mastery map,
  - completed exercises,
  - preferred theme + light/dark mode,
  - spaced repetition queue state.
- Multi-device sync with conflict-safe timestamp merging.

## 5) UX & UI Direction
- **Style:** Creative, colorful doodle aesthetic (not minimal, still readable).
- **Accessibility:** Contrast-safe palettes, keyboard navigation, motion reduction.
- **Layout:**
  - Left: lesson flow
  - Center: code editor/runner
  - Right: memory + hints + objectives
- **Modes:** Light/Dark toggle globally persistent.

## 6) System Architecture (Recommended)

### Frontend
- React + TypeScript
- State: Zustand/Redux Toolkit
- UI: Tailwind + custom doodle component library
- Drag/drop: dnd-kit
- Code editor: Monaco
- Visuals: SVG/canvas layer for memory arrows and animated doodles

### Backend
- Node.js (NestJS or Express)
- PostgreSQL (users, progress, content metadata)
- Redis (session cache, challenge queues)
- Object storage for assets/themes

### Execution Engine
- WASM-based C toolchain service (isolated worker model)
- Event stream for step execution snapshots

### AI/Teaching Layer
- Hint + explanation service using prompt templates:
  - Socratic strategy
  - Error translator
  - Nudge detector

## 7) Data Model (High Level)
- `users`
- `concepts`
- `exercises`
- `attempts`
- `mastery_scores`
- `review_queue`
- `themes_unlocked`
- `streaks`

## 8) Gamification Loop
- XP per activity (first-try bonus)
- Streak multiplier (with grace tokens)
- Badges for skill clusters (Pointers Pro, Loop Master)
- Weekly quests (3 weak-spot fixes + 1 boss challenge)

## 9) Content Authoring Strategy
- Template-driven exercise creation:
  - concept tags,
  - difficulty tier,
  - expected misconceptions,
  - nudge rules,
  - hint tree.
- Start with 150–250 high-quality exercises across fundamentals.

## 10) Phased Delivery Roadmap

### Phase 1 (MVP, 6–8 weeks)
- Auth + progress save
- MCQs + Parsons + basic bug-fix exercises
- WASM compile/run
- Basic step runner (variables only)
- Light/dark + 2 doodle themes
- Initial adaptive review queue

### Phase 2 (8–12 weeks)
- Full memory visualizer (stack/heap/pointers)
- Advanced Debug Detective scenarios
- Socratic hint system v2
- Better analytics dashboard for learners

### Phase 3 (12+ weeks)
- Multiplayer challenge mode
- Teacher/mentor dashboards
- Community-generated puzzles with moderation

## 11) Quality & Metrics
Track:
- Time-to-first-correct per concept
- Retry reduction over sessions
- Weak-topic recovery rate
- 7-day and 30-day retention
- Hint dependency trend

Success target examples:
- 25% reduction in repeated pointer mistakes by week 3
- 40% of users maintain 7+ day learning streak

## 12) Risks & Mitigations
- **WASM runtime complexity:** Start with limited runtime features and expand.
- **Noisy AI hints:** Use constrained templates + rule checks.
- **Content bottleneck:** Build exercise generator tooling for author productivity.
- **UI overload:** Progressive disclosure (show advanced panels only when needed).

## 13) Next Actions (Immediate)
1. Finalize MVP scope (Phase 1 features only).
2. Create wireframes for 3 core screens:
   - Lesson screen
   - Debug Detective screen
   - Memory visualizer screen
3. Implement prototype with one full topic: **Pointers**.
4. Run pilot with 10 learners and measure comprehension gain.
