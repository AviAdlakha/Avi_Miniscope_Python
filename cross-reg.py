minian_path = r'C:\Users\Avi\minian\minian'
dpath = r"Z:\Avi_Analysis\Avi_Python\NCFiles_29-01-2024"
f_pattern = r'^59.*\.nc$'
id_dims = ["session"]

param_dist = 5


import os
import sys
import warnings
import itertools as itt
import numpy as np
import xarray as xr
import holoviews as hv
import pandas as pd
from holoviews.operation.datashader import datashade, regrid
from dask.diagnostics import ProgressBar
sys.path.append(minian_path)
from minian.cross_registration import (calculate_centroids, calculate_centroid_distance, calculate_mapping,
                                       group_by_session, resolve_mapping, fill_mapping)
from minian.motion_correction import estimate_motion, apply_transform
from minian.utilities import open_minian, open_minian_mf
from minian.visualization import AlignViewer


minian_ds = open_minian_mf(
    dpath, id_dims, pattern=f_pattern)