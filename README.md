# PhaKIR_Dataset

This repository provides code for pre-processing the PhaKIR dataset. 

To split the provided videos into individual frames, the script `split_video_in_frames.py` can be used. This will reproduce the same folder structure that was used during the PhaKIR challenge: frames are grouped in folders of 1,000 and all frame numbers are padded to six digits. Detailed instructions are as follows:

## Instructions for Frame Extraction

* Place the script in the same folder as the video files.
* Run the script with the video number to split it into frames. For example, to process video 01, use the following command:

  ```bash
  python split_video_in_frames.py 01
  ```
* A new folder named `Frames` will be generated, containing a subfolder for the individual video. The video frames are stored with six-digit padded numbers and grouped in folders of 1,000.
