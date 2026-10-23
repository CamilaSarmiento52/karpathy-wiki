"""Make scripts/ importable, and keep tests off the network and the real raw/."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import rawstore  # noqa: E402


@pytest.fixture
def store(tmp_path, monkeypatch):
    """An empty repo root for rawstore, with no pauses between requests."""
    monkeypatch.setattr(rawstore, "ROOT", tmp_path)
    monkeypatch.setattr(rawstore, "PAUSE", 0)
    (tmp_path / "raw").mkdir()
    return tmp_path
