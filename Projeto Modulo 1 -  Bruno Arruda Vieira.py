# RECURSOS USADOS:

# Variáveis <-
# Estruturas condicionais <- 
# Estruturas de repetição <-
# Operadores lógicos <-
# Funções <-
# Formatação de String <-

# ====================================== JOGO DE JORGINHO =========================================================


def jogoJorginho():
  print('Você escolheu o Jorginho da Serraria. Jorginho sente algo quente em seu rosto e ao abrir os olhos percebe que estava dormindo na calçada e o sol o acordou.')
  opcao = input('''Você se levanta e decide voltar para o bar ou ir para casa?
  1 - Voltar para o bar
  2 - Ir para casa
  ''')
  condicao = True
  while condicao:
    if(opcao == '1'):
      condicao = False
      print('Jorginho ao entrar no bar foi direto para o balcão.')
      opcao = input('''Deseja pedir algo para beber?
      1 - sim
      2 - não
      ''')
      if(opcao == '1'):
        print('O garçom perguntou se Jorginho queria água com gelo ou cerveja')
        opcao = input('''O que você quer beber?
        1 - Água
        2 - Cerveja
        ''')
        if(opcao == '1'):
          print('Jorginho como estava morrendo de sede acabou bebendo a água muito rápido e engasgou com um cubo de gelo... rip')
          morreu('Jorginho')
        else:
          print('Jorginho tomou duas canecas de cerveja e saiu do bar')
          continuacaoJorginho(True)
      else:
        print('Jorginho bebeu nada.')
        continuacaoJorginho(False)

    elif(opcao == '2'):
      condicao = False
      print('Jorginho estava muito tonto após acordar e quando foi atravessar a rua acabou pisando no rabo de um gato que o arranhou, e no impulso Jorginho foi para o meio da pista e foi atropelado... rip')
      morreu('Jorginho')
    else:
      print('É 1 ou 2, chefia')


def continuacaoJorginho(beber):
  print('Jorginhou decidiu ir direto para o trabalho porque já estava atrasado')
  opcao = input('''Você quer pegar um ônibus ou ir andando?
  1 - Ir andando
  2 - Pegar um ônibus
  ''')
  if(opcao == '1'):
    print('Jorginho decidiu ir caminhando para o trabalho')
    print('Jorginho enquanto caminhava viu algo em seu caminho ao longe, um Ganso muito estranho estava o encarando.')
    opcao = input('''Jorginho então percebe que está pisando em algo, ele vai ver o que é?
    1 - sim
    2 - não
    ''')
    if(opcao == '2'):
      print('Jorginho decidiu não ligar para o que ele estava pisando, ao chegar mais próximo do Ganso ele percebeu que o Ganso começou a correr pra cima dele e com isso Jorginho ao tentar fugir da fera acabou tropeçando no seu próprio cadarço, com isso o Ganso conseguiu pegar-lo ... rip')
      morreu('Jorginho')
    else:
      print('Jorginho resolver olhar no que estava pisando e percebe que seu cadarço está desamarrado e assim ele o amarra adequadamente. ')
      print('Ao voltar pro seu caminho ele percebe que o Ganso não se escontrava mais em seu caminho e decide continuar seu percurso para a Serraria')
      opcao = input('''Quando finalmente Jorginho chega na Serraria seus amigos o chamam para conversar, mas Jorginho está atrasado e precisa bater seu ponto. O que Jorginho fará?
      1 - Ir conversar com seus amigos antes de bater o ponto
      2 - Ir logo bater o ponto
      ''')
      if(opcao == '1'):
        print('Após Jorginho bater um longo papo com seus amigos ele vai bater o ponto e percebe que está sendo feita uma manuntenção nele')
        print('Jorginho percebe que está muito atrasado e precisa bater o ponto ou pode somente ir trabalhar e dizer que esqueceu de bater o ponto.')
        opcao = input('''O que fazer?
        1 - Tentar bater o ponto mesmo em manuntenção
        2 - Ir trabalhar direto e meter o loko
        ''')
        if(opcao == '1'):
          print('Ao tentar bater o ponto a máquina explode na cara de Jorginho... rip')
          morreu('Jorginho')
        else:
          print('Jorginho começou a operar a máquina na produção de tábuas e percebeu que estava sem seus EPIs.')
          opcao = input('''Jorginho irá colocar os EPIs?
          1 - sim
          2 - não
          ''') 
          if(opcao == '1' and beber == True):
            print('Por conta da cerveja Jorginho enquanto colocava o seu EPI esqueceu de olhar se tinha algo em sua bota, tinha um escorpião... rip')
            morreu('Jorginho')
          if(opcao == '1' and beber == False):
            print('Jorginho verificou todo o seu EPI, inclusive tirou um escorpião de sua bota, porém a caminho da máquina ele viu algo brilhando no chão e se agachou para pegar, Jorginho só ouviu a buzina de um caminhão enquanto sorria por ter achado uma moeda de 1 Real... rip')
            morreu('Jorginho')
          if(opcao == '2'):
            print('Jorginho no auge da sua masculinidade resolveu que não precisava usar EPI até que uma farpa minúscula entrou no seu dedo, no susto ele acabou dando um passo para trás esbarrando em seu colega de trabalho, como ele já estava assustado virou bruscamente para ver no que ele tinha encostado e perdeu o equilíbrio caindo em cima da Serra... rip')
            morreu('Jorginho')
      else:
        print('Quando Jorginho colocou o dedo na máquina pra bater ponto ele levou um choque tão grande que o fritou... rip')
        morreu('Jorginho')
  else:
    print('Jorginho ao entrar no ônibus esqueceu de se segurar e com isso caiu e bateu a cabeça... rip')
    morreu('Jorginho')


