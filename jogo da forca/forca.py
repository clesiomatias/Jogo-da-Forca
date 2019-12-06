#-*-coding utf-8 -*-
'''Clone do jogo clássico da "forca", programado em python
utilizando o modulo gráfico nativo Turtle e banco de dados com 
arquivos .txt'''

#-- Escopo de importações --
import turtle
import random
import time

#-- Escopo de variáveis globais --
score = 0 #variavel de controle dos pontos conquistados
niveis = 1 # variavel de controle dos niveis, alterados segundo o score
palavra ='' #variavel que controla a palavra escolhida
jogando = True #variavel de controle do loop do jogo

#-- variavel que permite o reset da janela atravez da
# função cria_janela
janela = None 
erro = 0# variavel de controle de erros
escolhas = []#variavel que guarda as escolhas pra conferir se não se repetem

#----Registro de imagens---#
turtle.register_shape('forca.gif')
turtle.register_shape('corda.gif')
turtle.register_shape('cabeça.gif')
turtle.register_shape('bDir.gif')
turtle.register_shape('bEsq.gif')
turtle.register_shape('pDir.gif')
turtle.register_shape('pEsq.gif')
turtle.register_shape('peito.gif')
turtle.register_shape('barriga.gif')
#-- Escopo de objetos do jogo
'''todos os objetos do jogo serão criados
através de chamadas de funções'''

#-- Escopo de funções --
def cria_janela():
	global janela
	#desenhando janela
	janela = turtle.Screen()
	janela.setup(800,600)
	janela.title('Jogo da Forca')
	janela.bgcolor('green')
	
	#desenhando a forca
	forca = turtle.Turtle()
	forca.shape('forca.gif')
	forca.speed(0)
	forca.pu()
	forca.setpos(-200,75)
	
	# desenhando o score
	score_pen = turtle.Turtle()
	score_pen.speed(0)
	score_pen.ht()
	score_pen.color('white')
	score_pen.setpos(0,250)
	score_pen.clear()#sempre que a janela é redesenhada, reseta o score_pen
	score_pen.write(f'Score: {score}', font = ('Arial', 32,'normal'))
	
	# desenhando o nivel atual
	nivel_pen = turtle.Turtle()
	nivel_pen.speed(0)
	nivel_pen.ht()
	nivel_pen.color('white')
	nivel_pen.setpos(190,250)
	nivel_pen.clear()#sempre que a janela é redesenhada, reseta o nivel_pen
	nivel_pen.write(f'-  Nível: {niveis}', font = ('Arial', 32,'normal'))


#---------------
'''funções que desenharão as partes do corpo e a corda
se o usuario errar a(s) letra(s)'''

def criaCabeca():
	cabeca = turtle.Turtle()
	cabeca.speed(0)
	cabeca.pu()
	cabeca.ht()
	cabeca.shape('cabeça.gif')
	cabeca.setpos(-90,155)
	cabeca.st()
	

def criaCorda():
	corda = turtle.Turtle()
	corda.speed(0)
	corda.pu()
	corda.ht()
	corda.shape('corda.gif')
	corda.setpos(-90,155)
	corda.st()

def cria_pEsq():
	pEsq = turtle.Turtle()
	pEsq.speed(0)
	pEsq.pu()
	pEsq.ht()
	pEsq.shape('pEsq.gif')
	pEsq.setpos(-80,-85)
	pEsq.st()	

def cria_pDir():
	pDir = turtle.Turtle()
	pDir.speed(0)
	pDir.pu()
	pDir.ht()
	pDir.shape('pDir.gif')
	pDir.setpos(-15,-85)
	pDir.st()

def cria_bDir():
	bDir = turtle.Turtle()
	bDir.speed(0)
	bDir.pu()
	bDir.ht()
	bDir.shape('bDir.gif')
	bDir.setpos(-25,32)
	bDir.st()

def cria_bEsq():
	bEsq = turtle.Turtle()
	bEsq.speed(0)
	bEsq.pu()
	bEsq.ht()
	bEsq.shape('bEsq.gif')
	bEsq.setpos(-122,40)
	bEsq.st()

