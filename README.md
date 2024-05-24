# Project Setup Tool

This tool helps you set up a new web development project with a predefined structure and initializes a Git repository.

## Usage

To create a new project, run the following command:

```bash
python create_project.py <project_name> [options]
```

### Options

`-t, --template`: Choose a template (1 for Basic, 2 for Intermediate, 3 for Advanced)

#### Example

```bash
python create_project.py my_project -t 2
```

## Requirements

- Python 3.x
- `rich` library for enhanced CLI output

## Installation

```bash
pip install rich
```

```perl
### Step 3: Compile the Script

Use `PyInstaller` to compile the script into an executable.

```

```bash
pyinstaller --onefile create_project.py
```
