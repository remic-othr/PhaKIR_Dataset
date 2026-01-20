# PhaKIR_Dataset

This repository provides code for pre-processing the PhaKIR dataset. 

To split the provided videos into individual frames, the script `split_video_in_frames.py` can be used. This will reproduce the same folder structure that was used during the PhaKIR challenge: for improved accessibility, frames are grouped in folders of 1,000, and all frame numbers are padded to six digits to ensure consistency with the segmentation mask filenames. Detailed instructions are as follows:

## Instructions for Frame Extraction

* Place the script `split_video_in_frames.py` in the same folder as the video files.
* Run the script with the video number to split it into frames. For example, to process video 01, use the following command:

  ```bash
  python split_video_in_frames.py 01
  ```
* A new folder named `Frames` will be generated, containing a subfolder for the individual video. The video frames are stored with six-digit padded numbers to ensure consistency with the segmentation mask filenames and grouped in folders of 1,000 for improved accessibility.

> **Note:** The default compression level for the resulting `.png` frames is set to `3`, which is the default of the `cv2.imwrite` function. Depending on available storage and specific requirements, this value (in line 49) can be adjusted between `0` (no compression, fastest access) and `9` (maximum compression, slowest access).
