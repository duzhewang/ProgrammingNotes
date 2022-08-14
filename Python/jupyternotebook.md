# Jupyter notebook notes
Last updated date: 8/11/2022


### Install Jupyter notebook

```
python3 -m pip install jupyter notebook
```

### Open Jupyter notebook in terminal 
  - step 1: change the working directory to the one which will be used 
  ```
  cd workingdirectory
  ```

  - step 2: launch jupyter notebook
  ```
  jupyter notebook
  ```
### nbviewer
Sometimes, when opening jupyter notebook on Github, it shows something went wrong. That is, the notebook rendering on Github is having some hiccups. Instead, we can copy and paster the notebook link to https://nbviewer.jupyter.org/.   


### Add date, author name in jupyter notebook

```
%load_ext watermark
%watermark -d -u -a "Duzhe Wang" -v -p numpy,sklearn,pandas
```
**Note: no white space between package names.** 

- See more details from this link: https://github.com/rasbt/watermark/blob/master/docs/watermark.ipynb


### Shortcuts

- From code cell to markdown: "esc + m ". From mardown to code cell: " esc + y ". See more shortcuts from ```Help->Keyboard Shortcuts``` in jupyter notebook
- ``shift+return: run cell, select below``
- ``control+return: run selected cell``
- delete the cell: ``dd``
- change the cell to markdown by hitting ``m`` key
- change the cell to code by hitting ``y`` key
- ``control``+``c`` to shutdown the jupyter notebook server

### Convert a jupyter notebook to pdf: in shell, type
  ```
  jupyter nbconvert <notebook name> --to pdf
  ```

### Insert a picture in the notebook:

```
#Import library
from IPython.display import Image
# Load image from local storage
Image(filename = "img.png", width = 600, height = 300)


```


## Create html file for jupyter notebook
- In jupyter notebook, use ``%load_ext pretty_jupyter``
- After creating the jupyter notebook, in terminal, use ``jupyter nbconvert --to html --template pj PATH/TO/YOUR/JUPYTER/NOTEBOOK``
- See demo from https://github.com/JanPalasek/pretty-jupyter-examples/tree/main/demo
- How to override the default title?
  - In the `Edit` tab in the notebook, click `Edit Notebook Metadata`. Then type `"title": "New title"`.
  
