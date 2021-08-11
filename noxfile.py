import nox
import os

# NOX USAGE: https://nox.thea.codes/en/stable/usage.html

WORKING_DIR = os.path.dirname(__file__)
CONFIG_TOML = os.path.join(WORKING_DIR, "pyproject.toml")
FILE = os.path.join(WORKING_DIR, "src", "debug_utils.py")

# Stopping if any session fails
nox.options.stop_on_first_error = True

# Re-using virtualenvs
nox.options.reuse_existing_virtualenvs = True


@nox.session(python="3.8")
def isort(session):
    session.install("isort")
    session.run("isort", "--settings-path", CONFIG_TOML, "-d", "-v", FILE)


@nox.session(python="3.8")
def mypy(session):
    session.install("mypy")
    session.run("mypy", "--config-file", CONFIG_TOML, FILE)


@nox.session(python="3.8")
def black(session):
    session.install("black")
    session.run("black", "--config", CONFIG_TOML, "--diff", FILE)


@nox.session(python="3.8")
def flake(session):
    session.install("flake8")
    session.run("flake8", "--config", CONFIG_TOML, FILE)
