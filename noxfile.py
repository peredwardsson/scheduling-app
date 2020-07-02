"""Configs Nox for running different sessions."""
import tempfile
from typing import Any

import nox
from nox.sessions import Session

locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "tests", "mypy"
package = "scheduling_app"


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """Installs packages with constraints."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=["3.8"])
def tests(session: Session) -> None:
    """Runs tests."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock"
    )
    session.run("pytest", *args)


@nox.session(python=["3.8"])
def lint(session: Session) -> None:
    """Runs linting with Flake8."""
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8"])
def black(session: Session) -> None:
    """Runs linting with Black."""
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python="3.8")
def safety(session: Session) -> None:
    """Runs security check with Safety."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python="3.8")
def mypy(session: Session) -> None:
    """Runs mypy."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)


@nox.session(python="3.8")
def typeguard(session: Session) -> None:
    """Runs typeguard."""
    args = session.posargs or ["-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    # install_with_constraints(session, "pytest", "pytest-mock", "typeguard")
    install_with_constraints(session, "pytest", "typeguard")
    session.run("pytest", f"--typeguard-packages={package}", *args)


@nox.session(python="3.8")
def pytype(session: Session) -> None:
    """Run the static type checker."""
    args = session.posargs or ["--disable=import-error", *locations]
    install_with_constraints(session, "pytype")
    session.run("pytype", *args)
