# Create venv
python3 -m venv venv
source venv/bin/activate

# Install repo
pip install wheel
pip install -e .
pip install -r requirements-dev.txt

git init
pre-commit install