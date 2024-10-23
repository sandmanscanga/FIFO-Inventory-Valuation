# FIFO Inventory Valuation (fifo) [0.0.0]

A package for calculating inventory valuation, based on FIFO (first
in first out). The package is designed to be used in a warehouse
management system, where the inventory is stored in a list of
dictionaries.

## Dependencies

- [Python](https://www.python.org/) (>=3.12)
- [Poetry](https://python-poetry.org/)
- [Ruff](https://pypi.org/project/ruff/)
- [Pylint](https://pylint.pycqa.org/en/latest/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Pydocstyle](https://www.pydocstyle.org/en/stable/)
- [Bandit](https://bandit.readthedocs.io/en/latest/)
- [Mypy](https://mypy.readthedocs.io/en/stable/)
- [Isort](https://pycqa.github.io/isort/)
- [Black](https://black.readthedocs.io/en/stable/)
- [Pytest](https://docs.pytest.org/en/latest/)
- [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
- [Sphinx](https://www.sphinx-doc.org/en/master/)
- [Sphinx Read the Docs Theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)
- [Semantic Versioning](https://semver.org/)
- [Git](https://git-scm.com/)
- [Changelog](https://keepachangelog.com/en/1.0.0/)
- [License](https://choosealicense.com/)
- [Contributing](https://www.contributor-covenant.org/)
- [Issues](https://guides.github.com/features/issues/)
- [Acknowledgments](https://en.wikipedia.org/wiki/Acknowledgment)

## Pre-Requisites

Installing the package is simple. Before installing the package,
make sure you have all the dependencies installed on your system.

> **Python**

Install the latest version of Python from the
[official website](https://www.python.org/). Ensure that you
have the correct version of Python installed on your system
and that the Python executable is available in the system's PATH.

> **Poetry**

Install the package using [Poetry](https://python-poetry.org/). If
you don't have Poetry installed, you can install it using the
following command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

Alternatively, you can install Poetry using `pip`:

```bash
python -m venv venv
./venv/bin/python -m pip install -U pip
./venv/bin/python -m pip install poetry
```

Also note that using a virtual environment is strongly recommended
to avoid conflicts with other Python packages.

---

## Installation

After installing Poetry, you can install the package using the
following command:

```bash
poetry install
```

Updating the package dependencies is also recommended to ensure
that you have the latest version of the package dependencies. You
can update the package dependencies using the following command:

```bash
poetry update
```

Once the package is installed, you can run the package using the
following command:

```bash
poetry run python -m fifo
```

---

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)

## Issues

If you find any issues, please create an issue on the
[GitHub](https://github.com/sandmanscanga/FIFO-Inventory-Valuation/issues)
page.

## License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE.md) file for details.

## Acknowledgments

- [Python Packaging User Guide](https://packaging.python.org/)
- [Python Testing with pytest](https://docs.pytest.org/en/latest/)
- [Python Code Quality: Tools & Best Practices](https://realpython.com/python-code-quality/)
- [Python Continuous Integration and Delivery with GitHub](https://realpython.com/python-continuous-integration/)
- [Python Project Setup Best Practices](https://sourcery.ai/blog/python-best-practices/)
- [Python Project Structure Best Practices](https://sourcery.ai/blog/python-best-practices/)
- [Python Logging Best Practices](https://sourcery.ai/blog/python-best-practices/)
