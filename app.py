import subprocess
import gradio as gr

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return result.stdout + "\n" + result.stderr
    except Exception as e:
        return str(e)

with gr.Blocks(title="Linux Terminal") as demo:
    gr.Markdown("# My Linux Terminal - chinkscaxs")
    cmd = gr.Textbox(label="Ketik perintah linux disini", placeholder="contoh: ls -la atau bash script.sh")
    output = gr.Textbox(label="Hasil", lines=15)
    btn = gr.Button("JALANKAN")
    btn.click(run_command, inputs=cmd, outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)
