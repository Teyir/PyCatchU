from io import BytesIO
from tkinter import PhotoImage
import requests


def download_file(url) -> PhotoImage:
    try:
        # Initialize
        r: requests.models.Response = requests.get(
            url=url, stream=True)

        my_stream = BytesIO()

        # Chunk download
        for chunk in r.iter_content(chunk_size=128):
            # Write the downloaded chunk to the stream variable.
            my_stream.write(chunk)

        # Return PhotoImage data
        return PhotoImage(data=my_stream.getvalue())

    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
