# A supervised multi-class framework for mineral classification of Iberian beads

[![GitHub License](https://img.shields.io/github/license/Daniel-SanchezG/MACLAS)](https://github.com/Daniel-SanchezG/MACLAS/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10155404.svg)](https://doi.org/10.5281/zenodo.10155404)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Daniel-SanchezG/MACLAS/blob/main/Model_development.ipynb)



This repository is a supplement to

["A supervised multiclass framework for mineral classification of Iberian beads"]()


**It contains the following Notebooks:**

---

**1.[Model development](./Model_development.ipynb):** The entire development pipeline of the multiclass classfication model.

**2.[Proof-of-concept](./Proof-of-concept.ipynb):** A real-world use case of the pre-trained model. 

**3.[MACLAS model](./MACLAS.ipynb):** This notebook allows the use of the trained model on new data (on binder).

---

* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Daniel-SanchezG/MACLAS/HEAD) launches an **interactive** Jupyter Lab version in your browser that you can navigate and run.  
* Nbviewer links provide an static HTML version of the notebooks.
* All notebooks and data can also be downloaded directly from this repository. 

---
| Nbviewer |
| ---      |
| [Model_development.ipynb](https://nbviewer.org/github/Daniel-SanchezG/MACLAS/blob/main/Model_development.ipynb) |
| [Proof-of_concept.ipynb](https://nbviewer.org/github/Daniel-SanchezG/MACLAS/blob/main/Proof-of-concept.ipynb) |
| [MACLAS model.ipynb](https://nbviewer.org/github/Daniel-SanchezG/MACLAS/blob/main/MACLAS.ipynb) |

---
To enable reproducibility, we provide a data directory with the training [data](./DATA/maclas_training.xlsx) required to run the workflow. 

---
**Development environment**

Python implementation: CPython
Python version       : 3.8.10
IPython version      : 8.12.3

ipywidgets: 7.7.5
matplotlib: 3.6.0
numpy     : 1.23.5
pandas    : 1.4.4
sklearn   : 1.2.2
pycaret   : 3.0.4
jupyterlab: 4.2.0
seaborn   : 0.12.2
imblearn  : 0.12.3
re        : 2.2.1

Compiler    : GCC 9.4.0
OS          : Linux
Release     : 5.15.0-113-generic
Machine     : x86_64
Processor   : x86_64
CPU cores   : 4
Architecture: 64bit

---
**Authors:** [Daniel Sanchez-Gomez](mailto:daniel-sanchez-gomez@edu.ulisboa.pt), Carlos P. Odriozola, Ana Caterina Sousa, José Angel Garrido-Cordero, Galo Romero-García, José María Martínez-Blanes, Manuel Edo i Benaigues, Ferrán Borrel Tena. 

=======

