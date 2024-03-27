XCROCO-LOPS
====== 




Installation
=============

Install miniconda:
Download Miniconda3 (i.e. for python3) from the [conda website](https://conda.io/miniconda.html) and run:
```
./Miniconda3-latest-Linux-x86_64.sh
```

Download the repository:
```
git clone https://gitlab.inria.fr/croco-ocean/devs/gcambon/xcroco-lops.git
```

Install an appropriate conda-environment:
```
cd xcroco-lops
conda env create -f environment.yml
conda activate xcroco-lops-env
```

Install the xcroco-lops project in the conda environment
```
pip install .
```
see also [conda doc](doc/conda.md)

In order to add the environnement to kernels available to jupyter, you need to run:
```
python -m ipykernel install --user --name xcroco-lops-env --display-name "xcroco-lops-env"
```
