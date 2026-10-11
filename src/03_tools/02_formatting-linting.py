# RUFF -- Linter and Formatter
"""
🟡 1. Installing Ruff

    ⭕ Ruff checks your code for mistakes (linting) and makes it neat (formatting).
       It replaces flake8, isort, black and more.

        1. uv add --dev ruff                        [Add Ruff to the project with uv]
        2. python -m pip install ruff               [Install Ruff with pip]
        3. uv tool install ruff                     [Install Ruff once, use in all projects]
        4. uvx ruff check .                         [Run Ruff without installing it]
        5. ruff --version                           [Check the installed version]

🟡 2. Linting (Finding Problems)

    * Linting finds mistakes like unused imports, unused variables, and bad habits.

    ⭕ Important Commands for Linting:
        1. ruff check .                             [Check all files in the current folder]
        2. ruff check <file.py>                     [Check one file only]
        3. ruff check --fix .                       [Fix the problems that can be fixed by itself]
        4. ruff check --diff .                      [Show what would change, without changing files]
        5. ruff check --watch .                     [Check again every time a file changes]
        6. ruff check --statistics .                [Show how many times each problem was found]
        7. ruff check --select I .                  [Check only some rules (here: import order)]
        8. ruff check --unsafe-fixes --fix .        [Also apply risky fixes. Check the result after]

🟡 3. Formatting (Making Code Neat)

    * Formatting fixes spaces, quotes, and line breaks. Its output is almost the same as Black.

    ⭕ Important Commands for Formatting:
        1. ruff format .                            [Format all files]
        2. ruff format <file.py>                    [Format one file only]
        3. ruff format --check .                    [Only check, do not change files. Good for CI]
        4. ruff format --diff .                     [Show what would change]

    ⭕ Best order to run:
        ruff check --fix . && ruff format .         [Fix first, then format]

🟡 4. Settings in pyproject.toml

    * Keep all settings in one file: pyproject.toml

        [tool.ruff]
        line-length = 88                            [Max characters in one line]
        target-version = "py312"                    [Lowest Python version your project supports]

        [tool.ruff.lint]
        select = ["E", "W", "F", "I", "UP", "B", "SIM", "RUF"]
        ignore = ["E501"]                           [Skip line-length rule, the formatter handles it]

        [tool.ruff.format]
        quote-style = "double"                      [Use "double" quotes]

    ⭕ What the rule letters mean:
        1. E, W    [Basic style errors and warnings]
        2. F       [Real mistakes, like unused imports]
        3. I       [Import order, same as isort]
        4. UP      [Update old code to new Python style]
        5. B       [Likely bugs]
        6. SIM     [Make code simpler]
        7. RUF     [Ruff's own rules]

🟡 5. Useful Extra Commands

    1. ruff rule <code>                             [Explain one rule, example: ruff rule F401]
    2. ruff linter                                  [List all rule groups]
    3. ruff config                                  [Show all settings you can use]
    4. ruff clean                                   [Delete Ruff's cache]
    5. # noqa: F401                                 [Comment to skip a rule on one line]
    6. ruff check --add-noqa .                      [Add noqa comments to all current problems]

🟡 6. Run it Automatically

    ⭕ Editor (VS Code):
        1. Install the "Ruff" extension
        2. Set it as the default formatter for Python
        3. Turn off old flake8, pylint and Black settings, so they do not clash

    ⭕ Pre-commit (runs before every commit):
        repos:
          - repo: https://github.com/astral-sh/ruff-pre-commit
            rev: <version>
            hooks:
              - id: ruff
                args: [--fix]
              - id: ruff-format

    ⭕ CI (GitHub Actions or any other):
        1. ruff check .
        2. ruff format --check .

🟡 7. Type Checking (Different Job)

    * Ruff does NOT check types. Use another tool for that.

        1. mypy .                                   [Popular and old type checker]
        2. pyright                                  [Fast type checker, used in many editors]
        3. uvx ty check                             [New type checker from the Ruff team]

🟡 8. Important Concepts

    1. Linting finds problems. Formatting only changes how code looks.
    2. Run "ruff check --fix" first, then "ruff format".
    3. Keep all settings in pyproject.toml, so the whole team uses the same rules.
    4. Start with a small list of rules, then add more later.
    5. Ruff is very fast, so you can run it on every save.
    6. In an old project, do not format everything at once. Do it in one separate commit.
    7. Ruff does not check types. Use mypy, pyright or ty with it.
"""
