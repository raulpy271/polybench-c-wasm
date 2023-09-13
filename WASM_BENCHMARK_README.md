# WebAssembly benchmark 

# Execução do benchmark

### Instalar browsers: firefox e chrome

Após instalar ambos os browsers, ativar as flags:
 - Firefox: Acessar `about:config` e ativar `dom.allow_scripts_to_close_windows`
 - Chrome: Acessar `chrome://flags/` e ativar "Download Bubble"

### Instalar cheerp

```bash
# Adding the repository
sudo add-apt-repository ppa:leaningtech-dev/cheerp-ppa
sudo apt-get update

# To install all cheerp components, run
apt-get install cheerp-core
```

### Instalar emscripten

Instalação via compilação de código fonte:

```
# Get the emsdk repo
git clone https://github.com/emscripten-core/emsdk.git
git pull

# Download and install the latest SDK tools.
./emsdk install latest

# Make the "latest" SDK "active" for the current user. (writes .emscripten file)
./emsdk activate latest

# Activate PATH and other environment variables in the current terminal
source ./emsdk_env.sh
```

