# GOP Report Generator

A Python utility designed to efficiently extract and report data from the GOP service.

## Getting Started

These instructions will guide you through setting up the GOP Report Generator on your system.

### Pre-requisites

Before you begin, ensure you have the following installed:
- **Python 3.12** or newer
- **pip** (Python Package Installer)
- **pipx** (optional, for isolated global python application installation. Poetry is usually installed with pipx)
- **Poetry** for dependency management and packaging.

**Poetry Installation:**
Follow the Poetry installation instructions [here](https://python-poetry.org/docs/#installation).

### Project Setup

1. **Clone the repository:** Obtain a local copy of the code.
2. **Environment Variables:** Configure your `.env` file based on the `.env.example` provided in the root directory. You must specify `GOP_USER` and `GOP_PASSWORD` for authentication purposes.
3. **Install Dependencies:** Navigate to the project's root directory and run:
   ```
   poetry install
   ```
   This command reads the `pyproject.toml` file and installs the necessary dependencies.


### File Structure Overview

The structure of the project includes various Python scripts, a README, and configuration files. Key components include:

- `extract.py` and `extract_gop.py`: Scripts for data extraction from the GOP website.
- `query.py`: Composes queries for fetching specific information.
- `tests.py`: Obtains IDs and descriptions for processing.
- `to_excel.py`: Transforms extracted data into structured Excel reports.

### Running the Utility

Ensure your environment variables are set properly before execution. You can run the utility through the main script:

```bash
poetry run python main.py
```

This command initiates the process of data extraction, filtering, and report generation.

## Structure and Code Details

The utility employs a modular approach, segregating functionalities like data extraction (`extract_gop.py`), query composition (`query.py`), and report generation (`to_excel.py`). To ensure efficient data handling, `extract_gop.py` utilizes concurrent requests to process multiple items simultaneously. Each script is designed with clear responsibilities, making the codebase easy to navigate and extend.

