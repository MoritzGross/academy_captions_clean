import streamlit as st

from download_from_youtube import download_audio_from_youtube
from main import write_captions_to_srt_file

st.markdown(open("README.md", "r").read())

yt_url = st.text_input("Enter the youtube URL here")

if yt_url != "":
    with st.spinner("May take a few minutes ..."):
        download_audio_from_youtube(yt_url, "../downloads", "temp")
        write_captions_to_srt_file(vid_name='temp.mp3',
                                   do_translation=False,
                                   source_folder="../downloads/",
                                   result_folder='srt_files/')

    with open('srt_files/temp_DE.srt', 'r') as f:
        st.download_button(
            label="Download SRT file",
            data=f,
            file_name="xentral_subtitle.srt",
            mime="text/plain")
