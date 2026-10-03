import gradio as gr
import ollama as ol


def tipo_de_videojuego (tipo:str) -> str:
    """
    Recibe el tema o género de interés del cliente y consulta a Ollama
    para obtener recomendaciones de videojuegos según las reglas definidas.
    """
    respuesta = ol.chat(
        model = "llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente de una tienda de videojuegos."
                    "Solo puedes responder dudas sobre videojuegos."
                    "Solo puedes responder en español."
                )
            },
            {
                "role": "user",
                "content": f"Recomiendame videojuegos sobre el siguiente tipo: {tipo}"
             }
        ]
    )
    return respuesta["message"]["content"] 

with gr.Blocks() as interfaz:
    
    tipo = gr.Textbox(
        label="Ingrese el genero de videojuego de su interes: ", lines=10)
    
    boton_recomendar = gr.Button("Recomendar", variant="primary")

    recomendacion_output = gr.Textbox(label="Recomendaciones de videojuegos ", lines=10)
   
    boton_recomendar.click(
        fn=tipo_de_videojuego,
        inputs=tipo,
        outputs=recomendacion_output
    ) 

interfaz.launch()