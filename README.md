# Subtitle-Converter
Converts subtitles in a "given" wrong format to a standard SRT format

## Features:
It converts all the subtitles with the extension SRT in your folder to a standard SRT format.

## Intro:
I basically made this python file to convert [subtitles for Udacity Videos](http://d2uz2655q5g6b2.cloudfront.net/2980038599/Lesson%201%20Subtitles.zip), and you can use it now.

## Requirements:
- Python 2.7 installed on your computer
- subtitle files with extension SRT of the same format as [sample_wrong_subtitle.srt](sample_wrong_subtitle.srt)

## How to Use:
You have a folder, say Videos_and_Subtitles_folder, and it contains videos like video_01.mp4, video_01.srt, other_video_02.mp4, other_video_02.srt and so on. 

You [download this python file:](batch_subtitle_converter.py) and move it inside the folder containing subtitles. 

Then run this python file, either by double-clicking it or by command line, 

and it will convert the srt files like video_01.srt, other_video_02.srt and so on to a standard SRT format that VLC can understand.

Take this [sample_wrong_subtitle.srt](sample_wrong_subtitle.srt) subtitle to try this [python file](batch_subtitle_converter.py) on.
