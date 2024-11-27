# Video Captioning and AI Video Generation

## Project Description

A Gradio-based application that combines video captioning and AI video generation. This project processes an input video, generates a descriptive caption using the BLIP model, and creates a new AI video based on the caption using the ModelScope text-to-video synthesis pipeline.

## Features

-Upload a video file for processing.
-Extract a meaningful caption from the input video.
-Generate an AI-created video based on the caption.
-View the input video, AI-generated video, and caption side-by-side in a user-friendly interface.

## Setup Instructions

1. Clone this repository:
   '''bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>

3. Install the required dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

5. Access the Gradio interface through the provided URL in your terminal.

## How to Use

1. Launch the application and upload a video file (e.g., .mp4 format).
2. The app will process the video to:
    -Generate a caption.
    -Create an AI video based on the caption.
3. View the results in the interface:
    -Left: Input video.
    -Right: AI-generated video.
    -Below: Caption displayed in a text box.

## Expected Outputs

-Input Video: The original video uploaded by the user.
-Generated Video: An AI-rendered video created based on the caption.
-Generated Caption: A descriptive textual summary of the input video.
