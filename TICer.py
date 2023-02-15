#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Written by Jessie Taylor, 2023 (MIT License)
import pandas as pd
from astroquery.simbad import Simbad
import numpy as np

def TICer(KIC_ID: str):
  """ 
  Function which uses the Simbad database to obtain
  the TIC identifier of a star using the KIC identifier
  
  Parameters
  ----------
  KIC_ID : str
      The Kepler (KIC) ID of the star, added without 
      the "KIC" string at the beginning, so just the numbers.
  
  Yields
  ------
  TIC_ID : str
      The associated TIC identifier of the input star

  """
  # Obtain all associated IDs with the given KIC#
  ids = Simbad.query_objectids(("KIC" + KIC_ID))
  # Convert to dataframe
  dfids = pd.DataFrame()
  dfids["ID"] = ids.to_pandas() 
  # Properly decode
  dfids["ID"] = dfids["ID"].str.decode("utf-8")
  # Generate mask so only entries which state they
  tic_mask = dfids["ID"].str.startswith("TIC")
  # Apply mask
  dfids_masked = dfids[tic_mask]
  # Convert to string and split to get list with entry 1 as TIC# (with no "TIC")
  TIC_ID = dfids_masked.to_string().split("TIC ")[1]
  
  #print("KIC_ID =", KIC_ID, "\nTIC_ID =", TIC_ID)
  return TIC_ID


if __name__ != "__main__":
    print("TICer successfully imported")
    
