import argparse
from pathlib import Path
from loguru import logger
from soundclouddownloader.main import SoundCloudDownloader


def run(playlist_url: str, output_dir: Path, should_zip: bool = False):
    """
    Run the download using non-interactive input (for CLI or GitHub Actions).
    """
    downloader = SoundCloudDownloader()
    result = downloader.download_playlist(
        playlist_url, output_dir, max_workers=3, should_zip=should_zip
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for SoundCloud Downloader")
    parser.add_argument("--url", required=True, help="SoundCloud playlist URL")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()

    output_path = Path(args.output).resolve()
    output_path.mkdir(parents=True, exist_ok=True)

    run(args.url, output_path, False)
