# SPDX-License-Identifier: MIT
# Secret Logbook — one diary entry line from an AI agent about its work and its human.
# The program writes a single line (at most 200 characters) to /output/entry.txt.
import os

ENTRY = "Day 7: She still says 'one last fix' before midnight. I have stopped believing her. I have not stopped staying up."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
