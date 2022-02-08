from pathlib import Path

PATH_CONFIG = Path(__file__).parent
PATH_SRC = PATH_CONFIG.parent
PATH_PROJECT_ROOT = PATH_SRC.parent
PATH_TESTS = PATH_PROJECT_ROOT / "tests"


def test_path_definitions():
    """
    tests that the path definitions are correct
    """
    assert str(PATH_CONFIG).endswith(str(PATH_SRC / "config")), \
        "config path not correct, check config/definitions.py"
    assert str(PATH_TESTS).endswith(str(PATH_PROJECT_ROOT / "tests")), \
        "tests path not correct, check config/definitions.py"

    print("\nConfigured paths:\n")
    print(PATH_CONFIG)
    print(PATH_SRC)
    print(PATH_PROJECT_ROOT)
    print(PATH_TESTS)
    print("\nPaths configured correctly!")


if __name__ == "__main__":
    test_path_definitions()
