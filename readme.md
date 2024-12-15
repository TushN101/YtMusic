# YtMusic.py

![Capture](https://github.com/user-attachments/assets/5c8b8447-f919-4d9b-9b08-41945ece720d)

YtMusic.py is a Python script that allows you to download and manage your favorite music directly from YouTube in the best available audio quality. The script organizes downloads in a local folder and provides features like folder management, playback, and playlist cleanup, all from the command line.

## Features

- **Download Music**: Fetch audio tracks from YouTube in high-quality formats.
- **Playlist Management**: Organize and clean your music library effortlessly.
- **VLC Integration**: Play downloaded music directly using VLC Media Player.
- **Cross-Platform Compatibility**: Designed for Windows users.

## Prerequisites

Before using this script, ensure the following dependencies are installed:

1. **Python 3.6+**
2. **Required Packages**:
    - [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading content from YouTube.
    - Other Python modules like `os` and `subprocess` (default in Python).
3. **VLC Media Player**:
    - Install VLC from [VideoLAN](https://www.videolan.org/).
    - Ensure VLC is added to your system's PATH or use the default installation path in the script.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/YtMusic.py.git
cd YtMusic.py
```

2. Install dependencies:

```bash
pip install yt-dlp
```

3. Run the script:

```bash
python YtMusic.py
```

## Usage

### Main Menu

The script provides the following options in its interactive menu:

1. **Add music to library**
    - Enter a YouTube URL to download audio in the best quality.
2. **Open playlist folder**
    - Opens the folder where downloaded tracks are stored.
3. **Open music player**
    - Launch VLC Media Player to play your downloaded music.
4. **Format playlist folder**
    - Clears all files in the playlist folder.
5. **Exit**
    - Exits the script.

### Default File Structure

All music is stored in a dedicated folder within the `Documents` directory:

```text
Documents/YtMusic-Vault/
```

### Example

To download a song, simply select option `1` and provide the YouTube video URL. The script will download the audio and save it in the `YtMusic-Vault` folder.

## Troubleshooting

- **VLC Error**:
    - Ensure VLC is installed and accessible at `C:\Program Files\VideoLAN\VLC\vlc.exe` (default path).
    - Update the VLC path in the script if needed.
- **yt-dlp Not Found**:
    - Ensure `yt-dlp` is installed using `pip install yt-dlp`.
    - Verify Python's `Scripts` directory is in your system PATH.

## Disclaimer

This script is intended solely for personal use to manage and organize your music library. The downloads utilize public YouTube content via Python libraries such as `yt-dlp`. It is not designed to bypass or infringe upon YouTube's terms of service or its premium services such as YouTube Music. Users are advised to ensure compliance with YouTube's guidelines and copyright policies when using this tool.

---

