"""Data model package for EnzymeDCAT-AP."""

from pathlib import Path
from .enzymedcat_ap import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "enzymedcat_ap.yaml"
