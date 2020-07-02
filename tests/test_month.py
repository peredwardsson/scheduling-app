"""Tests month recalling functions."""
import click.testing
from click.testing import CliRunner
import pytest

from scheduling_app import get_schedule


@pytest.fixture
def runner() -> CliRunner:
    """Returns a Click Runner."""
    return click.testing.CliRunner()


def test_month_switcher_with_int(runner: CliRunner) -> None:
    """Tests that the correct month is returned for a specific int."""
    result = runner.invoke(get_schedule.main, ["--month", "5"])
    assert "May" in result.output
    assert result.exit_code == 0


def test_month_switcher_without_int(runner: CliRunner) -> None:
    """Tests that no error is returned when no month is input."""
    result = runner.invoke(get_schedule.main)
    assert result.exit_code == 0
