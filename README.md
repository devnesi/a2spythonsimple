## Sobre
Servidor http simples para realizar consulta de players em servidores da valve utlizando a2s
### Preparar o ambiente e executar utilizando virtualenv
  1. Instale o python3.7 | *sudo apt install python3.7*
  2. Instale o ambiente virtual para o python3.7 | *sudo apt install python3.7-venv*
  3. Dentro do diretorio do projeto execute | *python3.7 -m venv venv*
  4. Entre dentro do ambiente virtual | *. venv/bin/activate*
  5. Instale as dependecias | *pip install -r requeriments.txt*
  6. Execute | *python server.py*
  #### Lembre-se que toda vez antes de executar o **passo 6** você deve estar dentro do ambiente virtual **passo 3**
  
### Preparar o ambiente e executar com python global
  1. Instale o python3.7 | *sudo apt install python3.7*
  2. Instale as dependecias | *pip3 install -r requeriments.txt*
  3. Execute | *python3.7 server.py*
  
### Uso
  0.0.0.0:8000/IP:PORTA
