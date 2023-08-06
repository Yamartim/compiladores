# T4 - analisador semântico

Membros:
- Fernando Oliveira
- Martim Lima

### Tutorial para a execução com o corretor automatico:
`$ java -jar compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python3 main.py" gcc <pasta temp> <indicar a pasta casos-de-teste> <nome do grupo> "t3"`

Exemplo de execução no Ubuntu:
`$ java -jar compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python3 main.py" gcc ../temp/ ../casos-de-teste/casos-de-teste "nome do grupo" "t3"`

### Tutorial t4 passo a passo:
1. Fazer o download dos arquivos

2. Compilar com 

`$ java -jar <arquivo antlr.jar> Alguma.g4 -Dlanguage=Python3 -visitor`
  
3. Caso não esteja instalado, instalar o módulo antlr runtime,
  
 `$ pip install -r requirements.txt`
 
  e rodar a main com:

 `$ python3 main.py <arquivo de entrada> <arquivo de saida>`
