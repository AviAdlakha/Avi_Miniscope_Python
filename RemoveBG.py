import cv2
from moviepy.editor import VideoFileClip
import os

videofolder = r'Z:\DLC\try\59\2023-10-21\P3.1_100pctreward_session05\videos\hispeed1'  # Replace with your video folder path

video_files = [file for file in os.listdir(videofolder) if file.endswith('.mkv')]

for video_file in video_files:
    # Create a VideoCapture object
    video_path = os.path.join(videofolder, video_file)
    video_reader = cv2.VideoCapture(video_path)

    # Read the first frame
    ret, first_frame = video_reader.read()

    # Create output directory and file
    parts = video_file.split('.')
    directory_path = r'Z:\DLC\try\59\2023-10-21\P3.1_100pctreward_session05\videos\hispeed1_nbg'  # Replace with your desired output directory
    output_video_file = os.path.join(directory_path, parts[0] + '.avi')

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f'Directory {directory_path} created.')

    # Define VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can also try 'MJPG' for better compression
    output_video_writer = cv2.VideoWriter(output_video_file, fourcc, 30.0, (first_frame.shape[1], first_frame.shape[0]))

    # Process each frame, subtracting the first frame
    while ret:
        # Read the current frame
        ret, frame = video_reader.read()

        if ret:
            processed_frame = cv2.subtract(255 - first_frame, 255 - frame)

            if videofolder.endswith('2'):
                processed_frame = cv2.rotate(processed_frame, cv2.ROTATE_180)

            # Write the processed frame to the output video file
            output_video_writer.write(255 - processed_frame)

    # Release resources
    video_reader.release()
    output_video_writer.release()

    print(f'Processing complete. {output_video_file} created')
