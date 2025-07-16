
import gradio as gr
from chatBot__logic import bot_response

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("🤖 Jarvis2 - Powered Using BlenderBot")

    gr.Markdown("Talk to Meta's BlenderBot Model. Ask Questions or Just Chill(if it chills) ")

    with gr.Row():
        user_input = gr.Textbox(label="Your Message")
        output = gr.Textbox(label="Jarvis's Reply")

    submit_btn = gr.Button("Order Jarvis")
    submit_btn.click(fn=bot_response, inputs=user_input, outputs=output)

demo.launch(share=True)