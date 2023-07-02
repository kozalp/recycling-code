from rdkit.Chem import MolFromSmiles
from rdkit import DataStructs
from rdkit.Chem.AllChem import GetMorganFingerprintAsBitVect
from chembl_structure_pipeline import standardizer
import pandas as pd
import numpy as np


def generate_ECFP6(df: pd.DataFrame, smilescol: str = "SMILES") -> list:
    ROMols = [MolFromSmiles(smile) for smile in df["SMILES"]]
    stROMols = [standardizer.standardize_mol(ROMol) for ROMol in ROMols]
    fps = [
        GetMorganFingerprintAsBitVect(stROMol, 3, nBits=1024) for stROMol in stROMols
    ]

    efps = []

    for fp in fps:
        arr = np.zeros((1,))
        DataStructs.ConvertToNumpyArray(fp, arr)
        efps.append(arr)

    return efps
