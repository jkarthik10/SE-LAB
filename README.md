# Rock Paper Scissor Lab — Lab 4 VibeCoding

Name: J Karthik
SRN: PES1UG25AM804

A Pygame Rock–Paper–Scissors game with corrected scoring, a first-to-five match, adaptive CPU move selection, procedural move icons, and a short reveal animation.

## Requirements
- Python 3.10 or newer
- Pygame (`python -m pip install -r requirements.txt`)

## Run
```bash
python main.py
```
Click **ROCK**, **PAPER**, or **SCISSORS**. The first side to 5 points wins the match. At match end, press **R** to restart.

## Lab tasks implemented
1. Correct winner evaluation: Rock beats Scissors, Scissors beats Paper, Paper beats Rock; equal moves draw.
2. First-to-five match conclusion, winner banner, and R-to-restart.
3. Adaptive CPU: stores up to eight recent player choices and, when a repeated preference is detected, biases the CPU toward the counter-move. It remains partly random.
4. Procedural geometric icons and a short shaking/countdown reveal before round result.

## Manual validation checklist
- [ ] Rock vs Scissors awards player point; Scissors vs Paper awards player point; Paper vs Rock awards player point.
- [ ] Reverse combinations award CPU point; matching moves are draws.
- [ ] Score increments only for wins, not draws.
- [ ] First to 5 triggers match-over overlay and blocks further moves.
- [ ] Pressing R resets score and pattern history.
- [ ] Repeated player choices influence CPU selections over multiple rounds.
- [ ] Icons and reveal animation display; result remains visible for approximately 1.8 seconds.

## Lab submission
Place the actual before/after recordings and exported LLM chat history in `Lab-4/`. Videos must be recorded from your own machine. Make a separate Git commit for each task and push to your personal repository; do not open a pull request against the SETAPESU26 source repository.
