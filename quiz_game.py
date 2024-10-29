
import random

questions = [
    {"question": "¿Cuál es la capital de Francia?", "answer": "paris"},
    {"question": "¿Cuál es el resultado de 5 + 7?", "answer": "12"},
    {"question": "¿Quién escribió 'Cien años de soledad'?", "answer": "gabriel garcia marquez"},
    {"question": "¿Cuál es el animal más rápido del mundo?", "answer": "guepardo"},
    {"question": "¿En qué año llegó el hombre a la luna?", "answer": "1969"}
]

def quiz_game():
    print("¡Bienvenidos al Juego de Preguntas y Respuestas!")
    score = 0
    random.shuffle(questions)

    for q in questions:
        user_answer = input(f"{q['question']} ").strip().lower()
        if user_answer == q['answer']:
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {q['answer']}.")

    print(f"\nJuego terminado. Obtuviste {score}/{len(questions)} puntos.")

quiz_game()
    