# MACLAS(Mineral Archaeological Classification System)

## A Supervised Multiclass Model for mineral classification of prehistoric personal adornments in Iberia

[![GitHub License](https://github.com/Daniel-SanchezG/MACLAS/blob/main/LICENSE)]


This repository is a supplement to

["Paper_1"]()


**It contains the following Notebooks:**

---

**1.[Model development](./Model_development.ipynb):** The entire development pipeline of the multiclass classfication model.

**2.[Proof-of-concept](./Prediction_function.ipynb):** This notebook presents a real-world use case of the pre-trained model. 

**3.[MACLAS Model](./MACLAS.ipynb):** This notebook allows the use of the pre-trained models on new data.

---

**Run the following notebooks and explore the development and application of MACLAS.** 


![Binder](https://mybinder.org/badge_logo.svg) buttons launch a
 interactive Jupyter Notebook or Jupyter Lab version in your web browser.  

All notebooks and data can also be downloaded directly from this repository. 

---

|Jupyter Notebook | Jupyter Lab | HTML |
| ---      | --               | ---         | ---  |
|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F0-Workflow.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/0-Workflow.html) |
|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F1-CreateDataset.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F1-CreateDataset.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/1-CreateDataset.html) |
|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F2-CalculateFeatures.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F2-CalculateFeatures.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/2-CalculateFeatures.html) |
|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F3-FitModel.ipynb) |[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F3-FitModel.ipynb)  | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/3-FitModel.html) |
|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F4-Predict.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F4-Predict.ipynb)| [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/4-Predict.html) |

---

To enable reproducibility, we provide a data directory with the trainig data required to run the workflow. The full dataset is available [here](./example1/data/Datasets.md).

---
**Development environment**

Python implementation: CPython
Python version       : 3.8.10
IPython version      : 7.34.0

ipywidgets: 7.7.5
matplotlib: 3.6.3
numpy     : 1.23.5
pandas    : 1.4.4
sklearn   : 1.2.2
pycaret   : 3.0.4
jupyterlab: 3.6.1

Compiler    : GCC 9.4.0
OS          : Linux
Release     : 5.15.0-78-generic
Machine     : x86_64
Processor   : x86_64
CPU cores   : 4
Architecture: 64bit
---

=======

