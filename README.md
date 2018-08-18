#Cminus Compiler

## How to run

1. Install pipenv

        $ pip install pipenv

2. Install Antlr 4.7 on LINUX

        $ cd /usr/local/lib

        $ wget https://www.antlr.org/download/antlr-4.7.1-complete.jar

        $ export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

        $ alias antlr4='java -jar /usr/local/lib/antlr-4.7.1-complete.jar'

        $ alias grun='java org.antlr.v4.gui.TestRig'

3. cd into the repository

4. Install the dependencies

        $ sudo pipenv install //sudo pipenv --python python3.6 install
		$ pipenv shell

5. Install antlr4

        $ pip install antlr4-python3-runtime

	or pip version 10.x

		$ sudo apt install python3-pip --reinstall
		$ python3 -m pip install antlr4-python3-runtime
		
6. Install tabulate

        $ pip install tabulate

	 or pip version 10.x

		$ python3 -m pip install tabulate
	
7. To generate the parse
 
        $ antlr4 -Dlanguage=Python3 -visitor -o compilador/gen cminus.g4

8. To run the compiler

		$ python3 -m project --lexer --ast --symbol --intermediate  --asbly --bin --file testes/pudim.txt

## Command Line Options

The compiler runs as a Python module, so you have to run python -m compiler to actually execute the compiler.

To make the compiler output the tokens, add the option --lexer.

To make the compiler output the AST, add the option --ast.

To make the compiler output the symbol table, add the option --symbol.

To make the compiler output intermediate code, add the option --middle.

To make the compiler output assembly code, add the option --asm.

To make the compiler output machine code, add the option --bin.

To specify which file it should compile, add the option --file <your file here>.