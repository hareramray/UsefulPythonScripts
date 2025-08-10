from moviepy.editor import VideoFileClip

def split_video(input_path, output_path1, output_path2, split_time):
    """
    Split a video into two parts at the specified time.
    
    Args:
        input_path (str): Path to the input video file
        output_path1 (str): Path for the first part of the video
        output_path2 (str): Path for the second part of the video
        split_time (float): Time in seconds where to split the video
    """
    try:
        # Load the video
        video = VideoFileClip(input_path)
        
        # Get the duration of the video
        duration = video.duration
        
        if split_time >= duration:
            raise ValueError("Split time cannot be greater than or equal to video duration")
        
        # Create the first part of the video
        first_part = video.subclip(0, split_time)
        first_part.write_videofile(output_path1)
        
        # Create the second part of the video
        second_part = video.subclip(split_time, duration)
        second_part.write_videofile(output_path2)
        
        # Close the video to free up resources
        video.close()
        first_part.close()
        second_part.close()
        
        print(f"Video successfully split into {output_path1} and {output_path2}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Get input from user
    input_video = "attribute.mkv"
    output_part1 = "part1.mp4"
    output_part2 = "part2.mp4"
    
    try:
        split_time = float(input("Enter the time to split the video (in seconds): "))
        split_video(input_video, output_part1, output_part2, split_time)
    except ValueError as e:
        print("Please enter a valid number for the split time.")
