# ___PROJECT_NAME

## Install

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install project as editable
pip install -e . # Also installs requirements

# Install dev requirements
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```