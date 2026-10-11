# TYPE CHECKERS -- Find Type Mistakes Before Running Code
"""
🟡 1. What is Type Checking

    ⭕ A type checker reads your type hints, like  def add(a: int, b: int) -> int
       and tells you about mistakes before you run the code.
       Python does not check these hints by itself.

        1. Ruff            [finds style problems]
        2. Type checker    [finds wrong types]
        3. Use both together

🟡 2. Which Tool to Choose in 2026

    ⭕ The main tools:
        1. mypy        [Oldest and most trusted]
        2. pyright     [From Microsoft, powers Pylance in VS Code]
        3. Pyrefly     [From Meta, Rust-based, stable and fast]
        4. ty          [From Astral, very fast, but still in beta]

    ⭕ Simple advice:
        1. New project          -> Pyrefly
        2. Old project on mypy  -> Stay on mypy, or move to Pyrefly
        3. Important production -> mypy or pyright (safest)
        4. Want to try newest   -> ty

🟡 3. Important Commands

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

🟡 4. Type Hints You Should Know

    1. def greet(name: str) -> str:       [Hints for input and output]
    2. list[int], dict[str, int]          [Use built-in types, not typing.List]
    3. int | None                         [Number or None, use this, not Optional]
    4. Any                                [Means "skip checking", use it as little as possible]
    5. # type: ignore                     [Skip one line]

🟡 5. Run it Automatically

    1. Editor     [Use only one checker in the editor, to avoid double errors]
    2. CI         [Add these commands:]
                    ruff check .
                    ruff format --check .
                    mypy .                [Or: pyrefly check / pyright / ty check]

🟡 6. Important Concepts

    1. Ruff is not a type checker. Use both together.
    2. Pick ONE type checker per project, different tools show different errors.
    3. Rust tools (Pyrefly, ty) are 10 to 100 times faster than mypy and pyright.
    4. ty is still beta, so good to try but not the safest choice yet.
    5. In an old project, start with basic mode, then go strict slowly.
    6. Add hints to function inputs and outputs first, it gives the biggest benefit.
"""
