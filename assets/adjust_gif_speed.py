from PIL import Image
import numpy as np

def slow_down_gif(input_path, output_path, speed_factor=0.8):
    # Open the GIF
    with Image.open(input_path) as img:
        # Get all frames
        frames = []
        durations = []
        for frame in range(img.n_frames):
            img.seek(frame)
            frames.append(img.copy())
            durations.append(img.info['duration'])
        
        # Calculate new durations
        new_durations = [int(duration / speed_factor) for duration in durations]
        
        # Save the new GIF
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            duration=new_durations,
            disposal=2  # Restore to background color before rendering next frame
        )

    print(f"Slowed down GIF saved as {output_path}")

# Usage
speed_factor=0.6
input_gif = "Profile_HD.gif"  # Replace with your input GIF path
output_gif = f"Profile_HD_{speed_factor}x.gif"  # Replace with your desired output path

slow_down_gif(input_gif, output_gif, speed_factor)