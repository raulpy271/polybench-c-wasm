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
CHEERP_FLAGS=-cheerp-pretty-code -target cheerp-wasm
POLYBENCH_FLAGS=-DMEDIUM_DATASET -DPOLYBENCH_TIME -DPOLYBENCH_NO_FLUSH_CACHE

{filename}_cheerp.wasm {filename}_cheerp.js: {filename}.c {filename}.h
	$(CHEERP) $(CHEERP_FLAGS) $(POLYBENCH_FLAGS) \\
		-I {utilities} -I . \\
        {utilities}/polybench.c {filename}.c \\
		-o {filename}_cheerp.js
	cat {utilities}/cheerp_print_mem.js >> {filename}_cheerp.js

{filename}_ems.wasm {filename}_ems.js: {filename}.c {filename}.h
	$(EMCC) $(POLYBENCH_FLAGS) \\
		-I {utilities} -I . \\
        {utilities}/polybench.c {filename}.c \\
		--post-js {utilities}/emcc_print_mem.js \\
		-o {filename}_ems.js

clean:
	@ rm -f *.wasm *.js

"""

def create_makefiles():
    utilities_path = os.getcwd()
    for category in categories:
        category_path = '../' + category
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

