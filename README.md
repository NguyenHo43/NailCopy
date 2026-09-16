# NailCopy

A CLI tool that generates marketing descriptions for nail salon services using the Claude API.

## Why I Built This

As a former nail technician, I noticed salons often struggle to write catchy captions for social media or price boards. NailCopy turns a plain service description into a ready-to-use marketing line.

## What It Does

Takes a description (e.g. "pastel pink ombre with rhinestone accents") and returns a short marketing sentence generated via Claude.

## Example

Enter nail service description: pastel pink ombre with rhinestone accents

--- Marketing description ---
Dreamy pastel pink ombre meets sparkle: elegant nails for effortless glam.

## Tech Stack

- Python
- Anthropic Claude API (claude-haiku-4-5-20251001)
- python-dotenv

## Setup

git clone https://github.com/NguyenHo43/NailCopy.git
cd NailCopy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Add your API key in a `.env` file:

ANTHROPIC_API_KEY=your_key_here

Run:

python nail_copy.py

## Limitations / Next Steps

- No output length validation yet
- Single input only — batch processing could be added
- No automated tests yet

## About

Built by [Nguyen Ho](https://github.com/NguyenHo43) — CS student at University of Oklahoma, former nail technician.
