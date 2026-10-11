# UV -- Package Manager
"""
🟡 1. Installing and Manager Python

    ⭕ It's used to install and manage python version for current project
        1. uv python list                           [list down available python versions]
        2. uv python install <version>              [install specific python version]
        3. uv python upgrade                        [use to install or update that version to an available patch release.]
        4. uv python pin <version>                  [pin specific python version for current project]
        5. uv python dir                            [give the directory where all the python version is installed]
        6. uv python uninstall <version             [uninstall the specific version of python]

🟡 2. Projects in UV
    * It's similar to npm init in JS ecosystem, "uv init" initiate project along with all required files for managing dependencies

    ⭕ Important Commands for Project:
        1. uv init -p <python-version> --no-package --name <name>
        2. uv add [--dev] <package-name>                        [Add a particular package]
        3. uv remove <package-name>                             [Removes a particular package]
        4. uv sync                                              [Install everything required like npm install]
        5. uv tree                                              [Display the projects dependency]
        6. uv venv -p <python-version>                          [Creates a virtual environment]
        7. uv lock                                              [Creates a lock file]

🟡 3. Tool in UV
    * Similar to npx or bunx, so run library without installing it, in uv we can do this use "uvx

        ⭕ Example:
            1. uvx ruff

🟡 4. Common utility commands
    1. uv run                                               [use to run script, module, installed cli tools]
    2. uv tool [install, list, upgrade, uninstall]          [unlike uvx it install and we can use across all the projects]
"""

# PIP -- Package Manager
"""
🟡 1. Installing and Managing Packages

    ⭕ Used to install, update, and remove Python packages in the current environment.

        1. python -m pip install <package-name>       [Install a package]
        2. python -m pip install --upgrade <package>  [Upgrade a package]
        3. python -m pip uninstall <package-name>    [Remove a package]
        4. python -m pip list                        [List installed packages]
        5. python -m pip show <package-name>         [Show package details]
        6. python -m pip check                       [Check for dependency conflicts]

🟡 2. Managing Project Dependencies

    ⭕ Used to install packages listed in requirements.txt.

        1. python -m pip install -r requirements.txt
           [Install all packages listed in the file]

        2. python -m pip freeze > requirements.txt
           [Save installed packages and their versions]

        3. python -m pip freeze
           [Display installed packages with exact versions]

🟡 3. Virtual Environments

    ⭕ Use a virtual environment to isolate project dependencies.

        1. python -m venv .venv
           [Create a virtual environment]

        2. .venv\Scripts\Activate.ps1
           [Activate in Windows PowerShell]

        3. deactivate
           [Deactivate the virtual environment]

🟡 4. Important Concepts

    1. pip installs packages; it does not manage Python versions.
    2. Use python -m pip to ensure pip runs with the intended Python interpreter.
    3. requirements.txt commonly lists project dependencies.
    4. pip freeze lists installed packages; it does not generate a proper lockfile.
    5. Prefer a virtual environment instead of installing project packages globally.
"""
