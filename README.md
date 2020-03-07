Playing around with mindsdb
===========================

Doco

- https://mindsdb.github.io/mindsdb/docs/predictor-interface 
- https://mindsdb.github.io/mindsdb/docs/data-sources


Installing mindsdb on windows
=============================

pipenv install mindsdb

might fail so 
pip uninstall scikit-learn
pip install scikit-learn

if you have problems installing pytorch, see
https://stackoverflow.com/questions/60137572/issues-installing-pytorch-1-4-no-matching-distribution-found-for-torch-1-4
and possibly install pytorch first, within the pipenv virtual environment, and possibly a specific version of pytorch e.g. pip install torch===1.4.0 

vscode
======
Set-ExecutionPolicy RemoteSigned
using powershell to avoid warnings re running activate.ps1
https://github.com/Microsoft/vscode-python/issues/2559

Installing on Mac
=================

Worked ok for Python 3.7 but with Python 3.8
ERROR: No matching distribution found for sentencepiece==0.1.85 
see https://github.com/google/sentencepiece/issues/411 
This issue persists on MacOS because MacOS did not have a 3.8 wheel released, and therefore v0.1.83 is still attempted with a pip install. 

Solution: Use Python 3.7