def criaBarriga():
	barriga = turtle.Turtle()
	barriga.speed(0)
	barriga.pu()
	barriga.ht()
	barriga.shape('barriga.gif')
	barriga.setpos(-65,0)
	barriga.st()

def criaPeito():
	peito = turtle.Turtle()
	peito.speed(0)
	peito.pu()
	peito.ht()
	peito.shape('peito.gif')
	peito.setpos(-75,60)
	peito.st()
#---------

'''função que escolhe uma palavra segundo o nivel:
score até 4  nivel 1
score de 5 a 10 nivel 2
score de 11 a 15 nivel 3
score acima de 16 nivel 4'''
def escolhePalavra():
	global score
	if score <= 4: #verifica o score
		nivel = open('nivel1.txt','r') #abre o arquivo especifico do nivel atual
	elif score <=10 :		
		nivel = open('nivel2.txt','r')
	elif score <= 15:		
		nivel = open('nivel3.txt','r')
	else:		
		nivel = open('nivel4.txt','r')
		
	#cria a lista de palavras segundo o arquivo do nivel		
	palavras = nivel.readlines()
	return random.choice(palavras) # retorna a palavra escolhida

'''função que trata caracteres especiais nas palavras escolhidas'''
def trata_char_especial(p):
	#especiais = ÀÂÄÁÅ Ç ÈÊÉË ÏÌÎÍ ÒÖÓÕÔ ÙÜÚÛ
	nova = '' #palavra temporaria
	
	#percorrenco a palavra escolhida e substituindo
	#os caracteres especiais por caracteres normais  
	for letra in p:
		if letra in 'ÀÂÄÁÅÃ': 
			nova+='A'
		elif letra in 'ÈÊÉË':
			nova+='E'
		elif letra in 'ÏÌÎÍ':
			nova +='I'
		elif letra in 'ÒÖÓÕÔ':
			nova+='O'
		elif letra in 'ÙÜÚÛ':
			nova+= 'U'
		elif letra == 'Ç':
			nova += 'C'
		else: 
			nova+=letra
	#retornando a palavra escolhida já tratada, sem cc especiais
	return nova
	
	
'''função que desenha as partes do corpo 
segundo os erros do usuário'''
def trata_erro(erros):
	if erros == 1:
		criaCabeca()
	elif erros == 2:
		criaPeito()
	elif erros == 3:
		criaBarriga()
	elif erros == 4:
		cria_bDir()
	elif erros == 5:
		cria_bEsq()
	elif erros == 6:
		cria_pDir()
	elif erros == 7:
		cria_pEsq()
	elif erros == 8:
		criaCorda()


