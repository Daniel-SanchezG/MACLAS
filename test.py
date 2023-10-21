#!/usr/bin/env python
import subprocess
import tempfile


def exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        print(fout.name)
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
# these notebook must be run in order
    exec_notebook('./Workflow.ipynb')
    exec_notebook('./Model_development.ipynb')
    exec_notebook('./Prediction_function.ipynb')
    exec_notebook('./MACLAS.ipynb')
    


if __name__ == '__main__':
    test()