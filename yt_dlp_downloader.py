#!/usr/bin/env python3
"""
YouTube Video Downloader using yt-dlp
A more robust alternative to pytube that handles YouTube API changes better.
"""

import argparse
import os
import sys
import subprocess
import json
from typing import Optional, List

def check_yt_dlp_installed() -> bool:
    """Check if yt-dlp is installed."""
    try:
        result = subprocess.run(['yt-dlp', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"✅ yt-dlp version: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ yt-dlp is not installed")
        print("   Install with: pip install yt-dlp")
        return False

def validate_youtube_url(url: str) -> bool:
    """Basic YouTube URL validation."""
    youtube_patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+',
        r'(?:https?://)?(?:www\.)?youtu\.be/[\w-]+',
        r'(?:https?://)?(?:www\.)?youtube\.com/embed/[\w-]+'
    ]
    
    import re
    for pattern in youtube_patterns:
        if re.match(pattern, url):
            return True
    return False

def get_video_info(url: str) -> Optional[dict]:
    """Get video information using yt-dlp."""
    try:
        cmd = [
            'yt-dlp',
            '--dump-json',
            '--no-playlist',
            url
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error getting video info: {e.stderr}")
        return None
    except json.JSONDecodeError:
        print("[!] Error parsing video information")
        return None

def list_formats(url: str) -> bool:
    """List available formats for the video."""
    try:
        print(f"[*] Getting available formats for: {url}")
        
        cmd = [
            'yt-dlp',
            '--list-formats',
            '--no-playlist',
            url
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"[!] Error listing formats: {e.stderr}")
        return False

def download_video(url: str, output_path: str = 'downloads', 
                  format_spec: str = 'best', audio_only: bool = False) -> bool:
    """
    Download video using yt-dlp.
    
    Args:
        url: YouTube video URL
        output_path: Output directory
        format_spec: Format specification (e.g., 'best', 'worst', 'best[height<=720]')
        audio_only: If True, download audio only
    """
    try:
        # Create output directory
        os.makedirs(output_path, exist_ok=True)
        
        # Build command
        cmd = [
            'yt-dlp',
            '--output', f'{output_path}/%(title)s.%(ext)s',
            '--no-playlist',
            '--progress',
        ]
        
        # Add format specification
        if audio_only:
            cmd.extend(['--extract-audio', '--audio-format', 'mp3'])
            cmd.extend(['--format', 'bestaudio[ext=m4a]/bestaudio[ext=mp3]/bestaudio'])
        else:
            cmd.extend(['--format', format_spec])
        
        # Add URL
        cmd.append(url)
        
        print(f"[*] Starting download with command: {' '.join(cmd)}")
        print(f"[*] Output directory: {output_path}")
        
        # Run download
        result = subprocess.run(cmd, check=True)
        
        if result.returncode == 0:
            print(f"[+] Download completed successfully!")
            return True
        else:
            print(f"[!] Download failed with return code: {result.returncode}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"[!] Download error: {e}")
        return False
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        return False

def main():
    """Main function to handle command line arguments and execute download."""
    parser = argparse.ArgumentParser(
        description="YouTube Video Downloader using yt-dlp - More robust than pytube",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  %(prog)s "URL_HERE" -f "best[height<=720]"
  %(prog)s "URL_HERE" --audio
  %(prog)s "URL_HERE" --list-formats
  %(prog)s "URL_HERE" -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
        """
    )
    
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", default="downloads", 
                       help="Output directory (default: downloads)")
    parser.add_argument("-f", "--format", default="best",
                       help="Format specification (default: best)")
    parser.add_argument("--audio", action="store_true",
                       help="Download audio only (MP3)")
    parser.add_argument("--list-formats", action="store_true",
                       help="List available formats and exit")
    parser.add_argument("--info", action="store_true",
                       help="Show video information and exit")
    
    args = parser.parse_args()
    
    # Check if yt-dlp is installed
    if not check_yt_dlp_installed():
        sys.exit(1)
    
    # Validate URL
    if not validate_youtube_url(args.url):
        print(f"[!] Error: Invalid YouTube URL: {args.url}")
        sys.exit(1)
    
    try:
        if args.info:
            # Show video information
            info = get_video_info(args.url)
            if info:
                print(f"[*] Video Title: {info.get('title', 'Unknown')}")
                print(f"[*] Duration: {info.get('duration', 'Unknown')} seconds")
                print(f"[*] Uploader: {info.get('uploader', 'Unknown')}")
                print(f"[*] View Count: {info.get('view_count', 'Unknown'):,}")
                print(f"[*] Upload Date: {info.get('upload_date', 'Unknown')}")
            return
        
        if args.list_formats:
            # List available formats
            if not list_formats(args.url):
                sys.exit(1)
            return
        
        # Proceed with download
        success = download_video(
            url=args.url,
            output_path=args.output,
            format_spec=args.format,
            audio_only=args.audio
        )
        
        if not success:
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n[!] Download cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 