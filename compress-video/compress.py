import os
import argparse
import subprocess

def compress_video(input_path, compression_percentage):
    input_file, extension = os.path.splitext(os.path.basename(input_path))
    output_path = f'{input_file}_compressed.{extension}'
    
    ffmpeg_cmd = f'ffmpeg -i {input_path} -vf "scale=iw*{compression_percentage}:ih*{compression_percentage}" -c:v libx264 -crf 23 -preset medium -c:a copy {output_path}'

    try:
        subprocess.check_output(ffmpeg_cmd, shell=True)
        print('Compression completed successfully. Output file:', output_path)
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {e}')

def main():
    parser = argparse.ArgumentParser(description='Compress a video using FFmpeg.')
    parser.add_argument('--input', '-i', dest='input_file', required=True, help='Input video file path')
    parser.add_argument('--compression', '-c', dest='compression_percentage', type=float, required=True, help='Compression percentage (e.g., 0.5 for 50% compression)')
    args = parser.parse_args()

    compress_video(args.input_file, args.compression_percentage)

if __name__ == '__main__':
    main()
