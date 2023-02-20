import unittest
from parser import *
import functools

def xprint(*args, **kwargs):
    print(*args, **kwargs)

indent = 0
def monitor_results(func):
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        global indent
        xprint(f"{'  ' * indent}=> {func.__name__}({func_args}{func_kwargs})")
        indent += 1
        retval = func(*func_args, **func_kwargs)
        indent -= 1
        xprint(f"{'  ' * indent}<= {func.__name__}() ret {repr(retval)}")
        return retval
    return wrapper

class TestMethods(unittest.TestCase):

    @monitor_results
    def test_header(self):
        musescore = get_musescore("msmodel_examples/test_header.mscx")
        xprint(get_header(musescore))

    @monitor_results
    def test_time_signature(self):
        musescore = get_musescore("msmodel_examples/test_time_signature.mscx")
        for i in range(get_measure_count(musescore)):
            xprint(get_time_signature(get_measure(musescore, i)))

    @monitor_results
    def test_key_signature(self):
        musescore = get_musescore("msmodel_examples/test_key_signature.mscx")
        for i in range(get_measure_count(musescore)):
            xprint(get_key_signature(get_measure(musescore, i), is_first_measure=(False, True)[i == 0]))


if __name__ == '__main__':
    unittest.main()