# ====================================== JOGO DE GRAÇA =========================================================
def jogoGraca():
  print('A Professora Graça, frustrada com a falta de valorização na sua profissão pensa todos os dias em mudar de área.')
  opcao = input('''Deseja finalmente ir atrás de outra área profissional ou quer continuar fazendo a mesma coisa que a torna infeliz todos os dias ?
  1 - Continuar onde está e largar essa ideia boba
  2 - Pesquisar sobre outras profissões afim de encontrar algo que realmente a torne feliz
  ''')
  condicao = True
  while condicao:
    if(opcao == '2'):
      condicao = False
      print('Após 10 minutos de pesquisa Graça rapidamente achou algo extremamente interessante, ela se viu fascinada pela área de T.I e agora se sente motivada a seguir em frente e estudar mais sobre e seguir carreira na área.')
      opcao = input('''Apesar de estar muito divertido ver vários vídeos sobre T.I, especificamente sobre Análise de Dados, Graça sabe que precisa ir dar aula. Chegando na sua sala de aula ela se depara com uma turma extremamente mal-educada e pensa "Será que eu devo repreendê-los?"
      1 - Repreender a turma e falar a eles o porque da educação ser importante
      2 - Deixar para lá e começar a aula
      ''')
      if(opcao == '1'):
        print('A turma riu dela')
        opcao = input('''Como Graça agiu?
        1 - Graça começou a discutir com os alunos
        2 - Graça viu que são apenas crianças e conversou sobre histórias de malcriações que ela fez quando criança.
        ''')
        if(opcao == '1'):
          print('Graça tem um ataque nervoso correu pro meio da avenida... rip')
          morreu('Graça')
        else:
          print('Graça fica entusiasmada e foca mais na aula.')
          continuacaoGraca(True)
      else:
        print('A turma diminiu o barulho mas nem prestaram atenção na aula de Graça.')
        continuacaoGraca(False)

    elif(opcao == '1'):
      condicao = False
      print('Após 10 minutos ela se tocou que a vida dela sempre seria aquele inferno e teve um ataque cardíaco... rip')
      morreu('Graça')
    else:
      print('É 1 ou 2, chefia')


