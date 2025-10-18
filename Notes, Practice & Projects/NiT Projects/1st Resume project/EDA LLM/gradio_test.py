import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()

# path="D:\NareshIT_PrakashSenapati\My Projects\Data\titanic_ dataset_final.csv"