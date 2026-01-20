import sys
import os
import cv2

##############################
### Instructions:
### - Put video files together with this script in one folder.
### - Execute this script with the video number to split into frames, e. g., with the following command for video 01: 'python split_video_in_frames.py 01'
### - A new folder 'Frames' is created, where the single frames of the video are stored into.
##############################

def split(video_number):

    video_number = str(video_number)

    print('Video number: ' + video_number)    

    filename = './Video_' + video_number + '.mp4'

    capture = cv2.VideoCapture(filename)

    save_path = './Frames/Video_' + video_number

    if(os.path.exists('./Frames') == False):
        os.makedirs('./Frames')

    if(os.path.exists(save_path) == False):
        os.makedirs(save_path)


    frameNr = 0
    
    while (True):

        success, frame = capture.read()

        folders = range(0, 100000000, 1000)

        for f in range(len(folders)):
            if(frameNr >= folders[f] and frameNr < folders[f + 1]):
                curr_subdir = str(folders[f])
    
        if success:
            frame_save_path = os.path.join(save_path, curr_subdir)

            if(os.path.exists(frame_save_path) == False):
                os.makedirs(frame_save_path)

            cv2.imwrite(os.path.join(frame_save_path, 'frame_' + str(frameNr).zfill(6) + '.png'), frame, [cv2.IMWRITE_PNG_COMPRESSION, 3])
    
        else:
            break


        print('Finished ' + str(frameNr) + ' frames.')
    
        frameNr += 1
    
    capture.release()


video_number = str(sys.argv[1])
split(video_number)