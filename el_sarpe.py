import time
import os

def mostrar_letras():
    os.system('cls' if os.name == 'nt' else 'clear')

    blanco = "\033[37m"
    amarillo = "\033[33m"
    celeste = "\033[36m"
    morado = "\033[35m"
    verde = "\033[32m"
    reset = "\033[0m" 

    colores = [blanco, amarillo, celeste, morado, verde]

    letras = [
        
        ("Solo quiero el sarpe", 0.05, "🎶", 2.1),
        ("De mi parte, quiero besarte", 0.04, "💋", 2.1),
        ("Vamos pa' mi chante", 0.05, "🏠", 2.1), 
        ("Quiero el sarpe", 0.05, "🎵", 2.1),
        ("De mi parte, quiero besarte", 0.04, "😘", 2.1),
        ("Vamos pa' mi chante", 0.05, "🚶‍♂️", 2.5), 

      
        ("Eh, eh, eh, ieh", 0.07, "🎤", 2.5),
        ("Eh, eh, vamos pa' mi chante, ieh", 0.06, "🕺", 2.5),
        ("Eh, eh, eh, ieh", 0.07, "🔊", 2.5),
        ("Eh, eh, eh", 0.08, "🔥", 6.0), 

       
        ("Entonces qué", 0.06, "🤨", 1.8),
        ("Con to'a confianza, se que me transa", 0.04, "🤝", 2.0),
        ("Tengo coctel pa' la panza", 0.04, "🍸", 2.0),
        ("I finna heal out de bronze and de ganja", 0.04, "🌿", 2.0),
        ("Pero depende de la birra que me lanza", 0.04, "🍺", 2.0),
        ("Esa para mí no es mala canza (no way)", 0.04, "🙅‍♂️", 2.0),
        ("Pero desde mi infancia", 0.05, "👶", 2.0),
        ("Estaba esperando a alguien como teus con", 0.04, "⏳", 2.0),
        ("Desesperanza", 0.07, "😩", 2.0),
        ("Un momento si soy muy directo, lo siento", 0.04, "✋", 2.0),
        ("Ese es mi estilo y no la rento", 0.04, "😎", 2.0),
        ("Pero atento, yo no te miento", 0.04, "👀", 2.0),
        ("Me tiene como loco ese movimiento", 0.04, "🌪️", 2.0),
        ("Un minuto pero yo no soy bruto", 0.04, "🧠", 2.0),
        ("Es que es tan chica y yo no discuto", 0.04, "🤐", 2.0),
        ("Ojalá que feeling es mutuo", 0.04, "✨", 2.0),
        ("Estando contigo yo disfruto", 0.05, "🎉", 2.0)
    ]

    for i, (linea, velocidad, emoji, tiempo_total) in enumerate(letras):
        inicio = time.time()
        
        color = colores[i % len(colores)]
        print(color, end="") 
        
        for caracter in linea:
            print(caracter, end="", flush=True)
            time.sleep(velocidad) 
            
        print(f" {emoji}{reset}")
        
        tiempo_tomado = time.time() - inicio
        tiempo_restante = tiempo_total - tiempo_tomado
        
        if tiempo_restante > 0:
            time.sleep(tiempo_restante)

if __name__ == "__main__":
    mostrar_letras()