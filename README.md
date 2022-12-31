## Setup of Base Skeleton for Python Projects:

### Steps to follow:
* Create Template.py for generating below list of files:
    * .github/workflows/.gitkeep
    * src/<project_name>/__init__.py
    * tests/__init__.py
    * tests/unit/__init__.py
    * tests/integration/__init__.py
    * init_setup.sh
    * setup.py
    * setup.cfg
    * requirements.txt
    * requirements_dev.txt
    * pyproject.toml
    * tox.ini

* Run -> bash init_setup.sh
* Run -> pytest -v
* Run -> tox

* Under requirements.txt:
    * pandas, numpy, matplotlib, sklearn
    * ipywidgets
    * notebook
    * ensure
    * py-youtube
    * pytest, black, flake8, tox, mypy, -e .