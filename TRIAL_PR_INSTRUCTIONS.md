# Make one genuine trial PR

This ZIP is a ready-made trial repository working tree with intentional bugs. A hosted pull request cannot be pre-created without access to your GitHub account, so use the steps below to create a real PR in a new repository.

## Steps
1. On GitHub, create an empty repository named `minishop-review-trial`. Do not initialize it with a README.
2. Extract this ZIP and open PowerShell inside the extracted `minishop-review-trial` folder.
3. Replace `YOUR-USERNAME` in the commands below.

```powershell
git init
git add .
git commit -m "Add MiniShop trial app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/minishop-review-trial.git
git push -u origin main
git checkout -b trial/semantic-bugs
```

To make the PR show changed files, `main` must be a clean baseline and the trial branch must introduce the bugs. Easiest approach:
- Before pushing the first commit, correct the five intentional bugs and commit that as `main`.
- Then create `trial/semantic-bugs`, restore the buggy versions of `src/cart.py`, `src/inventory.py`, `src/auth.py`, `src/shipping.py`, and `src/tax.py` from this ZIP, and commit them.
- Push the branch with `git push -u origin trial/semantic-bugs`.
- On GitHub, click **Compare & pull request** and create the PR into `main`.

## Expected bugs (evaluator only; do not paste this list into the PR description)
1. `src/cart.py`: subtracts percentage as a currency amount.
2. `src/inventory.py`: restock overwrites instead of adding.
3. `src/auth.py`: accepts password prefix instead of exact match.
4. `src/shipping.py`: express mode halves the fee.
5. `src/tax.py`: returns total including tax rather than tax only.

`src/orders.py` is intended to be correct. The tests for buggy behavior are expected to fail until the defects are fixed. Use this repository only for testing.
