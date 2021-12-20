# nbconvert-flowkey

Some failed attempts at combining the functionality of the [toc2 nbconvert extension](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/toc2/README.html)
with my own custom template.

**Old attempts / notes (in case I ever come back to this later):**

TOC2 w/ nbconvert < 6 out of the box (works but not with my custom template):

```dockerfile
FROM python:3.9-slim

WORKDIR /usr/src/myapp

COPY requirements.txt ./

RUN pip install --trusted-host pypi.python.org -r requirements.txt && \
    pip install nbconvert==5.6.1 && \
    pip install ipykernel==5.5.5 && \
    pip install jupyter_client==6.1.12 && \
    pip install jupyter_contrib_nbextensions==0.5.1 && \
    jupyter contrib nbextension install --user && \
    jupyter nbextension enable toc2/main

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN pip install git+https://github.com/pawlodkowski/nbconvert-flowkey.git

CMD jupyter nbconvert analysis.ipynb --to notebook --output 'ex.ipynb' --execute && \
    jupyter nbconvert ex.ipynb --to html_toc --no-input --output 'report.html'
```

initial attempt at building my own custom exporter (the code found in this branch):

```dockerfile
FROM python:3.9-slim

WORKDIR /usr/src/myapp

COPY requirements.txt ./

RUN pip install --trusted-host pypi.python.org -r requirements.txt && \
    pip install nbconvert==6.1.0 && \
    pip install ipykernel==5.5.5 && \
    pip install jupyter-packaging==0.11.1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN pip install git+https://github.com/pawlodkowski/nbconvert-flowkey.git

CMD jupyter nbconvert analysis.ipynb --to notebook --output 'ex.ipynb' --execute && \
    jupyter nbconvert ex.ipynb --to html_toc --no-input --output 'report.html'
```