#loop do jogo (main_loop)
while jogando:
	cria_janela()#inicia a janela
	 #escolhe palavra e coloca tudo em maiúsculas
	palavra = escolhePalavra().upper()
	#trata a palavra escolhida e reserva numa palavra temporaria
	palavra_t = trata_char_especial(palavra)
	#variavel que representa as letras. 
	palavra_escondida = '' 
	
	#desehando a palavra escondida
	for i in range(len(palavra)-1):
		palavra_escondida += '-'	
	turtle.ht()
	turtle.speed(0)
	turtle.pu()
	turtle.setpos(-150,-320)
	turtle.write(palavra_escondida,font = ('Arial',100,'bold'))
	
	#loop de tentativas do jogo
	while True: 
		#obtendo a resposta do usuario
		resposta = str(turtle.textinput('Escolha uma Letra:','')).upper()
		#se a errou:
		if resposta not in palavra_t:
			erro+=1 #aumenta a variavel de erros
			trata_erro(erro)
			#mostra a mensagem de erro
			msg_erro = turtle.Turtle()
			msg_erro.ht()
			msg_erro.pu()
			msg_erro.color('red')
			msg_erro.write('letra errada',font = ('Arial',40,'bold') )
			msg_erro.speed(0)
			msg_erro.setpos(150,150)
			time.sleep(0.5)
			msg_erro.clear()
			#se errar oito vezes perde
			if erro == 8:
				#mostra a mensagem de fim
				turtle.clear()
				turtle.setpos(-200,-250)
				turtle.write('Você foi enforcado',font = ('Arial',40,'bold'))
				time.sleep(1)
				#Mostra a palavra certa
				turtle.clear()
				turtle.setpos(-200,-350)
				turtle.write(f'Palavra correta:\n{palavra}',font = ('Arial',40,'bold'))
				#para o loop de tentativas
				break
		# se a letra for repetida
		if resposta in escolhas:
			erro+=1
			trata_erro(erro)
			#mostra a mensagem de erro por repetição
			msg_erro = turtle.Turtle()
			msg_erro.ht()
			msg_erro.pu()
			msg_erro.color('blue')
			msg_erro.write('Letra Repetida',font = ('Arial',40,'bold') )
			msg_erro.speed(0)
			msg_erro.setpos(150,150)
			time.sleep(0.5)
			msg_erro.clear()
			
			if erro == 8:
				#mostra a mensagem de fim
				turtle.clear()
				turtle.setpos(-200,-250)
				turtle.write('Você foi enforcado',font = ('Arial',40,'bold'))
				time.sleep(1)
				#Mostra a palavra certa
				turtle.clear()
				turtle.setpos(-200,-350)
				turtle.write(f'Palavra correta:\n{palavra}',font = ('Arial',40,'bold'))
				#para o loop de tentativas
				break
		# se acertou a letra
		if resposta in palavra_t:
			contador =0# variavel que controla a posição da letra certa dentro da palavra
			#percorrendo a palavra tratada
			for letra in palavra_t:
				# transformando a palavra escondida em lista
				#para facilitar a substituição
				palavra_escondida = list(palavra_escondida)
				#verificando se a resposta é a letra atual
				if letra == resposta:
					#fazendo a substituição na tela  to traço pela letra
					del(palavra_escondida[contador])
					palavra_escondida.insert(contador,palavra[contador])
					palavra_escondida = str().join(palavra_escondida)
					turtle.clear()
					turtle.write(palavra_escondida,font = ('Arial',100,'bold'))
				contador +=1 #aumentando o contador
	
		#inserindo a letra escolhida na lista de escolhas
		#para verificar se foi repetida	
		escolhas.append(resposta)
		#verificando se completou a palavra
		if '-' in palavra_escondida:
			# se não completou
			continue
		else:
			# se completou
			score+=1# aumenta score
			#aumenta nivel
			if score <= 4:
				niveis = 2
			elif score <= 10:
				niveis = 3
			elif score <= 15:
				niveis = 4
			#mostra mensagem de vitoria
			msg_venceu = turtle.Turtle()
			msg_venceu.ht()
			msg_venceu.pu()
			msg_venceu.color('yellow')
			msg_venceu.speed(0)
			msg_venceu.setpos(-300,-200)
			msg_venceu.write('Parabéns voce venceu!',font = ('Arial',35,'bold') )
			
			time.sleep(1.5)
			msg_venceu.clear()
			#para o loop de tentativas
			break
	#pergunta se quer jogar novamente
	novo_jogo = str(turtle.textinput('Jogar novamente:',' [S/N]'))
	#loop de verificação de escolha jogar novamente
	while True:
		
		if novo_jogo in 'Ss':
			#se jogar de novo
			turtle.clear()#limpa a palavra da tela
			erro=0 # zera os erros
			escolhas=[] #zera as escolhas
			janela.clear() #limpa a tela
			break # para o loop de verificação
		if novo_jogo in "Nn":
			#se não jogar de novo
			time.sleep(0.5)#pequena pausa
			janela.clear()#limpa janela
			#mostra mensagem final
			msg_final = turtle.Turtle()
			msg_final.ht()
			msg_final.pu()
			msg_final.color('gray')
			msg_final.speed(0)
			msg_final.setpos(-200,-150)
			msg_final.write('Obrigado\n     por\n   jogar!',font = ('Arial',70,'bold') )
			
			time.sleep(2)#pequena pausa
			janela.bye()# fecha janela e encerra programa
		else:
			#se a opção não for nem 's' nem 'n', tenta outra vez
			novo_jogo = turtle.textinput('Jogar novamente:',' [S/N]')
				
#loop da janela		
janela.mainloop()
