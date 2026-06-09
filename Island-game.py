import random
from time import sleep
#Apresentação/Introdução
print(10 * '\033[1;33m<', 'O Despertar na Ilha', 10 * '>')
print('''\033[0;0mVocê acorda em uma ilha deserta após um naufrágio.
O sol quente bate em sua pele, e o som das ondas quebra o silêncio.
Sua última lembrança é do barco afundando durante uma tempestade.
Agora, você precisa tomar decisões para garantir sua sobrevivência.\n''')

sleep(5)

#sistema de enrgia:
print(40 * '\033[1;33m=\033[0;0m ')
energia = 100
print('Você vai começar com 100 de energia\n'
      'A cada escolha sua energia pode subir ou diminuir')
print(40 * '\033[1;33m=\033[0;0m ')

def eng():
    if energia >= 70:
        print(f'\033[1;32m Você ainda tem {energia}⚡ \033[0;0m\n')
    elif energia < 70 and energia >= 30:
        print(f'\033[1;33m Você ainda tem {energia}⚡ \033[0;0m\n')
    elif energia < 25:
        print(f'\033[1;31m Você ainda tem {energia}⚡ \033[0;0m\n')

print()
sleep (3)

#Escolha 1:
print('\033[1;32m Iniciando jogo... \033[0;0m ')
sleep(2)

print('Ao acordar na praia você olha ao seu redor e enxerga uma floresta,\n'
      'o que você decide fazer?\n'
      '(1) Explorar a floresta em busca de recursos\n'
      '(2) Caminhar pela praia e procurar sinais de vida.')

esc1 = int(input('Faça sua escolha:'))
while esc1 != 1 and esc1 != 2:
    print('\033[1;31mValor inválido tente novamente!\033[0;0m ')
    esc1 = int(input('Faça sua escolha:'))

eg = random.randint(20,40)
energia = energia - eg
print(f'\033[1;31m Voçê acabou gastando {eg}⚡ \033[0;0m ')
eng()
sleep(3)

#Escolha 2a(floresta)
if esc1 == 1:
    print(40 * '\033[1;33m=\033[0;0m')
    print('Explorando a Floresta:')
    print('Você entra na floresta e logo encontra um pequeno rio de água cristalina.\n'
          'A sombra das árvores oferece um alívio do calor intenso,\n'
          'Você decide:')

    print('(1)Beber água do rio\n'
          '(2)Procura outra fonte de água')
    esc2a = int(input('Faça sua escolha:'))

    while esc2a != 1 and esc2a != 2:
        print('\033[1;31mValor inválido tente novamente!\033[0;0m ')
        esc2a = int(input('Faça sua escolha:'))
    if esc2a == 1:
        eg = random.randint(15,35)
        energia = energia - eg
        print('A água pode estar contaminada e você começa a se sentir mal')
        print(f'\033[1;31m Você perdeu {eg}⚡')
        eng()
        sleep(3)

        print('Humm, voce começou a passar mal, o que deseja fazer?')
        print('(1)Beber mais a água do rio\n'
              '(2) Procurar uma fonte de água mais segura')
        esc3a = int(input('Faça sua escolha:'))

        if esc3a == 1:
            while esc3a == 1:
                eg = random.randint(15,35)
                energia = energia - eg
                print(f'\033[1;31m Você perdeu {eg}⚡')
                if energia <= 0:
                    print('\033[1;31m Você perdeu!\033[0;0m ')
                    exit()
                else:
                    eng()
                    esc3a = int(input('Humm, voce começou a passar mal, o que deseja fazer?\n'
                                      '(1)Beber mais a água do rio\n'
                                      '(2) Procurar uma fonte de água mais segura\n'
                                      'Faça sua escolha:'))
                    if esc3a == 2:
                        egan = random.randint(5, 15)
                        energia = energia + egan
                        print('Você encontra um coqueiro e consegue beber água de coco.')
                        print(f'\033[1;32m Você ganhou {egan}⚡')
                        eng()
                        sleep(3)

        elif esc3a == 2:
            egan = random.randint(5,15)
            energia = energia + egan
            print('Você encontra um coqueiro e consegue beber água de coco.')
            print(f'\033[1;32m Você ganhou {egan}⚡')
            eng()
            sleep(3)

    elif esc2a == 2:
        egan = random.randint(5,15)
        energia = energia + egan
        print('Você encontra um coqueiro e consegue beber água de coco.')
        print(f'\033[1;32m Você ganhou {egan}⚡')
        eng()
        sleep(3)

