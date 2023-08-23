# MACLAS(Mineral Archaeological Clasification System)

## A Supervised Multiclass Model for mineral classificaiton of prehistoric personal adornments in Iberia

[![GitHub License](https://img.shields.io/github/license/jupyter-guide/ten-rules-jupyter.svg)](https://github.com/sbl-sdsc/mmtf-spark/blob/master/LICENSE)

This repository is a supplement to

["Paper_1"](https://doi.org/10.1371/journal.pcbi.1007007) 

[![Tweets](https://img.shields.io/badge/dynamic/json.svg?url=https://api.altmetric.com/v1/id/64040119&label=Altmetric&query=$.score&style=social)](https://www.altmetric.com/details/64040119)

**The notebooks in this directory demonstrate the development and application of  a "supervised multiclass model for mineral classification of prehistoric personal adornments in Iberia". You can reproduce the whole process, train different models and test their performance or skip the process and use the ready-made MACLAS on your own data**

**this pipeline contains the following Notebooks:**

---

**1. Model development:** We perform a serie of preprocess techniques and fit twelve different classification models using the built dataset.

**2. Make a prediction:** This notebook presents a proof of work to test the generalization capacity of the model on a set of 20 archaeological samples from the northeastern coast of Spain. 

**3.MACLAS Model:** This notebook allows the use of the pre-trained models on new data.


---

**Run the following notebooks and explore how we developed and applied a Mineral Archaeological CLAssification System (MACLAS).** The nbviewer links below provide a non-interactive preview of notebooks and ![Binder](https://mybinder.org/badge_logo.svg) buttons launch
Jupyter Notebook or Jupyter Lab in your web browser.  All notebooks can also be launched directly from the links in the Workflow.ipynb top-level notebook.

---

| Nbviewer | Jupyter Notebook | Jupyter Lab | HTML |
| ---      | --               | ---         | ---  |
| [Workflow.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F0-Workflow.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/0-Workflow.html) |
| [Model_development(mineral_species).ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/1-CreateDataset.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F1-CreateDataset.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F1-CreateDataset.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/1-CreateDataset.html) |
| [Model_development(Strunz_system).ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/2-CalculateFeatures.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F2-CalculateFeatures.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F2-CalculateFeatures.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/2-CalculateFeatures.html) |
| [Proof-of-work.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/3-FitModel.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F3-FitModel.ipynb) |[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F3-FitModel.ipynb)  | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/3-FitModel.html) |
| [MACLAS.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/4-Predict.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F4-Predict.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F4-Predict.ipynb)| [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/4-Predict.html) |

---

**MACLAS.ipynb** Contains the pretrained model that can be used for predict on your own data

To enable reproducibility, we provide a data directory with all data required to run the workflow. A description of the data with download location and download date is [available](./example1/data/Datasets.md).

---
=======

