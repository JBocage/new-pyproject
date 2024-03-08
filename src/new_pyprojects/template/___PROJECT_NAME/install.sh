python3 -m venv venv
source venv/bin/activate

pip install wheel
pip install -e .
pip install -r requirements-dev.txt

black . -q
isort .

git init # F:GIT
git add .  # F:FIRSTCOMMIT
git commit -m "___FIRST_COMMIT_MSG"  # F:FIRSTCOMMIT

pre-commit install # F:GIT

___CLI_NAME doc update # F:CLIGROUP&DOCS
