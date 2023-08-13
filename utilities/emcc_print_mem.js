
var polybench_time = null;
var memory_used = null;
var _log = out;

function capture_time(time) {
    polybench_time = parseFloat(time);
    out = _log;
}

out = capture_time;

__ATPOSTRUN__.push((module) => {
    memory_used = module.asm.memory.buffer.byteLength;
    console.log(polybench_time);
    console.log(memory_used);
})

