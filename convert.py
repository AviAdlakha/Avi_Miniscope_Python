import itertools as itt
import os
import sys
import csv
import numpy as np
import xarray as xr

sys.path.append(r'C:\Users\Avi\minian\minian')

from minian.utilities import (
    TaskAnnotation,
    get_optimal_chk,
    load_videos,
    open_minian,
    save_minian,
)

def list_folders(path):
    try:
        entries = os.listdir(path)
        folders = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
        return folders

    except FileNotFoundError:
        return f"Folder not found: {path}"
    
if __name__ == "__main__":
    # Get user input for the folder path
    folder_path = input("Enter the  input folder path: ")
    
    # Call the function to list folders
    Animals = list_folders(folder_path)
    DataFolders=[]
    FailedSessions=[]
    for A in Animals:
        Date= list_folders(os.path.join(folder_path, A))
        for D in Date:
                Sessions= list_folders(os.path.join(folder_path,A, D))
                for S in Sessions:
                    try:
                        DataFolders.append(os.path.join(folder_path, A , D, S , 'minian-analysis\data' ))
                        minian_ds = open_minian(os.path.join(folder_path, A , D, S , 'minian-analysis\data' ))
                        minian_ds.to_netcdf(os.path.join(folder_path,A,D,S,'CalciumData.nc'))
                    except Exception as e:
                        FailedSessions.append(str(A)+'_'+str(S))
    file_path="Failed_NCFiles.csv"
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(FailedSessions)

    print('The number of sessions analysed: ' + str(len(DataFolders)))
    print('The number of sessions that failed: '+str(len(FailedSessions)))

    # Display the result
    # if isinstance(result, list):
    #     print(f"Folders in '{folder_path}':")
    #     for folder in result:
    #         print(folder)
    # else:
    #     print(result)


# minian_ds_path= r'Z:\Data\Avi_Data\Salience\ExperimentalCohort\59\2023-10-16\P3.1_100pctreward_session01\minian-analysis\data'

# minian_ds = open_minian(minian_ds_path)

# minian_ds.to_netcdf("minian_dataset.nc")

