"""Setup for {{ cookiecutter.project_name }}."""
from pathlib import Path
import re

from setuptools import find_packages, setup

TOP_DIR = Path(__file__).resolve().parent
PACKAGE_NAME = "{{ cookiecutter.package_name }}" 

with open(
    TOP_DIR / PACKAGE_NAME.replace("-", "_") / "__init__.py", "r", encoding="utf8"
) as handle:
    VERSION = AUTHOR = AUTHOR_EMAIL = None
    for line in handle.readlines():
        VERSION_match = re.match(r'^__version__ = (\'|")(?P<version>.+)(\'|")', line)
        AUTHOR_match = re.match(r'^__author__ = (\'|")(?P<author>.+)(\'|")', line)
        AUTHOR_EMAIL_match = re.match(
            r'^__author_email__ = (\'|")(?P<email>.+)(\'|")', line
        )

        if VERSION_match is not None:
            VERSION = VERSION_match
        if AUTHOR_match is not None:
            AUTHOR = AUTHOR_match
        if AUTHOR_EMAIL_match is not None:
            AUTHOR_EMAIL = AUTHOR_EMAIL_match

    for info, value in {
        "version": VERSION,
        "author": AUTHOR,
        "author email": AUTHOR_EMAIL,
    }.items():
        if value is None:
            raise RuntimeError(
                f"Could not determine {info} from "
                f"{TOP_DIR / PACKAGE_NAME.replace('-', '_') / '__init__.py'} !"
            )
    VERSION = VERSION.group("version")  # type: ignore[union-attr]
    AUTHOR = AUTHOR.group("author")  # type: ignore[union-attr]
    AUTHOR_EMAIL = AUTHOR_EMAIL.group("email")  # type: ignore[union-attr]

BASE = [
    f"{_.strip()}"
    for _ in (TOP_DIR / "requirements.txt").read_text(encoding="utf8").splitlines()
    if not _.startswith("#") and "git+" not in _
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url="{{ cookiecutter.git_url }}",
    description="OTE-API Plugin.",
    long_description=(TOP_DIR / "README.md").read_text(encoding="utf8"),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=BASE,
)
