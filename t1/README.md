# T1 compiladores
Membros:
- Fernando Oliveira
- Martim Lima

### Tutorial para a execução com o corretor automatico:
`$ java -jar compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python3 main.py" gcc <pasta temp> <indicar a pasta casos-de-teste> <nome do grupo> "t1"`

Exemplo de execução no Ubuntu:
`java -jar compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python3 main.py" gcc ../temp/ ../casos-de-teste/casos-de-teste "7" "t1"`

### Tutorial t1 passo a passo:
1. Fazer o analisador léxico no arquivo .g4

2. Compilar com 

`$ java -jar <arquivo antlr.jar> <arquivo.g4> -Dlanguage=Python3`
  
3. Fazer uma main.py importando o arquivoLexer (tem um exemplo de main para o primeiro caso de teste no arquivo main.py)
  
4. instalar o módulo antlr runtime e rodar a main com
  
 `$ pip install -r requirements.txt`
 `$ python3 main.py <arquivo de entrada> <arquivo de saida>`
