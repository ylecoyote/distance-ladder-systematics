---
name: Video Processor
description: Process video files with audio extraction, format conversion (mp4, webm), and Whisper transcription. Use when user mentions video conversion, audio extraction, transcription, mp4, webm, ffmpeg, or whisper transcription.
---

# Video Processor

## MCP Tool Recommendations

### Vibe-Check (Quality/Performance Validation)
**Use when:**
- User needs transcription for production or publication (not just draft)
- User mentions quality requirements or accuracy concerns
- User requests batch processing of many files (resource planning)
- User hasn't specified Whisper model size (default is `base`)

**Example trigger**: "Transcribe this interview for my podcast" or "I need accurate subtitles for my YouTube video"

**Why**: Video processing involves quality vs speed tradeoffs. Vibe-check helps validate user expectations and prevent rework:
- **Model selection**: Is `base` sufficient, or does user need `medium`/`large` for publication quality?
- **Processing time**: Is user aware that `large` model takes 10x longer than `tiny`?
- **Audio quality**: Should audio be extracted and reviewed before full transcription?
- **Format choice**: Does user need SRT for web, VTT for accessibility, or plain text?

**Validation questions**:
- What will this transcription be used for? (draft notes vs publication)
- How important is accuracy? (quick draft vs must be perfect)
- Is processing time a constraint? (need it in 5 min vs can wait an hour)
- Have you verified the audio quality is good enough for transcription?

**Recommended models by use case**:
- Draft/notes: `tiny` or `base` (fast, ~85-90% accuracy)
- General use: `small` (balanced, ~92-95% accuracy)
- Publication/subtitles: `medium` (high quality, ~96-98% accuracy)
- Professional/critical: `large` (best quality, ~98-99% accuracy)

### Sequential-Thinking (Complex Workflow Planning)
**Use when:**
- User has multi-step processing pipeline (e.g., "extract highlights, transcribe Q&A only, create subtitles, convert to webm")
- User needs to process different sections of video differently
- User wants to optimize processing order (e.g., should we extract audio first or transcribe directly?)
- Batch processing requires strategic planning

**Example trigger**: "Process this 2-hour lecture: create highlights reel, transcribe only the Q&A section, add subtitles, and convert to web format"

**Why**: Complex video workflows benefit from reasoning about optimal sequencing:
1. **Order optimization**: Should we extract audio first or work with video directly?
2. **Conditional branching**: If audio quality is poor, what preprocessing is needed?
3. **Resource planning**: How to batch 50 videos without overwhelming system?
4. **Quality gates**: When should we preview/validate before continuing pipeline?

---

## Instructions

This skill provides video processing utilities including audio extraction, format conversion, and audio transcription using FFmpeg and OpenAI's Whisper model.

### Prerequisites

**Required tools** (must be installed in your environment):
- **FFmpeg**: Multimedia framework for video/audio processing
  ```bash
  # macOS
  brew install ffmpeg

  # Ubuntu/Debian
  apt-get install ffmpeg

  # Verify installation
  ffmpeg -version
  ```

- **OpenAI Whisper**: Speech-to-text transcription model
  ```bash
  # Install via pip
  pip install -U openai-whisper

  # Verify installation
  whisper --help
  ```

**Python packages** (included in script via PEP 723):
- click (CLI framework)
- ffmpeg-python (Python wrapper for FFmpeg)

### Workflow

Use the `scripts/video_processor.py` script for all video processing tasks. The script provides a simple CLI with the following commands:

#### 1. **Extract Audio from Video**

Extract the audio track from a video file:

```bash
uv run .claude/skills/video-processor/scripts/video_processor.py extract-audio input.mp4 output.wav
```

Options:
- `--format`: Output audio format (default: wav). Supports: wav, mp3, aac, flac
- Output is suitable for transcription or standalone audio use

#### 2. **Convert Video to MP4**

Convert any video file to MP4 format:

```bash
uv run .claude/skills/video-processor/scripts/video_processor.py to-mp4 input.avi output.mp4
```

Options:
- `--codec`: Video codec (default: libx264). Common options: libx264, libx265, h264
- `--preset`: Encoding speed/quality preset (default: medium). Options: ultrafast, fast, medium, slow, veryslow

#### 3. **Convert Video to WebM**

Convert any video file to WebM format (web-optimized):

```bash
uv run .claude/skills/video-processor/scripts/video_processor.py to-webm input.mp4 output.webm
```

Options:
- `--codec`: Video codec (default: libvpx-vp9). Options: libvpx, libvpx-vp9
- WebM is optimized for web playback and streaming

#### 4. **Transcribe Audio with Whisper**

Transcribe audio or video files to text using OpenAI's Whisper model:

```bash
# Transcribe video file (audio will be extracted automatically)
uv run .claude/skills/video-processor/scripts/video_processor.py transcribe input.mp4 transcript.txt

# Transcribe audio file directly
uv run .claude/skills/video-processor/scripts/video_processor.py transcribe audio.wav transcript.txt
```

