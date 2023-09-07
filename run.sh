#!/bin/bash

DOWNLOAD_DIR="/home/raul/Downloads"
FULL_BENCHMARK="$DOWNLOAD_DIR/benchmark_full.csv"

CATEGORIES=(
    'linear-algebra/blas'
    'linear-algebra/kernels'
    'linear-algebra/solvers'
    'datamining'
    'stencils'
    'medley'
)

run_each_algorithm () {
    for category in ${CATEGORIES[@]};
    do
        curr_pwd=`pwd`
        algorithms=`ls $category`
        for algorithm in $algorithms;
        do
            benchmark_path=$category/$algorithm
            echo "Entering $benchmark_path"
            cd $benchmark_path
            make -s clean
            make -s
            echo "Running benchmark"
            python -m http.server &
            firefox --private-window http://localhost:8000/${algorithm}_cheerp.html
            firefox --private-window http://localhost:8000/${algorithm}_emscripten.html
            echo "Benchmark runned."
            kill `pidof python`
            cd $curr_pwd
        done
    done
}

create_full_benchmark_result () {
    benchmark_files=(`ls $DOWNLOAD_DIR/benchmark_*`)
    # Create CSV Header
    head -n 1 ${benchmark_files[0]} > $FULL_BENCHMARK
    # Create CSV Body
    tail -q -n +2 ${benchmark_files[@]} >> $FULL_BENCHMARK
}

run_each_algorithm
echo "Crating full CSV"
create_full_benchmark_result
echo $FULL_BENCHMARK " created!"
