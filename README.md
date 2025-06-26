# YouTube Video Downloader

A robust Python tool for downloading YouTube videos with various quality options, progress tracking, and error handling.

## Features

- ✅ Download videos in various resolutions (720p, 1080p, etc.)
- ✅ Audio-only downloads
- ✅ Progress tracking during downloads
- ✅ Multiple format support (MP4, WebM)
- ✅ URL validation
- ✅ Error handling and recovery
- ✅ List available resolutions
- ✅ Flexible output directory
- ✅ Cross-platform compatibility

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd video_downloader
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Download a video with highest available quality:
```bash
python yt_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Advanced Usage

**Download with specific resolution:**
```bash
python yt_downloader.py "URL_HERE" -r 1080p
```

**Download audio only:**
```bash
python yt_downloader.py "URL_HERE" --audio
```

**Specify output directory:**
```bash
python yt_downloader.py "URL_HERE" -o /path/to/downloads
```

**Download in WebM format:**
```bash
python yt_downloader.py "URL_HERE" --format webm
```

**List available resolutions:**
```bash
python yt_downloader.py "URL_HERE" --list-resolutions
```

**Combine multiple options:**
```bash
python yt_downloader.py "URL_HERE" -r 720p -o downloads --format mp4
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `url` | YouTube video URL (required) | - |
| `-o, --output` | Output directory | `downloads` |
| `-r, --resolution` | Video resolution (720p, 1080p, etc.) or 'highest' | `highest` |
| `--audio` | Download audio only | `False` |
| `--format` | Video format (mp4, webm) | `mp4` |
| `--list-resolutions` | List available resolutions and exit | `False` |

## Examples

### Example 1: Download a music video in highest quality
```bash
python yt_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Example 2: Download a tutorial in 720p
```bash
python yt_downloader.py "https://www.youtube.com/watch?v=example" -r 720p
```

### Example 3: Extract audio from a video
```bash
python yt_downloader.py "https://www.youtube.com/watch?v=example" --audio
```

### Example 4: Check available resolutions first
```bash
python yt_downloader.py "https://www.youtube.com/watch?v=example" --list-resolutions
```

## Output

The tool provides detailed feedback during the download process:

```
[*] Video Title: Example Video Title
[*] Video Length: 180 seconds
[*] Views: 1,234,567
[*] Selected stream: 1080p (video/mp4)
[*] File size: 45.2 MB
Downloading... 67.3% (30485760/45234567 bytes)
[+] Download completed successfully!
[+] File saved: downloads/Example Video Title.mp4
```

## Error Handling

The tool includes comprehensive error handling for:
- Invalid YouTube URLs
- Network connectivity issues
- Unavailable video streams
- Permission errors
- Disk space issues

## Troubleshooting

### Common Issues

1. **"pytube is not installed"**
   ```bash
   pip install pytube
   ```

2. **"Invalid YouTube URL"**
   - Ensure the URL is a valid YouTube video URL
   - Supported formats: youtube.com/watch?v=, youtu.be/, youtube.com/embed/

3. **"No suitable stream found"**
   - Try different resolutions
   - Use `--list-resolutions` to see available options
   - Some videos may have restrictions

4. **Download fails**
   - Check internet connection
   - Verify video is not private/restricted
   - Try different format with `--format webm`

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws. Only download videos you have permission to download.