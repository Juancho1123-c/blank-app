import random
import streamlit as st
import time

# Configuración de las luces y modos
LUZ_TOTAL = 10  # Número de luces
COLORES = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Violeta", "Cyan", "Magenta", "Blanco", "Negro"]
MODOS = ['Clásico', 'Desafío', 'Competitivo']

def generar_secuencia(largo):
    """Genera una secuencia de colores aleatorios."""
    return [random.choice(COLORES) for _ in range(largo)]

def mostrar_secuencia(secuencia):
    """Muestra la secuencia de colores uno por uno en la interfaz de Streamlit."""
    st.write("Secuencia:")
    for color in secuencia:
        st.markdown(f"<span style='color:{color.lower()}; font-size:30px;'>{color}</span>", unsafe_allow_html=True)
        time.sleep(0.5)  # Pausa para mostrar cada color
    st.write("\n" + "-" * 20)

def obtener_intentos(largo):
    """Obtiene los intentos del jugador en forma de lista de colores."""
    intentos = []
    st.write("Introduce tu secuencia haciendo clic en los colores:")
    for i in range(largo):
        color = st.selectbox(f"Color {i + 1}", COLORES, key=i)
        intentos.append(color)
    return intentos

def verificar_secuencia(secuencia, intentos):
    """Verifica si la secuencia del jugador es correcta."""
    return secuencia == intentos

def jugar_clasico():
    """Modo Clásico: el jugador sigue una secuencia fija."""
    largo = 3  # Comienza con una secuencia de 3
    while True:
        secuencia = generar_secuencia(largo)
        mostrar_secuencia(secuencia)
        intentos = obtener_intentos(largo)
        
        if verificar_secuencia(secuencia, intentos):
            st.success("¡Correcto! La secuencia se alarga.")
            largo += 1  # La secuencia crece
        else:
            st.error("¡Fallaste! Fin del juego.")
            break

def jugar_desafio():
    """Modo Desafío: la secuencia crece con cada acierto."""
    largo = 1  # Inicia con una secuencia de 1
    while True:
        secuencia = generar_secuencia(largo)
        mostrar_secuencia(secuencia)
        intentos = obtener_intentos(largo)
        
        if verificar_secuencia(secuencia, intentos):
            st.success("¡Correcto! Aumenta la dificultad.")
            largo += 1  # La secuencia crece en dificultad
        else:
            st.error("¡Fallaste! Fin del juego en modo desafío.")
            break

def jugar_competitivo():
    """Modo Competitivo: dos jugadores se alternan turnos en la misma secuencia."""
    largo = 3  # Comienza con una secuencia de 3
    turno = 1  # Jugador 1 inicia
    
    while True:
        st.write(f"\nTurno del Jugador {turno}")
        secuencia = generar_secuencia(largo)
        mostrar_secuencia(secuencia)
        intentos = obtener_intentos(largo)
        
        if verificar_secuencia(secuencia, intentos):
            st.success("¡Correcto!")
            largo += 1  # La secuencia crece
            turno = 2 if turno == 1 else 1  # Cambia de jugador
        else:
            st.error(f"Jugador {turno} falló. Jugador {3 - turno} gana el juego.")
            break

def main():
    st.title("Bienvenido a 'Simón Dice'")

    modo = st.selectbox("Selecciona un modo de juego:", MODOS)

    if st.button("Iniciar Juego"):
        if modo == 'Clásico':
            jugar_clasico()
        elif modo == 'Desafío':
            jugar_desafio()
        elif modo == 'Competitivo':
            jugar_competitivo()

if __name__ == "__main__":
    main()
