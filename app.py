import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys
import cv2
import os

# Load the BLIP processor and model for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Initialize the AI video generator pipeline
p = pipeline('text-to-video-synthesis', 'damo/text-to-video-synthesis')

# Function to generate caption from a video
def generate_caption(video_path):
    cap = cv2.VideoCapture(video_path)
    _, frame = cap.read()  # Extract the first frame (simplified)
    cap.release()

    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    inputs = processor(images=frame_rgb, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

# Function to generate AI video based on caption
def generate_ai_video(caption, output_path):
    try:
        test_text = {'text': caption}
        output = p(test_text, output_video=output_path)
        ai_video_path = output[OutputKeys.OUTPUT_VIDEO]
        return ai_video_path
    except Exception as e:
        return None, f"Error generating AI video: {e}"

# Main function for Gradio interface
def gradio_app(video_file):
    if not video_file:
        return None, None, "No video file provided."

    # Generate caption for the input video
    caption = generate_caption(video_file.name)

    # Generate AI video based on the caption
    output_path = f"/content/{os.path.basename(video_file.name).replace('.mp4', '_generated.mp4')}"
    ai_video_path = generate_ai_video(caption, output_path)

    # Check if AI video generation was successful
    if not os.path.exists(ai_video_path):
        return video_file.name, None, f"Error: AI video not generated. Caption: {caption}"

    return video_file.name, ai_video_path, caption

# Gradio interface
interface = gr.Interface(
    fn=gradio_app,
    inputs=gr.File(type="filepath"),  # Single video upload
    outputs=[
        gr.Video(label="Input Video"),  # Display input video
        gr.Video(label="AI-Generated Video"),  # Display AI-generated video
        gr.Textbox(label="Generated Caption"),  # Display caption
    ],
    title="Video Captioning and AI Video Generation",
    description="Upload a video file to generate a caption and an AI-generated video."
)

# Launch the interface in Colab
interface.launch(debug=True, share=True)  # Set share=True for external access if needed
