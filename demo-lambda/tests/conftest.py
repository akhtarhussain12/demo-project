import sys
from pathlib import Path


def pytest_configure(config):
    sys.path.append(str(Path(__file__).absolute().parents[1] / "src/"))


def pytest_unconfigure(config):
    sys.path.remove(str(Path(__file__).absolute().parents[1] / "src/"))