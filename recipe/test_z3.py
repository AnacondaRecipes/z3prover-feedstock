import os
import importlib.metadata
import z3

PKG_NAME = os.environ["PKG_NAME"]
PKG_VERSION = os.environ["PKG_VERSION"]  # "4.15.4"

# PyPI wheels append ".0" — derive it; conda metadata may report either form
PY_VERSION = f"{PKG_VERSION}.0"   # "4.15.4.0"
LIB_VERSION = PKG_VERSION         # "4.15.4" — libz3 uses 3-component version


def test_py_module_version():
    """Verify python module versions agree.

    PyPI releases have an extra trailing digit, e.g. `4.15.4.0`. Only `.0` has
    been observed since 2017.

    see https://pypi.org/project/z3-solver/#history
    """
    module_version = importlib.metadata.version(PKG_NAME)
    print(f"{PKG_NAME} module version:", module_version)
    # Normalize trailing ".0" — both "4.15.4" and "4.15.4.0" are acceptable
    normalized = module_version if not module_version.endswith(".0") else module_version[:-2]
    assert normalized == PKG_VERSION


def test_libz3_version():
    """Verify the python version reports the expected `libz3` version.

    The should match the tag pattern without `z3-` or the python micro version,
    e.g. `4.15.4`.
    """
    libz3_version = z3.get_version_string()
    print("libz3 version:", libz3_version)
    assert libz3_version == LIB_VERSION


def test_py_example():
    """Verify simple smoke test, adapted from upstream example.

    see https://github.com/Z3Prover/z3/blob/z3-4.15.4/examples/python/example.py
    """
    s = z3.Solver()
    x, y = z3.Real("x"), z3.Real("y")
    s.add(x + y > 5, x > 1, y > 1)
    print(s.check())
    print(s.model())