# Compilação do Polybench/C para WebAssembly e execução dos algoritmos no navegador 

Esse repositório contém ferramentas necessárias para realizar a compilação do Polybench/C para plataforma WebAssembly e executa-lo no navegador. Ao executar os algoritmos no navegador é capturado métricas de uso de memória e tempo de execução, esses dados são salvos em disco no formato CSV.

Foi previamente executado os algoritmos utilizando as ferramentas aqui disponíveis, os resultados obtidos encontram-se no diretório [`results`](results).

O repositório foi criado como o _fork_ do Polybench/C, isto é, os arquivos do _benchmark_ foram copiados para o repositório e em seguida foi adicionado _scripts_ para realizar a compilação dos algoritmos. Os arquivos adicionados são: [run.sh](run.sh), [wasm-makefile-gen.py](wasm-makefile-gen.py), [cheerp_capture_time.js](utilities/cheerp_capture_time.js), [emscripten_capture_time.js](utilities/emscripten_capture_time.js) e [runner.template.html](utilities/runner.template.html).

# Instalação das ferramentas

### Instalar Python 3.8

### Instalar browsers: firefox e chrome

Após instalar ambos os browsers, ativar as flags:
 - Firefox: Acessar `about:config` e ativar `dom.allow_scripts_to_close_windows`
 - Chrome: Acessar `chrome://flags/` e desativar "Download Bubble"

### Instalar cheerp 3.0

```bash
sudo add-apt-repository ppa:leaningtech-dev/cheerp-ppa
sudo apt-get update

sudo apt-get install cheerp-core=3.0-1~focal
```

### Instalar emscripten v3.1.36

Instalação via compilação de código fonte:

```
git clone https://github.com/emscripten-core/emsdk.git
git pull

./emsdk install 3.1.36

./emsdk activate 3.1.36

# Adiciona executável do emsdk em $PATH
source ./emsdk_env.sh
```

# Compilação e execução no navegador

Após instalar as ferramentas necessárias, a execução pode ser feita utilizando o _script_ [run.sh](run.sh). Antes de executa-lo, Pode-se alterar as seguintes variáveis do mesmo:

```sh
# Caminho do executável do firefox
FIREFOX=/home/professor/Downloads/firefox/firefox
# Caminho do executável do google chrome
CHROME=google-chrome-stable
# Caminho onde é feito download de arquivos no navegador
DOWNLOAD_DIR="$HOME/Downloads"
```

Por fim, a execução pode ser feita com o comando:

```
./run.sh
```

Esse comando irá compilar cada algoritmo do Polybench/C e abrir ambos os navegadores para execução de cada algoritmo.

