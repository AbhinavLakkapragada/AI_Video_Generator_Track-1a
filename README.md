# Video Captioning and AI Video Generation

A Gradio-based application that combines video captioning and AI video generation. This project processes an input video, generates a descriptive caption using the BLIP model, and creates a new AI video based on the caption using the ModelScope text-to-video synthesis pipeline.

## Features

- Upload a video file for processing.
- Extract a meaningful caption from the input video.
- Generate an AI-created video based on the caption.
- View the input video, AI-generated video, and caption side-by-side in a user-friendly interface.

## Platform Used: Google Colab with T4 GPU

This application requires significant computational resources, as the text-to-video-synthesis model cannot run on standard laptop CPUs. It has been tested and verified on Google Colab using the T4 GPU runtime. To replicate the results, ensure the runtime is set to GPU under Runtime > Change runtime type.

## Models Used

This project utilizes the following state-of-the-art models for video captioning and AI-generated video synthesis:

1. BLIP Image Captioning Model:

- Description:
    BLIP (Bootstrapping Language-Image Pretraining) is a model designed for tasks like image captioning and visual question answering. It generates natural language descriptions of images with high accuracy. In this project, BLIP is used to generate a textual caption from the first frame of the uploaded video.
- Model Details:
    Name: Salesforce/blip-image-captioning-base
    Framework: Hugging Face Transformers
- Link: https://huggingface.co/Salesforce/blip-image-captioning-large

2. Text-to-Video Synthesis Model:

- Description:
    This model from modelscope takes text descriptions as input and generates corresponding video sequences. It is a cutting-edge model that leverages multimodal learning for generating synthetic videos from textual prompts. In this project, it generates an AI video based on the caption produced by the BLIP model.
- Model Details:
    Name: damo/text-to-video-synthesis
    Framework: ModelScope
- Link: https://huggingface.co/ali-vilab/modelscope-damo-text-to-video-synthesis


## Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/AbhinavLakkapragada/AI_Video_Generator_Track-1a.git
cd AI_Video_Generator_Track-1a

```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

or install them manually if the above is not working:

```bash
pip install gradio
```
```bash
pip install modelscope==1.4.2
```
```bash
pip install pytorch-lightning
```
```bash
pip install open_clip_torch==2.24.0
```

3. Run the application:

```bash
python app.py
```

## How to Use

1. Launch the application and upload a video file (e.g., .mp4 format).

2. The app will process the video to:
- Generate a caption.
- Create an AI video based on the caption.

3. View the results in the interface:
- Left: Input video.
- Right: AI-generated video.
- Below: Caption displayed in a text box.

## Inputs

The input videos are from the sample synthetic videos.

## Expected Outputs

- Input Video: The original video uploaded by the user.
- Generated Caption: A descriptive textual summary of the input video.
- Generated Video: An AI-rendered video created based on the caption.

## Demo

- Link: https://youtu.be/PaYxaAB5FWA
