# Concrete Slump Test Management System

A command-line tool to record fresh-concrete slump results and compare them
with operator-entered project acceptance limits.

## Features
- Project, location, batch/ticket, truck, mix, and technician details
- Measured slump and specified minimum/maximum (inches)
- Automatic PASS / OUT OF RANGE classification
- Persistent CSV history and simple summary counts
- Field procedure reminder

## Files
- `main.py` — menu and data-entry workflow
- `test_manager.py` — record creation and classification
- `storage.py` — CSV storage
- `reports.py` — individual report and history
- `validators.py` — reusable input validation
- `procedure_checklist.md` — field reminder

## Run
Requires Python 3.10+; no third-party packages.
Run `python main.py` from this folder.

Records are saved to `data/slump_tests.csv`. Back up this file regularly.

## Engineering note
PASS/OUT OF RANGE only compares the measured value to the limits entered by
the operator. It is not an independent certification of ASTM or contract
compliance. Follow the current adopted ASTM C143/C143M edition and project
requirements. A slump test does not determine compressive strength.
