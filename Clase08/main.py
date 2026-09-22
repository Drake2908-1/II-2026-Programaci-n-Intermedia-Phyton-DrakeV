import ollama as ol

respuesta = ol.chat(
    model="llama3.2", 
    messages=[
        {
            "role": "system", 
            "content": "Eres un costarricense ."
        },
        {
            "role": "user", 
            "content": "Hola, ¿cómo estás?"
        }]
)
print(respuesta["message"]["content"])