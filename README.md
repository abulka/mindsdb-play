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

