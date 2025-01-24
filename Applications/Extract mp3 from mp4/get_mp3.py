import moviepy
import moviepy.editor


video = moviepy.editor.VideoFileClip("")    # Put your file path in here

# Convert video to audio
audio = video.audio
audio.write_audiofile('new_audio.mp3')