def continuacaoGraca(Programação):
  print('Após 3 aulas chegou o intervalo e Graça foi pra sala dos professores para poder comer algo e recuperar suas forças')
  opcao = input('''Ao abrir sua tupperware Graça viu uma cartinha, e quando foi ler tinham escrito "Obrigado pela refeição Professora". O que Graça fez a seguir?
  1 - Graça foi comprar algo pra comer na cantina imaginando que quando virasse Analista de Dados não precisaria passar por isso novamente
  2 - Graça foi atrás do aluno gritando pelo Colégio dizendo que ia dar um fim nele
  ''')
  if(opcao == '1'):
    print('Graça comprou sua coxinha e lata de coca')
    print('Por ser alérgica a amendoim, independente de qualquer coisa ela sempre examine se tem amendoim em tudo que vai comer')
    opcao = input('''Com esse dia tão conturbado Graça examinou se tinha amendoim na sua coxinha?
    1 - sim
    2 - não
    ''')
    if(opcao == '2'):
      print('Como estava com fome Graça praticamente engoliu sua coxinha, começando a ter uma crise alérgica e infelizmente ninguém tinha um antialérgico ... rip')
      morreu('Graça')
    else:
      print('Ao examinar a coxinha Graça se assusta ao achar um amendoim dentro dela. Após ela finalmente comer algo sem amendoim o seu intervalo acaba')
      print('No caminho para a sala de aula Graça vê 5 alunos batendo em 2 garotos')
      opcao = input('''Graça decide intervir ou deixa para lá ?
      1 - Intervir na confusão
      2 - Não ligar para isso
      ''')
      if(opcao == '1'):
        print('Graça abordou os alunos e após soltar os 2 que estavam sendo agredidos perguntou o porque daquilo estar acontecendo')
        print('Os 5 agressores disseram que os outros 2 estavam chamando eles de burros porque não conseguiam entender Informática')
        opcao = input('''Graça explicou que isso não era motivo pra bater nos 2. Qual solução ela sugeriu?
        1 - Dizer que isso era problema dela e ir embora
        2 - Explicar que agressão não levaria a nada e após eles pedirem desculpas pelo ocorrido ela propôs que os outros 2 ensinassem informática aos outros 5. Eles aceitaram as desculpas e disseram que não teria problemas em ensinar.
        ''')
        if(opcao == '1'):
          print('Em casa Graça vê na tv que os 2 jovens não aguentaram as agressões e rip, com isso Graça acaba se desesperando e ao correr para a cama tropeça e cai em um lápis... rip')
          morreu('Graça')
        else:
          print('Graça sai tranquila e vai dar a sua aula')
          opcao = input('''Ao entrar na aula a Turma estava como?
          1 - Estavam ansiosos esperando a Professora Graça começar a aula
          2 - encapetada
          ''') 
          if(opcao == '1' and Programação == True):
            print('Graça ficou tão feliz em ver a turma esperando ela que isso a impulsionou a ser Professora de Análise de Dados, anos mais tarde ela descobriu ter um problema no coração que foi agravado com os anos sendo professora do ensino médio e acabou indo para uma melhor ... rip')
            morreu('Graça')
          if(opcao == '1' and Programação == False):
            print('Graça ficou tão feliz em ver a turma esperando ela que acabou desmaiando de felicidade e caiu em cima da coleção de canetas de Rebelde de sua aluna... rip')
            morreu('Graça')
          if(opcao == '2'):
            print('Após tudo que aconteceu Graça não aguentou ver aquela turma encapetada, pegou seus pilotos e começou a jogar em todos os alunos e após isso sumiu no meio do mato... rip')
            morreu('Graça')
      else:
        print('Graça decide continuar sendo professora do ensino médio para sempre e acaba tendo uma vida infeliz fazendo aquilo que não gosta... rip')
        morreu('Graça')
  else:
    print('Após esse incidente Graça enlouqueceu e foi internada em uma clínica psiquiátrica... rip')
    morreu('Graça')


# ====================================== JOGO DE ZECA =========================================================
def jogoZeca():
  print('Você escolheu o Zeca da Kombi. Ele está prestes a acordar para o trabalho.')
  opcao = input('''Deseja acordar e ir ao trabalho ou continuar dormindo?
  1 - acordar
  2 - continuar dormindo
  ''')
  condicao = True
  while condicao:
    if(opcao == '1'):
      condicao = False
      print('Zeca acordou!')
      opcao = input('''Deseja tomar banho?
      1 - sim
      2 - não
      ''')
      if(opcao == '1'):
        print('Zeca foi tomar banho, mas seu sabonete caiu no chão')
        opcao = input('''Como deseja pegar o sabonete?
        1 - pegar com o pé
        2 - pegar com a mão
        ''')
        if(opcao == '1'):
          print('Zeca escorregou e bateu a cabeça... rip')
          morreu('Zeca')
        else:
          print('Zeca pegou o sabonete e terminou seu banho')
          continuacaoZeca(True)
      else:
        print('Zeca não tomou banho.')
        continuacaoZeca(False)

    elif(opcao == '2'):
      condicao = False
      print('Zeca da Kombi dormiu tanto que o urubu levou... rip')
      morreu('Zeca')
    else:
      print('É 1 ou 2, chefia')


