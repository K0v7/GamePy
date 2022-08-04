from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

    def jogar(pontos: int) -> None:
        dificuldade: int = int(input('Informe o Nível de Dficuldade Desejado [1, 2, 3 ou 4]'))

        calc: Calcular = Calcular(dificuldade)

        print('Informe o Resultado para a seguinte operação')
        calc.mostrar_operacao()

        resultado: int = int(input())

        if calc.checar_resultado(resultado):
            pontos =+ 1
            print(f'Você Tem {pontos} pontos(s).')

            continuar: int = int(input('Deseja continuar no jogo ? [1 - sim, 0 - não]'))

            if continuar:
                jogar(pontos)
            else:
                print(f'Você finalizou com {pontos} ponto(s). ')
                print('Até a Próxima')


    if __name__ == '___main_':
        main()