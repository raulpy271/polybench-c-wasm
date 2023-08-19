
var polybench_time = null;
var initial_memory = null;
var memory_used = null;
var _log = out;

function capture_time(time) {
    polybench_time = parseFloat(time);
    out = _log;
}

out = capture_time;

__ATMAIN__.push((module) => {
    initial_memory = module.asm.memory.buffer.byteLength;
});

__ATPOSTRUN__.push((module) => {
    memory_used = module.asm.memory.buffer.byteLength;
    console.log(polybench_time);
    console.log(initial_memory);
    console.log(memory_used);
})

