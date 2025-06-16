# 🔄 Auto File Organizer

A Python script that automatically organizes your downloaded files (PDFs, images, documents, sounds, PPTs) into categorized folders using the `watchdog` module.
It monitors the download folder and moves files in real-time based on their type.

## 📂 How It Works

- Listens to changes in your Downloads directory
- When a new file is added:
  - It checks its extension and size
  - If it matches a known type (PDF, image, etc.), it moves the file to the correct folder

## ⚙️ Features

- Organizes files in real time
- Supports `.pdf`, `.docx`, `.jpg`, `.mp3`, `.pptx`, and more
- Ignores large files (>100MB)
- Uses `.env` file to configure paths

## 🛠 Requirements

- Python 3.8+
- `watchdog`
- `python-dotenv`

Install dependencies:

```bash
pip install watchdog python-dotenv
