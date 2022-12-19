import moviepy.editor as mp

# File path to the input video
input_video_path = '/path/to/input/video.mp4'

# Start and end timestamps for the video cut
start_time = '00:00:10' # 10 seconds into the video
end_time = '00:01:30' # 1 minute and 30 seconds into the video

# File path to the output video
output_video_path = '/path/to/output/video.mp4'

# Open the input video using moviepy
video = mp.VideoFileClip(input_video_path)

# Cut the video using the start and end timestamps
cut_video = video.subclip(start_time, end_time)

# Save the cut video to the specified output path
cut_video.write_videofile(output_video_path)

# Delete the original video
import os
os.remove(input_video_path)
