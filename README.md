# Meme Generator

A project to generate memes from the CLI and a web application using flask

## Overview

## Installation Instructions

Create a python virtual environment
Install the project dependencies using: pip install -r requirements.py

## meme generator CLI

Run python meme.py from the root of the application  on the terminal
to start the CLI application. Use python meme.py --help to display
additional help information.

usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

meme generator

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      path to image file
  --body BODY      meme
  --author AUTHOR  meme author

## flask applciation

Run the following commands on the terminal:
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload

copy the application url into your browser of choice
to run the application