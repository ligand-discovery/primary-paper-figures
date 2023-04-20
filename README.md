# Primary paper figures
Code to produce the main figures of the paper.

* Figures in .AI, .PDF and .PNG format are accessible at `results`.
* Executable IPython Notebooks to produce most panels related to this figures can be found in `notebooks`.
* Panels are stored in the `assets` folder.

## Installation

All dependencies related to these notebooks are `pip`-installable and you should be able to install them on-the-go as you encounter them. Two modules you may want to install are **stylia** and **fragmentembedding**:

```bash
git clone https://github.com/ligand-discovery/fragment-embedding
cd fragment-embedding
python -m pip install -e .
```

```bash
python -m pip install git+https://github.com/ersilia-os/stylia.git
```

## Disclaimer

* There are some custom paths associated to **Supplemental Figures**, since the data related to them is large and computations were conducted elsewhere.
* Similarly, for **Figure 5** data is read from the results of the [`interactome-signatures`](https://github.com/ligand-discovery/interactome-signatures) repository.