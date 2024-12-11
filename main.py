import random
from colorama import Fore, Style, init

# Inicializa o colorama para exibir cores no terminal
init(autoreset=True)

def exibir_titulo():
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.BLUE + Style.BRIGHT + "       Bem-vindo ao Jogo da Forca!")
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)

def exibir_status(letras_descobertas, tentativas, letras_erradas):
    print(Fore.CYAN + "\nPalavra: " + Fore.WHITE + " ".join(letras_descobertas))
    print(Fore.BLUE + f"Tentativas restantes: {Fore.WHITE}{tentativas}")
    if letras_erradas:
        print(Fore.RED + "Letras erradas: " + Fore.WHITE + ", ".join(letras_erradas))
    print(Fore.CYAN + "-" * 40)

def jogar_forca():
    exibir_titulo()

    # Lista de palavras
    palavras = ['python', 'programador', 'computador', 'algoritmo', 'desenvolvedor']
    palavra_secreta = random.choice(palavras).lower()
    letras_descobertas = ['_' for _ in palavra_secreta]
    tentativas = 6
    letras_erradas = []

    while tentativas > 0 and '_' in letras_descobertas:
        exibir_status(letras_descobertas, tentativas, letras_erradas)
        
        letra = input(Fore.CYAN + "Digite uma letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print(Fore.RED + "Digite apenas uma letra válida.")
            continue
        
        if letra in letras_descobertas or letra in letras_erradas:
            print(Fore.YELLOW + "Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            print(Fore.GREEN + "Boa! A letra está na palavra.")
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            print(Fore.RED + "Ops! Essa letra não está na palavra.")
            letras_erradas.append(letra)
            tentativas -= 1

    exibir_status(letras_descobertas, tentativas, letras_erradas)

    if '_' not in letras_descobertas:
        print(Fore.GREEN + Style.BRIGHT + "\nParabéns! Você venceu!")
        print(Fore.CYAN + "A palavra era: " + Fore.WHITE + palavra_secreta)
    else:
        print(Fore.RED + Style.BRIGHT + "\nQue pena! Você perdeu!")
        print(Fore.CYAN + "A palavra era: " + Fore.WHITE + palavra_secreta)

# Executa o jogo
if __name__ == "__main__":
    jogar_forca()