#Escolha 2b(praia):
elif esc1 == 2:
    print(40 * '\033[1;33m=\033[0;0m')
    print('Caminhando pela Praia:')
    print('Você decide caminhar pela praia, sentindo o calor do sol e a areia quente sob seus pés.\n'
          'Você também começa a sentir fome e cansaço, qual você escolhe:')
    print('(1) Caçar ou Pescar\n'
          '(2) Procurar Frutas')

    esc2b = int(input('Faça sua escolha:'))
    while esc2b !=1 and esc2b !=2:
        print('\033[1;31m Valor inválido tente novamente!\033[0;0m ')
        escb2 = int(input('Faça sua escolha:'))

    if esc2b == 1:
        eg = random.randint(15,35)
        energia = energia - eg
        print('Você não consegue coletar nada de proteína.')
        print(f'\033[1;31mVocê acabou gastando {eg}⚡\033[0;0m')
        eng()
        sleep(3)
    elif esc2b == 2:
        egan = random.randint(15,25)
        energia = energia + egan
        print('Você encontra frutas e se recupera')
        print(f'\033[1;32m Você ganhou {egan}⚡\033[0;0m ')
        eng()
        sleep(3)

#Escolha 3(noite):
print(40 * '\033[1;33m=\033[0;0m')
print('A noite chega:')
print('O sol começa a se pôr, e a temperatura cai rapidamente.\n'
      'O vento aumenta, e você sabe que precisa se preparar para a noite.\n'
      'Após algum tempo, você encontra destroços do barco, incluindo madeira, cordas e pedaços de tecido.\n'
      'O que você decide fazer?')

esc3 = int(input(('(1) Construir um abrigo\n'
                  '(2) Acender uma fogueira\n'
                  'Faça sua escolha:')))
while esc3 != 1 and esc3 != 2:
    print('\033[1;31m Valor inválido tente novamente! \033[0;0m')
    esc3 = int(input('Faça sua escolha:'))

if esc3 == 1:
    eg = random.randint(15,30)
    energia = energia - eg
    print(f'\033[1;31mVocê gastou {eg}⚡ para construir o abrigo.')
    eng()
    print()
    print('Pela manhã, pescadores da ilha o encontram e decidem ajudá-lo!')
elif esc3 == 2:
    eg = random.randint(5,15)
    energia = energia - eg
    print(f'\033[1;31mVocê gastou {eg}⚡ para acender a fogueira')
    eng()
    print()
    print('Um navio distante vê a fumaça e envia uma equipe de resgate rapidamente!')
    sleep(2)

#Desfecho:
if energia >= 70:
    print('\033[1;32mO resgate chega e você está tão bem que dá até para dar autógrafos para os socorristas.\n'
          'Você foi resgatado, e até parece que esteve em um spa por dias!')
elif energia >= 30 and energia < 70:
    print('\033[1;33mO resgate chega, mas você está tão fraco que mal consegue fazer uma piada\n'
          'Você sobreviveu, mas está mais parecendo um zumbi do que um herói!')
elif energia < 30:
    print('\033[1;33mO resgate chega, mas ele mal consegue levantar e até acha que o socorro é só mais um pesadelo.\n'
          'Você foi resgatado, mas vai precisar de muitos cafés para voltar à vida normal!')