Options:
- `--model`: Whisper model size (default: base). Options:
  - `tiny`: Fastest, lowest accuracy (~1GB RAM)
  - `base`: Fast, good accuracy (~1GB RAM) **[DEFAULT]**
  - `small`: Balanced (~2GB RAM)
  - `medium`: High accuracy (~5GB RAM)
  - `large`: Best accuracy, slowest (~10GB RAM)
- `--language`: Language code (default: auto-detect). Examples: en, es, fr, de, zh
- `--format`: Output format (default: txt). Options: txt, srt, vtt, json

**Transcription workflow:**
1. If input is video, FFmpeg extracts audio to temporary WAV file
2. Whisper processes the audio file
3. Transcription is saved in requested format
4. Temporary files are cleaned up automatically

#### 5. **Combined Workflow Example**

Process a video end-to-end:

```bash
# 1. Extract audio for analysis
uv run .claude/skills/video-processor/scripts/video_processor.py extract-audio lecture.mp4 lecture.wav

# 2. Transcribe to SRT subtitles
uv run .claude/skills/video-processor/scripts/video_processor.py transcribe lecture.mp4 lecture.srt --format srt --model small

# 3. Convert to web format
uv run .claude/skills/video-processor/scripts/video_processor.py to-webm lecture.mp4 lecture.webm
```

### Key Technical Details

**FFmpeg and Whisper Integration:**
- FFmpeg doesn't transcribe audio itself - it prepares audio for external transcription
- The workflow is: Extract audio (FFmpeg) → Transcribe (Whisper) → Optional: Re-integrate with video
- FFmpeg can pipe audio directly to Whisper for real-time processing (advanced use case)

**Audio Format for Transcription:**
- Whisper works best with WAV or MP3 formats
- Sample rate: 16kHz is optimal (script handles conversion automatically)
- The script extracts audio with optimal settings for Whisper

**Output Formats:**
- **txt**: Plain text transcript
- **srt**: SubRip subtitle format (includes timestamps)
- **vtt**: WebVTT subtitle format (web standard)
- **json**: Detailed JSON with word-level timestamps

### Error Handling

The script includes comprehensive error handling:
- Validates input files exist
- Checks FFmpeg and Whisper are installed
- Provides clear error messages for missing dependencies
- Handles temporary file cleanup on errors

### Performance Tips

- Use `tiny` or `base` models for quick drafts
- Use `small` or `medium` for production transcriptions
- Use `large` only when maximum accuracy is required
- For long videos, consider extracting audio first, then transcribe in segments
- WebM conversion with VP9 takes longer but produces smaller files

## Examples

### Example 1: Quick Video to MP4 Conversion

User request:
```
I have an AVI file from my old camera. Can you convert it to MP4?
```

You would:
1. Use the to-mp4 command with default settings:
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py to-mp4 old_video.avi output.mp4
   ```
2. Confirm the conversion completed successfully
3. Inform the user about the output file location

### Example 2: Extract Audio and Transcribe

User request:
```
I recorded a lecture video and need a transcript. Can you extract the audio and transcribe it?
```

You would:
1. First extract the audio:
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py extract-audio lecture.mp4 lecture.wav
   ```
2. Then transcribe using the base model (good balance of speed/accuracy):
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe lecture.mp4 transcript.txt --model base
   ```
3. Share the transcript.txt file with the user

### Example 3: Create Web-Optimized Video with Subtitles

User request:
```
I need to put this video on my website with subtitles. Can you help?
```

You would:
1. Convert to WebM for web optimization:
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py to-webm presentation.mp4 presentation.webm
   ```
2. Generate SRT subtitle file:
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe presentation.mp4 subtitles.srt --format srt --model small
   ```
3. Inform user they now have:
   - presentation.webm (web-optimized video)
   - subtitles.srt (subtitle file for embedding)

### Example 4: High-Quality Transcription with Language Specification

User request:
```
I have a Spanish interview video that needs an accurate transcript for publication.
```

You would:
1. Use a larger model with language specified for best accuracy:
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe interview.mp4 transcript.txt --model medium --language es
   ```
2. Optionally create SRT for review:
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe interview.mp4 transcript.srt --format srt --model medium --language es
   ```
3. Review the transcript with the user and make any necessary corrections

### Example 5: Batch Processing Multiple Videos

User request:
```
I have a folder of training videos that all need to be converted to WebM and transcribed.
```

You would:
1. List all video files in the directory:
   ```bash
   ls training_videos/*.mp4
   ```
2. For each video file, run the conversion and transcription:
   ```bash
   # For each video: video1.mp4, video2.mp4, etc.
   uv run .claude/skills/video-processor/scripts/video_processor.py to-webm training_videos/video1.mp4 output/video1.webm
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe training_videos/video1.mp4 output/video1.txt --model base

   # Repeat for each file
   ```
3. Confirm all conversions and transcriptions completed
4. Provide summary of output files

## Summary

The video-processor skill provides a unified interface for common video processing tasks:
- **Audio extraction**: Extract audio tracks in various formats
- **Format conversion**: Convert to MP4 (universal) or WebM (web-optimized)
- **Transcription**: Speech-to-text with multiple output formats
- **Flexible**: CLI arguments for model selection, language, and output formats

All operations are handled through a single, well-documented script with sensible defaults and comprehensive error handling.
