import gradio as gr
import ollama as ol

def recomendar_libros(tema: str) -> str:
    """
    Recibe el tema o género de interés del cliente y consulta a Ollama
    para obtener recomendaciones de lectura según las reglas definidas.
    """
    respuesta = ol.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente virtual de una librería. "
                    "Regla 1: Debes responder siempre en idioma español. "
                    "Regla 2: Recomienda únicamente un máximo de 3 libros sobre el tema solicitado, "
                    "incluyendo el título, autor y una breve razón de por qué leerlo."
                )
            },
            {
                "role": "user",
                "content": f"Recomiéndame libros sobre el siguiente tema: {tema}"
            }
        ]
    )
    
    # Retorna únicamente el texto de la respuesta generada por el modelo
    return respuesta["message"]["content"]


# ============================================================
# Parte C - Interfaz web con Gradio (15 puntos)
# ============================================================
with gr.Blocks() as interfaz:
    gr.Markdown("<h1 style='text-align: center;'>📚 Asistente Virtual de Librería</h1>")
    
    # Campo de texto donde el cliente escribe el tema de su interés
    tema_input = gr.Textbox(
        label="Tema o Género de Interés",
        placeholder="Ej. Misterio, Historia, Ciencia Ficción..."
    )
    
    # Botón con el texto "Recomendar"
    boton_recomendar = gr.Button("Recomendar", variant="primary")
    
    # Campo de texto donde se muestra la recomendación
    recomendacion_output = gr.Textbox(
        label="Recomendaciones de Lectura",
        lines=8
    )
    
    # Vinculación del evento click del botón
    boton_recomendar.click(
        fn=recomendar_libros,
        inputs=tema_input,
        outputs=recomendacion_output
    )

# Iniciar la interfaz web
if __name__ == "__main__":
    interfaz.launch()