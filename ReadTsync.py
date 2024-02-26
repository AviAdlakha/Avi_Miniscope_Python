import edlio
import csv
import os
import tkinter as tk
from tkinter import filedialog

def open_folder_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(title="Select a Folder")
    return folder_path


def create_timestamps(directory):
    folder_list = [folder for folder in os.listdir(os.path.join(directory, 'videos'))]

    # load our data collection
    dcoll = edlio.load(directory)

    for whichvideo in {'miniscope'}:
    # get the miniscope video dataset
        dset = dcoll.group_by_name('videos').dataset_by_name(whichvideo)

        # read auxiliary tsync data files - we assume there is only one such file here
        tsync_data = [tsync for tsync in dset.read_aux_data('tsync')]
        #assert len(tsync_data) == 1
        #tsync = tsync_data[0]

        # Create the directory if it doesn't exist

        timestampfolder= os.path.join(directory, 'videos',whichvideo,'timestamps')
        os.makedirs(timestampfolder, exist_ok=True)
        for i in range(len(tsync_data)):  
            # CSV filename based on iteration
            padded_number = str(i+1).zfill(2)
            csv_filename = f'Timestamps_{padded_number}.csv'
            csv_filepath = os.path.join(timestampfolder, csv_filename)
            tsync=tsync_data[i]
            # Writing to CSV file
            with open(csv_filepath, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(tsync.times)

            print(f'{csv_filename} created successfully!')


chosen_directory = open_folder_dialog()

for folder in os.listdir(chosen_directory):
    for subfolder in os.listdir(os.path.join(chosen_directory,folder)):
        for subsubfolder in os.listdir(os.path.join(chosen_directory,folder,subfolder)):
            try:
                create_timestamps(os.path.join(chosen_directory,folder,subfolder,subsubfolder))
            except:
                print("error in",subfolder,subsubfolder)



# print some information
# print('Labels:', tsync.time_labels)
# print('Units:', tsync.time_units)
# print('Creation Date:', tsync.time_created)

# # get a (X, 2) matrix mapping frame numbers to time stamps (in this case,
# # ensure your tsync units and labels match your expectations!)
# print(tsync.times)