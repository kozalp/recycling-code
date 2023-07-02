######## LIBRARIES ########

import pandas as pd
import os
import sys
from rdkit import RDLogger

#### Disable uncritical rdkit logging messages
logger = RDLogger.logger()
logger.setLevel(RDLogger.CRITICAL)

#### Add source code (src) folder to the system path
sys.path.append(os.getcwd() + "/src")
from utils.utils import generate_ECFP6  # the function from the utils.py file

######## CODE ########
path = r"/Users/mk/Documents/projects/recycling-code/data/AID_54381_datatable.csv"
df = pd.read_csv(path)
fps = generate_ECFP6(df)
print(fps)
