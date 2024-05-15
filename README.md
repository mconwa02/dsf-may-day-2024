# Data Science Festival May Day 2024

MLOPS in Financial Services

![speaker_flyer.jpg](docs%2Fspeaker_flyer.jpg)

https://pypi.org/project/statsmodels/

https://pypi.org/project/scikit-learn/

https://pypi.org/project/sktime/

https://pypi.org/project/darts/

## Setting up the Development Environment

To ensure a clean and isolated development environment, use a 
virtual environment created with `venv` and manage dependencies using 
`pyproject.toml`. 

Additionally, set up pre-commit hooks for code quality checks, 
including linting with Ruff.

### Creating a Virtual Environment

Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

### Installing Dependencies

Once inside the virtual environment, install project dependencies from the `pyproject.toml` file:
```bash
pip install -e .
```

Poetry and pip-tools are excellent package managers. As pip won't necessarily
handle all dependencies and constraints as effectively as package managers

### Setting up Pre-commit Hooks and Linting

Use `pre-commit` to enforce code quality standards. 
Additionally, use `ruff` for linting. 
Both packages are in the `pyproject.toml` file for install.

https://pre-commit.com

Navigate to your project directory and set up pre-commit hooks:
```bash
pre-commit install
```

A `.pre-commit-config.yaml` file is in project directory with config for 
ruff linting. Whenever you make a commit, `pre-commit` will run linting 
with Ruff and enforce code quality standards automatically.

https://github.com/astral-sh/ruff-pre-commit

