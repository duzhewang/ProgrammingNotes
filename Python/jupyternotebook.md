- install Jupyter notebook:
```
python3 -m pip install jupyter notebook
```
- open Jupyter notebook:
  - step 1: change the working directory
  ```
  cd workingdirectory
  ```

  - step 2: launch jupyter notebook
  ```
  jupyter notebook
  ```
- Sometimes, when opening jupyter notebook on Github, it shows something went wrong. That is, the notebook rendering on Github is having some hiccups. Instead, we can cope and paster the notebook link to https://nbviewer.jupyter.org/.   


- Add date, author name in jupyter notebook
```
%load_ext watermark
%watermark -d -u -a "Duzhe Wang" -v -p numpy,sklearn,pandas
```

- From code cell to markdown: "esc + m ". From mardown to code cell: " esc + y ". See more shortcuts from ```Help->Keyboard Shortcuts``` in jupyter notebook

- [A gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#statistics-machine-learning-and-data-science)