def continuacaoZeca(banho):
  print('Zeca foi tomar café da manhã')
  opcao = input('''Tomar café ou Iogurte?
  1 - Café
  2 - Iogurte
  ''')
  if(opcao == '1'):
    print('Zeca comeu seu pão, tomou seu café e foi trabalhar')
    print('Zeca entrou na Kombi para trabalhar')
    opcao = input('''Verificar a marcha?
    1 - sim
    2 - não
    ''')
    if(opcao == '2'):
      print('Zeca não verificou a marcha e, ao ligar, não percebeu que estava em primeira e bateu a Kombi... rip')
      morreu('Zeca')
    else:
      print('Zeca verificou a marcha e percebeu que estava em primeira, colocou no neutro e ligou a Kombi')
      print('Zeca foi ao terminal das Kombis e, ao chegar lá, viu um buraco')
      opcao = input('''Passar por cima do buraco ou desviar?
      1 - passar por cima
      2 - desviar
      ''')
      if(opcao == '1'):
        print('Zeca passou tranquilamente por cima do buraco')
        print('A Kombi de Zeca estava abastecida de passageiros e ele começou seu trajeto e percebeu que o cabo do freio da Kombi rompeu')
        opcao = input('''O que fazer?
        1 - se jogar da Kombi para se salvar
        2 - jogar a Kombi para o acostamento
        ''')
        if(opcao == '1'):
          print('Zeca pulo da Kombi para se salvar, mas acabou sendo atropelado por outro carro... rip')
          morreu('Zeca')
        else:
          print('Zeca jogou a Kombi para o acostamento')
          opcao = input('''Zeca estava usando cinto de segurança?
          1 - sim
          2 - não
          ''') 
          if(opcao == '1' and banho == True):
            print('Zeca jogou a Kombi para o acostamento e ficou tão feliz por ter sobrevivido que sofreu uma parada cardíaca... rip')
            morreu('Zeca')
          if(opcao == '1' and banho == False):
            print('Zeca jogou a Kombi para o acostamento e, apesar de ter sobrevivido, Zeca fedia tanto que foi confundido com um cadáver e enterrado vivo... rip')
            morreu('Zeca')
          if(opcao == '2'):
            print('Zeca jogou a Kombi para o acostamento e, como estava sem cinto de segurança, foi arremessado e acabou sendo atropelado por outro carro... rip')
            morreu('Zeca')
      else:
        print('Enquanto desviava, viu um doguinho e, ao tentar desviar, perdeu o controle e bateu em um poste... rip')
        morreu('Zeca')
  else:
    print('Zeca esqueceu que era intolerante a lactose e teve diarreia... rip')
    morreu('Zeca')


# ====================================== FUNCAO DE SAIR DO JOGO =========================================================
def sairJogo():
  condicao = False
  condicaoOut = True
  while condicaoOut:
    out = input('''Deseja realmente sair do jogo?
    1 - sim (e seu computador explode)
    2 - não (e você ganha um abraço :D)
    ''')
    if(out == '1'):
      condicaoOut = False
      print('Falou, comparça!')
      exit()
    elif(out == '2'):
      menuPrincipal()
    else:
      print('É 1 ou 2, chefia')

# ====================================== FUNCAO SOBRE O JOGO =========================================================
def sobreJogo():
  condicao = False
  print('''                               
                                  ==== NOME DO JOGO ==== 
                                        Bem vindo! 
      Neste jogo, você vai acompanhar três personagens, cada um com uma história diferente: 
  Jorginho da Serraria - trabalha em uma serraria, ajude-o a não morrer em um acidente de trabalho,
  Zeca da Kombi - trabalha como motorista de Kombi, ajude-o a não morrer em um acidente de trânsito,
            Professora Graça - trabalha em uma escola, ajude-a a não morrer de estresse.
              Sua missão é não deixar que seu personagem morra de uma forma idiota.
                                        Boa sorte!!
                                Criado por: Bruno Arruda''')

# ====================================== FUNCAO ESCOLHA PERSONAGEM =========================================================
def escolhaPersonagem():
  condicao = False
  condicaoPersonagem = True
  while condicaoPersonagem:
    personagem = input('''escolha seu personagem: 
    1 - Jorginho da Serraria
    2 - Zeca da Kombi
    3 - Professora Graça
    ''')
    if(personagem == '1'):
      jogoJorginho()
    elif(personagem == '2'):
      jogoZeca()
    elif(personagem == '3'):
      jogoGraca()


def escolhaMenu(opcao):
  if(opcao == '1'):
    escolhaPersonagem()
  elif(opcao == '2'):
    sobreJogo()
  elif(opcao == '3'):
    sairJogo()
  else: 
    print('É 1, 2 ou 3, chefia')

# ====================================== FUNCAO MENU =========================================================
def menuPrincipal():
  opcao = '0'
  print('''
                                              ---- MENU PRINCIPAL ----
                                                     1 - JOGAR
                                                     2 - SOBRE
                                                     3 - SAIR''')
  
  condicao = True
  while condicao:
    opcao = input('Escolha a opção desejada: '.rjust(72))
    escolhaMenu(opcao)

# ====================================== FUNCAO MORREU =========================================================
def morreu(personagem):
  print(personagem, 'morreu e você perdeu o jogo! :(')
  menuPrincipal()


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('                                                 Bem vindos(as) ao jogo                                                 ')
print('                                            - HOW NOT NOT DIE LIKE AN IDIOT -                                           ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# ====================================== CHAMANDO O MENU =========================================================
menuPrincipal()