# Lab 4 — VibeCoding Prompts and Task Log

Use these prompts as the task-by-task prompt record. Review and run the code after each change; keep each task in a separate Git commit.

## Task 1 — Fix inverted outcome evaluation
**Prompt:** Inspect `game/game_engine.py` and correct the winner logic. Rock must beat Scissors, Scissors must beat Paper, Paper must beat Rock, and identical choices must be a draw. Keep the scoring change limited to this task and provide a small test matrix for all nine combinations.

**Review checklist:** Test all nine combinations; verify only the winner receives a point and draws do not change scores.

## Task 2 — First-to-X match state
**Prompt:** Add a first-to-five match state. When either side reaches five points, stop accepting moves, display the match winner and final score, and tell the player to press R to reset the match. Reset both scores and round state on restart.

**Review checklist:** Verify the match ends at five, clicks are ignored after game over, and R fully resets the game.

## Task 3 — Adaptive CPU pattern tracking
**Prompt:** Replace purely random CPU selection with a lightweight adaptive strategy. Track a bounded history of the player's recent moves. When one move is repeated frequently, bias the CPU toward the move that defeats it, while retaining randomness so the strategy is not perfectly predictable. Explain the heuristic and review edge cases when there is insufficient history.

**Review checklist:** Verify early rounds remain random, history is bounded, and a clear repeated preference increases counter-move selection.

## Task 4 — Procedural icons and reveal animation
**Prompt:** Replace plain-text-only move displays with procedural Pygame geometry for rock, paper, and scissors. Add a brief synchronized shake/countdown reveal before showing the result. Preserve the 1.8-second result display and ensure the animation does not block event processing.

**Review checklist:** Verify all three icons render, animation is time-based, window close remains responsive, and result timing is preserved.

## Final verification prompt
**Prompt:** Review the entire project against the README tasks. Identify defects, check scoring and match-state transitions, verify restart behaviour, inspect the adaptive heuristic, and provide a manual test checklist. Do not claim a test passed unless it was actually run.

## Git commit plan
```bash
git add game/game_engine.py
git commit -m "Fix rock paper scissors winner evaluation"
git add game/game_engine.py
git commit -m "Add first-to-five match victory state"
git add game/game_engine.py
git commit -m "Add adaptive CPU pattern tracking"
git add game/game_engine.py
git commit -m "Add procedural move icons and reveal animation"
```
If multiple tasks modify the same file, stage only the relevant changes before each commit; do not create all four commits from one final snapshot and imply each represented a separate incremental implementation.
