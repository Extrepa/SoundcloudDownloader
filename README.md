# SoundCloud Downloader

## Description

The easiest way to run this is to fork and run via github actions.

This project provides a Python script for downloading entire playlists from SoundCloud. It uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to handle the downloading process, making it robust against changes in SoundCloud's website structure. The script downloads each track in the playlist, converts them to MP3 format, and optionally packages them into a zip file.

This project uses Poetry for dependency management and packaging. If you haven't installed Poetry yet, you can do so by following the [official installation guide](https://python-poetry.org/docs/#installation).

## Requirements

- Python 3.10+
- yt-dlp
- FFmpeg
- Poetry


## Running the program
You have 2 options:
### 1. Github Actions

- The simplest and fastest way to get your own hosted version
- Simply fork this repo and run via Github action

### 2. Local Installation

1. Clone this repository:
```python
git clone https://github.com/cainky/soundclouddownloader.git
```

2. Install the required Python packages:
```python
poetry install
```

3. Install FFmpeg:
- On Ubuntu or Debian: `sudo apt-get install ffmpeg`
- On macOS with Homebrew: `brew install ffmpeg`
- On Windows, download from the [official FFmpeg website](https://www.ffmpeg.org/download.html) and add it to your PATH.

## Usage

1. Run the script:

```python
cd soundclouddownloader
poetry run python main.py
```

2. When prompted, enter the URL of the SoundCloud playlist you want to download. Paste the entire url including the `?si=` part. Playlist can be private, just use the Share button to get the private link.

3. Enter Y/n if you want the script to create a zip file of all the tracks.

4. Enter the output directory where you want the files to be saved (or press Enter to use the `output` directory).

5. The script will download all tracks in the playlist, convert them to MP3, and optionally create a zip file containing all the tracks.

## Running tests
```bash
poetry run python -m unittest discover
```

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](./LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Please respect copyright laws and SoundCloud's terms of service when using this script. The authors are not responsible for any misuse of this software.
