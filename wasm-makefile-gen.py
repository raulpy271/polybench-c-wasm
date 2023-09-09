"""
usage: python wasm-makefile-gen.py
"""

import os


categories = (
    'linear-algebra/blas',
    'linear-algebra/kernels',
    'linear-algebra/solvers',
    'datamining',
    'stencils',
    'medley'
)

makefile_text = """
CHEERP=/opt/cheerp/bin/clang
EMCC=emcc
CHEERP_FLAGS=-O2 -cheerp-pretty-code -target cheerp-wasm -cheerp-linear-heap-size=524 -cheerp-make-module=es6
EMCC_FLAGS=-O2 --minify 0 -sINITIAL_MEMORY=1114112 -sALLOW_MEMORY_GROWTH -sMAXIMUM_MEMORY=$$((500 * 1024 * 1024))
POLYBENCH_FLAGS=-DPOLYBENCH_TIME

.PHONY: all clean

all: {filename}_cheerp.mjs {filename}_cheerp.html {filename}_emscripten.mjs {filename}_emscripten.html

{filename}_cheerp.wasm {filename}_cheerp.mjs: {filename}.c {filename}.h
	$(CHEERP) $(CHEERP_FLAGS) $(POLYBENCH_FLAGS) \\
		-I {utilities} -I . \\
        {utilities}/polybench.c {filename}.c \\
		-o {filename}_cheerp.mjs
	cat {utilities}/cheerp_capture_time.js >> {filename}_cheerp.mjs
	# Store initial size of the heap
	sed -E -i '/function\s+__start\s*\(/a initial_memory = __heap.byteLength;' {filename}_cheerp.mjs
	# Store final size of the heap and return result
	sed -E -i \\
        '/^\s*__start\s*\(\s*\)/a memory_used = __heap.byteLength; return {{polybench_time, initial_memory, memory_used}};' \\
        {filename}_cheerp.mjs

{filename}_emscripten.wasm {filename}_emscripten.mjs: {filename}.c {filename}.h
	$(EMCC) $(EMCC_FLAGS) $(POLYBENCH_FLAGS) \\
		-I {utilities} -I . \\
        {utilities}/polybench.c {filename}.c \\
		--post-js {utilities}/emscripten_capture_time.js \\
		-o {filename}_emscripten.mjs

{filename}_cheerp.html: {utilities}/runner.template.html
	sed 's/$$ALGORITHM/{filename}/;s/$$COMPILER/cheerp/' {utilities}/runner.template.html > {filename}_cheerp.html

{filename}_emscripten.html: {utilities}/runner.template.html
	sed 's/$$ALGORITHM/{filename}/;s/$$COMPILER/emscripten/' {utilities}/runner.template.html > {filename}_emscripten.html

clean:
	@ rm -f {filename}*.mjs {filename}*.wasm {filename}*.html

"""

def create_makefiles():
    utilities_path = os.getcwd() + "/utilities"
    for category_path in categories:
        for algorithm in os.listdir(category_path):
            makefile_path = category_path + '/' + algorithm + '/Makefile'
            print('creating file', makefile_path)
            with open(makefile_path, 'wt') as makefile:
                makefile.write(makefile_text.format(
                    filename=algorithm,
                    utilities=utilities_path
                ))

if __name__ == '__main__':
    create_makefiles()

