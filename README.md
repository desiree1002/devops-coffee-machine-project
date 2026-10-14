# Coffee Machine Backend
# Author: Desiree Payoyo

Hello, this is my repository for the DevOps Continuous Assessment. For this project, I built a simple project called Coffee Maker to demonstrate core DevOps workflows such as Agile project tracking, issue management with DoR/DoD, git branching strategies, and unit testing.

## What's in here?
* **Core Logic (`coffee_maker.py`):** A Python class that tracks water, beans and milk levels, handles brewing logic (like pulling an espresso or a latte), and catches errors if you ran out of supplies.
* **Unit Tests (`test_coffee_maker.py`):** A test suite built with `pytest` that checks successful brewing paths and edge cases (like low water or milk exceptions).

## Git Branching Strategy
To keep things organised and simulate a real development environment, I'm using a **Feature Branch Workflow**:
* `main`: This is the main branch. I don't push directly here, it's reserved for stable code. The only exception was the initial repository setup (README.md and LICENCE.md).
* `feature/<issue-number>-<short-description>`: Every time I work on a task from the GitHub project board, I create a new branch (e.g. `feature/5-resource-validation`).
* **Pull Requests:** Changes are merged back into `main` using Pull Requests that link directly to their respective issues on the GitHub Board to have full traceability.

## How to Run the Tests
Make sure you have Python and `pytest` installed, then run the tests from your terminal with:

```bash
pytest test_coffee_maker.py
```

## CoffeeMaker Class
A simple class that tracks:
* water level
* beans level
* milk level
* waste bin full

And supports:
* brew_espresso()
* brew_latte()
* brew_cappuccino()
* refill_supplies()
* empty_waste_bin()

## Licence
See [LICENCE.md](LICENCE.md).