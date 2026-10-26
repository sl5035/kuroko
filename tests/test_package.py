from importlib.metadata import version

import kuroko


def test_package_imports_with_its_metadata() -> None:
    assert kuroko.__doc__
    assert version("kuroko") == "0.1.0"
