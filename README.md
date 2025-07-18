# Aviation Model

This is a simple model for estimating the global fleet size for aircraft.

## Developer Guide

The first few sections of this guide outline how to access various parts of the project, such as the main software package, the analysis Python scripts and the documentation.

If you are interested in contributing to this repository, you may find the section titled [Contributing to the Project](#contributing-to-the-project) useful. Although it is not strictly necessary to use the same linting and formatting packages as used by the current contributors, it will minimise failures of the checks done when merging with the main.

### Installing Dependencies in Virtual Environments

This project uses uv to manage dependencies and virtual environments. [View the official UV documentation](https://docs.astral.sh/uv/).

Run the following command on the terminal to create the necessary environment:

```
uv sync
```

### Model and Analysis

This repository contains a package called "aviation" containing relevant functions for analysis. The functions are located in the src/aviation folder, which can be accessed [here.](src/aviation.py)

The [analysis](analysis/) folder contains the various models currently available.

There are:

- passengers_per_day.py
- required_global_fleet.py

Each model can be run from the terminal using the following command, where the name of the file is replaced accordingly:

```
uv run python analysis/file_name.py
```

The output should be the relevant variable name and its value with 2 decimal places.

### Accessing the Documentation

The documentation explaining the model and implementation is written using the mkdocs package. This can be accessed using the terminal through uv and typing:

```
uv run mkdocs serve
```

and will be hosted locally.

The documentation is separated into two sections:

- 'index.md' is the home page.
- 'aviation.md' is the documentation of the model, including constants and equations.

### Contributing to The Project

This repository uses various pre-commit hooks to maintain code style and avoid common errors. [View pre-commit documentation here.](https://pre-commit.com/)

The [.pre-commit-config.yaml](.pre-commit-config.yaml) file contains all of the hooks included in this project. These include various common checks as well as Ruff and UV.

References are managed by Zotero.
