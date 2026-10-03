import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import ollama as ol
from Producto import Producto

# Lista con productos iniciales de repuestos 
productos = [
    Producto("Filtro de Aceite", "Filtros", 15, 8.50, 5),
    Producto("Pastillas de Freno", "Frenos", 3, 35.00, 6),
    Producto("Bujía Iridium", "Motor", 24, 12.00, 10),
    Producto("Amortiguador Delantero", "Suspensión", 2, 85.00, 4),
    Producto("Aceite de Motor 5W-30", "Fluidos", 18, 28.00, 5),
    Producto("Disco de Freno", "Frenos", 1, 45.00, 3)
]

def obtener_dataframe():
    """Convierte la lista de objetos Producto a un DataFrame de Pandas."""
    datos = [p.__dict__ for p in productos]
    return pd.DataFrame(datos)

def agregar_producto(nombre, categoria, cantidad, precio, stock_minimo):
    """Agrega un nuevo repuesto al inventario y actualiza la tabla y gráfico."""
    nuevo_prod = Producto(
        nombre, 
        categoria, 
        int(cantidad), 
        float(precio), 
        int(stock_minimo)
    )
    productos.append(nuevo_prod)
    
    df = obtener_dataframe()
    fig = crear_grafico_inventario()
    
    return df, fig

def crear_grafico_inventario():
    """Genera un gráfico de barras comparando la Cantidad actual vs Stock Mínimo."""
    df = obtener_dataframe()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    
    if not df.empty:
        x = df["nombre"]
        ax.bar(x, df["cantidad"], label="Cantidad Actual", color="skyblue")
        ax.step(x, df["stock_minimo"], label="Stock Mínimo", color="red", where="mid", linestyle="--")
        
        ax.set_xlabel("Repuesto / Parte")
        ax.set_ylabel("Unidades")
        ax.set_title("Nivel de Stock de Repuestos")
        ax.set_xticklabels(x, rotation=30, ha="right")
        ax.legend()
        plt.tight_layout()
        
    return fig

def consultar_asistente_inventario(pregunta):
    """Consulta a Ollama sobre el estado del inventario de repuestos."""
    yield "🤖 Analizando el inventario de repuestos con la IA..."
    
    df = obtener_dataframe()
    
    # Identificar productos con stock bajo para alimentar el contexto de la IA
    productos_bajo_stock = df[df["cantidad"] <= df["stock_minimo"]]
    
    contexto = f"""
    Eres un Asistente Técnico y Administrador de Inventario especializado en repuestos automotrices.
    
    REGLAS OBLIGATORIAS:
    1. Responde preguntas únicamente basadas en los datos del inventario adjunto.
    2. Si el usuario pregunta qué piezas reabastecer o comprar urgentes, prioriza las que estén por debajo o igual a su 'stock_minimo'.
    3. Si la pregunta no se relaciona con piezas de auto o el inventario, responde: "Solo puedo ayudarte con la gestión de este inventario de repuestos."
    4. Sé conciso y profesional.

    INVENTARIO ACTUAL EN SISTEMA:
    {df.to_string(index=False)}

    PRODUCTOS CON STOCK CRÍTICO (Cantidad <= Stock Mínimo):
    {productos_bajo_stock.to_string(index=False) if not productos_bajo_stock.empty else "Ninguno, todo está con suficiente stock."}
    """
    
    respuesta = ol.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": contexto},
            {"role": "user", "content": pregunta}
        ]
    )
    
    yield respuesta["message"]["content"]

# --- INTERFAZ GRÁFICA CON GRADIO (gr.Blocks) ---
with gr.Blocks(title="Inventario de Repuestos Automotrices") as app:
    
    gr.Markdown("<h1 style='text-align: center;'>🏎️ Sistema de Control de Repuestos Automotrices</h1>")
    
    # Fila 1: Formulario de ingreso y Tabla de Inventario
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Registrar Nuevo Repuesto")
            nombre_in = gr.Textbox(label="Nombre del Repuesto", placeholder="Ej. Filtro de Aire")
            categoria_in = gr.Dropdown(
                choices=["Motor", "Frenos", "Suspensión", "Filtros", "Fluidos", "Eléctrico"],
                label="Categoría",
                value="Motor"
            )
            cantidad_in = gr.Number(label="Cantidad en Stock", value=1)
            precio_in = gr.Number(label="Precio ($)", value=0.0)
            stock_min_in = gr.Number(label="Stock Mínimo Requerido", value=5)
            
            btn_agregar = gr.Button("Agregar Repuesto", variant="primary")
            
        with gr.Column():
            gr.Markdown("## Inventario Actual")
            tabla_inventario = gr.DataFrame(value=obtener_dataframe())

    # Fila 2: Gráfico de Existencias y Consulta con IA
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Visualización de Existencias vs Stock Mínimo")
            plot_inventario = gr.Plot(value=crear_grafico_inventario())
            
        with gr.Column():
            gr.Markdown("## 🤖 Asistente Virtual de Repuestos")
            pregunta_in = gr.Textbox(
                label="Consulta a la IA sobre repuestos o pedidos urgentes",
                placeholder="Ejemplo: ¿Qué repuestos necesito pedir urgente al proveedor?"
            )
            btn_ia = gr.Button("Consultar Asistente", variant="primary")
            respuesta_out = gr.Markdown(label="Respuesta")

    # Vinculación de Eventos
    btn_agregar.click(
        fn=agregar_producto,
        inputs=[nombre_in, categoria_in, cantidad_in, precio_in, stock_min_in],
        outputs=[tabla_inventario, plot_inventario]
    )
    
    btn_ia.click(
        fn=consultar_asistente_inventario,
        inputs=pregunta_in,
        outputs=respuesta_out,
        show_progress="full"
    )

if __name__ == "__main__":
    app.launch()