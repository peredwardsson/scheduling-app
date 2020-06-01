# tests/test_month.py

import click.testing
import pytest

from scheduling_app import get_schedule


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_month_switcher_with_int(runner):
    result = runner.invoke(get_schedule.main, ["--month", "5"])
    assert "May" in result.output
    assert result.exit_code == 0


def test_month_switcher_without_int(runner):
    result = runner.invoke(get_schedule.main)
    assert result.exit_code == 0
