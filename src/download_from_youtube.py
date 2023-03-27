import yt_dlp

from main import write_captions_to_srt_file


def download_audio_from_youtube(youtube_url, output_folder, output_filename):
    print("Downloading audio from YouTube ...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/{output_filename}.%(ext)s',
        'merge_output_format': 'mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


if __name__ == '__main__':
    URL = 'https://www.youtube.com/watch?v=uQb5CkDillA'
    download_audio_from_youtube(URL, "../downloads", "temp")
    write_captions_to_srt_file(vid_name='temp.mp3',
                               do_translation=False,
                               source_folder="../downloads/",
                               result_folder='../srt_files/')
