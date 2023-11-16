If in same folder -
python compress.py --input input.mp4 --compression 0.5

Else -
python compress.py --input "C:\Users\user_name\Videos\input.mp4" --compression 0.5

- Make sure you have FFmpeg installed and set it as an environment variable - https://ffmpeg.org/download.html
- Compression is % of compression needed.
- Use --input or -i, --compression or -c
- Output will be stored in the same folder as the script
