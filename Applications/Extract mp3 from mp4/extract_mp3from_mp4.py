import moviepy
import moviepy.editor
import tkinter as tk
from tkinter.filedialog import askopenfilename ,asksaveasfilename

global open_file_path
global save_file_path

# to get file path of video file./
def fileopen():
    global open_file_path
    open_file_path = askopenfilename(
    filetypes=[("All Files", "*.*")]
    )
    if not open_file_path:
        return
    open_path.insert(0, open_file_path)


def filesave():
    global save_file_path
    save_file_path = (asksaveasfilename(
    filetypes=[("audio file", '*.MP3'),("All files", '*.*')]
    ) + ".mp3")
    if not save_file_path:
        return
    save_path.insert(0, save_file_path)


def file_convert(video_file,audio_file):         # Here video_file and audio_file are the file paths.
    video = moviepy.editor.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)
    popup = tk.Toplevel()
    popup.title("completed!")
    popup_text=tk.Label(popup, text="sucessfully converted and saved to your location \n\n\n credits:qxresearch @ GitHub ",height=10).pack(side=tk.TOP,anchor='nw')
    popup.mainloop()


uiwindow = tk.Tk()
uiwindow.title("video to audio converter")
main_frame = tk.Frame(uiwindow, height=20,width=80).pack(side=tk.TOP, fill=tk.BOTH)
open_label = tk.Label(main_frame, text="enter the path of the video file to be converted:").pack(side=tk.TOP ,anchor='w')
open_path = tk.Entry(main_frame, width=50)
open_path.pack(side=tk.TOP, fill=tk.BOTH)
open_Button = tk.Button(main_frame, text="Browse..",bg="sky Blue",command = lambda:fileopen()).pack(side=tk.TOP, anchor='e')
empty_space = tk.Label(main_frame, height=3).pack(side=tk.TOP,fill=tk.BOTH)
save_label = tk.Label(main_frame, text="enter the path for the converted audio file to be saved:",height=1).pack(side=tk.TOP ,anchor='w')
save_path = tk.Entry(main_frame, width=50)
save_path.pack(side=tk.TOP, fill=tk.BOTH)
save_button = tk.Button(main_frame, text="Browse..",bg="sky Blue", command=lambda:filesave()).pack(side=tk.TOP, anchor='e')
empty_space2 = tk.Label(uiwindow, text="______________________________________________________________________",height=2,fg="green")
empty_space2.pack(side=tk.TOP,fill=tk.BOTH,anchor='s')
second_frame = tk.Frame(uiwindow,width=100).pack(side=tk.TOP)
convert_button = tk.Button(second_frame, text="convert",bg="pink",borderwidth=4,command=lambda:[file_convert(open_file_path,save_file_path)])
convert_button.pack(side=tk.RIGHT, anchor='ne', padx=5,pady=5)
cancel_Button = tk.Button(second_frame, text="cancel",bg="pink",borderwidth=4,command=lambda:uiwindow.destroy()).pack(side=tk.RIGHT, anchor='ne',padx=5, pady=5)
uiwindow.mainloop()
