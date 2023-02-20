
## Getting started with Python in VS Code

- Reference link: https://code.visualstudio.com/docs/python/python-tutorial

## Virtual environment

- Virtual environment creation for macOS

```
python3 -m venv .venv
source .venv/bin/activate
```

- Type `deactivate` in the terminal window to deactivate the virtual environment

## convert jupyter notebook to python file 

- In VSCode command palette (shift+command+P), select `Jupyter: Convert to Python Script`

## Open VSCode for a folder

- First change the working directory to that folder in terminal, then type `code .` in terminal

- In case the above does not work, see the solution here: https://stackoverflow.com/questions/29955500/code-is-not-working-in-on-the-command-line-for-visual-studio-code-on-os-x-ma


## `Python: Select Interpretor`

- This one is used for `.py` file to select the python environment 
- For `ipynb`, use the button in the right upper corner to change the kernel
