# Video Splitter

A simple Python script to split videos at a specified timeline using moviepy.

## Installation

1. Make sure you have Python installed on your system
2. Install the required package using pip:
```bash
pip install moviepy==1.0.3
```

## Usage

1. Place your video file in the same directory as the script (or you can use full path)
2. Run the script:
```bash
python video_splitter.py
```

3. When prompted:
   - The script will use "attribute.mkv" as the input video file
   - It will create two output files: "part1.mp4" and "part2.mp4"
   - Enter the time (in seconds) where you want to split the video

Example:
```
Enter the time to split the video (in seconds): 30
```
This will split the video at the 30-second mark.

## Features

- Splits any video file at a specified time
- Supports various video formats (thanks to moviepy)
- Automatically handles video resources
- Provides error handling and validation
- Shows progress while processing

## Requirements

- Python 3.x
- moviepy 1.0.3

## Error Handling

The script includes error handling for:
- Invalid split times
- Missing input files
- Invalid time format inputs
- Split time exceeding video duration

## Notes

- The output files will be in MP4 format
- Make sure you have enough disk space for both output files
- The process may take some time depending on the video size and duration

## Example

If you have a 2-minute video and want to split it at 1 minute:
```python
Enter the time to split the video (in seconds): 60
```
This will create:
- part1.mp4 (0:00 to 1:00)
- part2.mp4 (1:00 to end)
