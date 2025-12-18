print("=== BEM-VINDO AO QUIZ DO CONHECIMENTO ===")

perguntas = [
    "Qual o comando é usado para exibir algo na tela?",
    "Qual a estrutura usada para repetir um bloco de código várias vezes?",
    "Qual a palavra usada para criar uma condição?",
    "Qual função retorna o tipo de um valor?",
    "O que significa '==' em Python?"
]

respostas = [
    "print",
    "for",
    "if",
    "type",
    "comparação"
]

continuar = "s"

while continuar == "s":
    acertos = 0

    for i in range(len(perguntas)):
        print(f"\nPergunta {i+1}: {perguntas[i]}")
        resposta_usuario = input("Sua resposta: ").lower().strip()

        if resposta_usuario == respostas[i]:
            print("✅ Você acertou a resposta, muito bem!")
            acertos += 1

        elif resposta_usuario == "":
            print("⚠️ Você não digitou nada!")

        else:
            print(f"❌ Errado, a resposta era: {respostas[i]}")

    print("\n=== RESULTADO FINAL ===")
    print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")

    if acertos == len(perguntas):
        print("🏆 Impressionante, você gabaritou!")
    elif acertos >= 3:
        print("💪 Bom trabalho! Continue melhorando.")
    else:
        print("😉 Boa tentativa, tente novamente.")

    continuar = input("\nVocê quer continuar? (s/n): ").lower().strip()

print("\nObrigado por jogar o QUIZ DO CONHECIMENTO! 🧠")
