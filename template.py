import os
from pathlib import Path
import logging

logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s] %(message)s",
)

logging.info("\n**********************PART**********************\n")
# logging.info("\n")

while True:
    project_name = input("Enter your project name, please!: ")
    logging.info(f"{project_name} added.")
    if project_name != "":
        break

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "setup.py",
    "setup.cfg",
    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    "tox.ini",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Folder created for {filedir} @path {filepath}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w", encoding="UTF-8") as f:
            pass
        logging.info(f"File created for {filename} @path {filepath}")
    else:
        logging.info(f"Filename {filename} already exists.")
