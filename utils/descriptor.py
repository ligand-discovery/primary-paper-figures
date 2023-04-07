import pandas as pd
import os
from dataclasses import dataclass

from rdkit import Chem
from rdkit.Chem import MolFromSmarts


@dataclass
class Descriptors:
    """Molecular descriptors"""

    #: Descriptor type
    descriptor_type: str
    #: Descriptor values
    descriptors: tuple
    # Descriptor name
    descriptor_names: tuple
    # t_stats for each molecule
    tstats: tuple = ()


def _calculate_rdkit_descriptors(mol):
    from rdkit.ML.Descriptors import MoleculeDescriptors  # type: ignore

    dlist = [
        "NumHDonors",
        "NumHAcceptors",
        "MolLogP",
        "NumHeteroatoms",
        "RingCount",
        "NumRotatableBonds",
    ]
    c = MoleculeDescriptors.MolecularDescriptorCalculator(dlist)
    d = c.CalcDescriptors(mol)

    def calc_aromatic_bonds(mol):
        return sum(1 for b in mol.GetBonds() if b.GetIsAromatic())

    def _create_smarts(SMARTS):
        s = ",".join("$(" + s + ")" for s in SMARTS)
        _mol = MolFromSmarts("[" + s + "]")
        return _mol

    def calc_acid_groups(mol):
        acid_smarts = (
            "[O;H1]-[C,S,P]=O",
            "[*;-;!$(*~[*;+])]",
            "[NH](S(=O)=O)C(F)(F)F",
            "n1nnnc1",
        )
        pat = _create_smarts(acid_smarts)
        return len(mol.GetSubstructMatches(pat))

    def calc_basic_groups(mol):
        basic_smarts = (
            "[NH2]-[CX4]",
            "[NH](-[CX4])-[CX4]",
            "N(-[CX4])(-[CX4])-[CX4]",
            "[*;+;!$(*~[*;-])]",
            "N=C-N",
            "N-C=N",
        )
        pat = _create_smarts(basic_smarts)
        return len(mol.GetSubstructMatches(pat))

    def calc_apol(mol, includeImplicitHs=True):
        # atomic polarizabilities available here:
        # https://github.com/mordred-descriptor/mordred/blob/develop/mordred/data/polarizalibity78.txt

        ap = os.path.join("../data", "atom_pols.txt")
        with open(ap, "r") as f:
            atom_pols = [float(x) for x in next(f).split(",")]
        res = 0.0
        for atom in mol.GetAtoms():
            anum = atom.GetAtomicNum()
            if anum <= len(atom_pols):
                apol = atom_pols[anum]
                if includeImplicitHs:
                    apol += atom_pols[1] * atom.GetTotalNumHs(includeNeighbors=False)
                res += apol
            else:
                raise ValueError(f"atomic number {anum} not found")
        return res

    d = d + (
        calc_aromatic_bonds(mol),
        calc_acid_groups(mol),
        calc_basic_groups(mol),
        calc_apol(mol),
    )
    return d


def classic_featurizer(smiles):
    names = tuple(
        [
            "HBD",
            "HBA",
            "cLogP",
            "Heteroatoms",
            "Rings",
            "Rot. Bonds",
            "Aromatic Bonds",
            "Acidic Groups",
            "Basic Groups",
            "Atomic Polarizability",
        ]
    )
    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
    R = []
    cols = None
    for m in mols:
        descriptors = _calculate_rdkit_descriptors(m)
        descriptor_names = names
        descriptors = Descriptors(
            descriptor_type="Classic",
            descriptors=descriptors,
            descriptor_names=descriptor_names,
        )
        R += [list(descriptors.descriptors)]
        if cols is None:
            cols = list(descriptors.descriptor_names)
    data = pd.DataFrame(R, columns=cols)
    return data