/***************************************************/

Requisitos:

	-Antlr4.7

/***************************************************/

Instação do Antlr4 (Ubuntu 16.04): 

	Antlr is a parser generator written in Java.

	Execute these commands to download atlr .jar file in /usr/local/lib directory

	$ cd /usr/local/lib
	$ curl -O http://www.antlr.org/download/antlr-4.7-complete.jar


	add antlr4 to your class path.

	$ export CLASSPATH=".:/usr/local/lib/antlr-4.7-complete.jar:$CLASSPATH"

	create alias

	$ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
	$ alias grun='java org.antlr.v4.runtime.misc.TestRig'

	Test installation

	$ java org.antlr.v4.Tool

	"ANTLR Parser Generator  Version 4.5
	 -o ___              specify output directory where all output is generated
	 -lib ___            specify location of grammars, tokens files
	 -atn                generate rule augmented transition network diagrams
	...........
	..........."

	The above 3 commands (one export and two alias commands) needs to be run every time you start a new terminal. To solve this problem put the three commands in your .bashrc file like shown below.

	Open the.bashrc file in any text editor 
	gedit ~/.bashrc

	and add the three commands at the bottom of the file.

	Note: bashrc is a script file that automatically executes whenever a new terminal is opened.

	Por fim, instale a extensao do antlr4 para o python.

	pip install antlr4-python3-runtime

/***************************************************/

Procedimento:

	Para gerar o analisador léxico e o parser através da gramática .g4 :

	$ antlr4 -Dlanguage=Python3 cminus.g4
    
    Desta forma aparecerá os arquivos gerados:
    -cminus.tokens
    -cminusLexer.py
    -cminusLexer.tokens
    -cminusListener.py
    -cminusParser.py

    Esses arquivos estão presentes na pasta 'arquivos gerados'. Caso precise para os testes, mover todos arquivos citados acima para a pasta raiz.

	Para executar o analisado em cima de um arquivo teste:

	$ python tree.py gdc_sem_erros.txt

    Utilizar códigos testes da própria pasta, pois foram retirados caracteres UniCode, pois apresentavam erros na compilacao.
