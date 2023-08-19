
var polybench_time = null;
var initial_memory = null;
var memory_used = null;
var _log = console.log;

function capture_time(time) {
    polybench_time = parseFloat(time);
    console.log = _log;
}

console.log = capture_time;

__dummy.promise.then(() => {
    memory_used = __heap.byteLength;
    console.log(polybench_time);
    console.log(initial_memory);
    console.log(memory_used);
});


