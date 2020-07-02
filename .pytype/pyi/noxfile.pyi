
from typing import Any
def __getattr__(name: Any) -> Any: ...
# Caught error in pytype: tuple index out of range
# Traceback (most recent call last):
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/io.py", line 155, in check_or_generate_pyi
#     errorlog, result, ast = generate_pyi(
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/io.py", line 112, in generate_pyi
#     errorlog, (mod, builtins) = _call(
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/io.py", line 65, in wrapper
#     return f(*args, **kwargs)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/io.py", line 78, in _call
#     return errorlog, analyze_types(
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/analyze.py", line 687, in infer_types
#     tracer.exitpoint = tracer.analyze(loc, defs, maximum_depth)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/analyze.py", line 426, in analyze
#     return self.analyze_toplevel(node, defs)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/analyze.py", line 401, in analyze_toplevel
#     new_node = self.analyze_function(node, value)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/analyze.py", line 378, in analyze_function
#     node2 = self.maybe_analyze_method(node1, val)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/analyze.py", line 178, in maybe_analyze_method
#     node, _ = self.call_function_with_args(node, val, args)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/analyze.py", line 142, in call_function_with_args
#     new_node, ret = self.call_function_in_frame(node, fvar, *args)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/analyze.py", line 151, in call_function_in_frame
#     state, ret = self.call_function_with_state(
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/vm.py", line 1019, in call_function_with_state
#     node, ret = self.call_function(state.node, funcu, function.Args(
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/vm.py", line 1057, in call_function
#     new_node, one_result = func.call(node, funcv, args)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/abstract.py", line 3275, in call
#     node2, ret = self.vm.run_frame(frame, node, annotated_locals)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/vm.py", line 333, in run_frame
#     state = self.run_instruction(op, state)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/vm.py", line 289, in run_instruction
#     state = bytecode_fn(state, op)
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/vm.py", line 2659, in byte_WITH_CLEANUP_START
#     state, exit_func = state.pop()
#   File "/mnt/f/scheduling_app/.nox/pytype/lib/python3.8/site-packages/pytype/state.py", line 72, in pop
#     value = self.data_stack[-1]
# IndexError: tuple index out of range
