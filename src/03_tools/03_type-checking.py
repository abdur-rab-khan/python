"""
🟡 1. Important Commands

    ⭕ mypy:
        1. uv add --dev mypy
        2. mypy .                         [Check all files]
        3. mypy --strict .                [Very strict mode]

    ⭕ pyright:
        1. uv add --dev pyright
        2. pyright                        [Check the project]

    ⭕ Pyrefly:
        1. uv add --dev pyrefly
        2. pyrefly init                   [Create config, copies old mypy or pyright settings]
        3. pyrefly check                  [Check the project]
        4. pyrefly infer                  [Write type hints into files automatically]

    ⭕ ty:
        1. uvx ty check                   [Run without installing]
        2. uv add --dev ty                [Install in the project]
        3. ty check                       [Check the project]

🟡 2. Type Hints You Should Know

    1. def greet(name: str) -> str:       [Hints for input and output]
    2. list[int], dict[str, int]          [Use built-in types, not typing.List]
    3. int | None                         [Number or None, use this, not Optional]
    4. Any                                [Means "skip checking", use it as little as possible]
    5. # type: ignore                     [Skip one line]

🟡 3. Run it Automatically

    1. Editor     [Use only one checker in the editor, to avoid double errors]
    2. CI         [Add these commands:]
                    ruff check .
                    ruff format --check .
                    mypy .                [Or: pyrefly check / pyright / ty check]
"""
