# Primary paper figures
Code to produce the main figures of the paper.

* Figures in .AI, .PDF and .PNG format are accessible at `results`.
* Executable IPython Notebooks to produce most panels related to this figures can be found in `notebooks`.
* Panels are stored in the `assets` folder.

## Installation

All dependencies related to these notebooks are `pip`-installable and you should be able to install them on-the-go as you encounter them. Some modules you may want to install are **fragmentembedding**, **mini-automl**, **mini-xai** and **stylia**:

```bash
git clone https://github.com/ligand-discovery/fragment-embedding
cd fragment-embedding
python -m pip install -e .
```

```bash
git clone https://github.com/ligand-discovery/mini-automl
cd mini-xai
python -m pip install -e .
```

```bash
git clone https://github.com/ligand-discovery/mini-xai
cd mini-xai
python -m pip install -e .
```

```bash
python -m pip install git+https://github.com/ersilia-os/stylia.git
```

## Disclaimer

* This repository is likely to evolve as figures are revised over manuscript iterations. Therefore, it is possible that, before publication, panel names in `assets` do not correspond to panels in the final figures.
* Likewise, some panels produced in the executable notebooks may not be part of any final figure.
* Also, please note that some figure panels were not produced with executable notebooks (e.g. in-fluorescence gels, or networks laid out with [Gephi](https://gephi.org/)).
* There are some custom paths associated to **Supplemental Figures**, since the data related to them is large and computations were conducted elsewhere.
* Similarly, for **Figure 6** data is read from the results of the [`interactome-signatures`](https://github.com/ligand-discovery/interactome-signatures) repository.