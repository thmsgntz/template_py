import nox
import os

# NOX USAGE: https://nox.thea.codes/en/stable/usage.html

ROOT_DIR = os.path.dirname(__file__)
CONFIG_TOOLS_DIR = os.path.join(ROOT_DIR, ".config_tools")
CONFIG_TOML = os.path.join(CONFIG_TOOLS_DIR, "pyproject.toml")
FLAKE_TOML = os.path.join(CONFIG_TOOLS_DIR, "flake8.toml")

SRC_DIR = os.path.join(ROOT_DIR, "src")
FILE = os.path.join(SRC_DIR, "classes.py")
TARGET = SRC_DIR

# Stopping if any session fails
nox.options.stop_on_first_error = True

# Re-using virtualenvs
nox.options.reuse_existing_virtualenvs = True

# provide a set of sessions that are run by default:
# nox.options.sessions = ["isort", "black_diff_only", "flake"]
nox.options.sessions = ["isort", "black", "flake"]


@nox.session(python="3.8")
def isort(session):
    # https://pycqa.github.io/isort/docs/upgrade_guides/5.0.0.html
    session.install("isort")
    session.run("isort", "--settings-path", CONFIG_TOML, TARGET)


@nox.session(python="3.8")
def mypy(session):
    session.install("mypy")
    session.run("mypy", "--config-file", CONFIG_TOML, TARGET)


@nox.session(python="3.8")
def black_diff_only(session):
    session.install("black")
    session.run("black", "--config", CONFIG_TOML, "--diff", TARGET)


@nox.session(python="3.8")
def black(session):
    session.install("black")
    session.run("black", "--config", CONFIG_TOML, TARGET)


@nox.session(python="3.8")
def flake(session):
    session.install("flake8")
    session.run("flake8", "--config", FLAKE_TOML, TARGET)
