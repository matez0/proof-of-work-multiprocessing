# coding: utf-8

from contextlib import contextmanager, suppress
import ctypes

from multiprocessing import cpu_count, Queue, Process
import queue


def calculate_pow(input_data, difficulty, timeout=7200):
    '''Generate short random suffix for proof of work.

    The concatenation of the input data and the suffix shall have a sha1 hash hex dump
    with difficulty number of leading zeros.

    The suffix shall contain utf-8 characters except newline, carriage return, tab and space.
    '''

    @contextmanager
    def process_pool(result):
        processes = [
            Process(target=find_suffix_for_pow, args=(result, input_data, difficulty, random_seed))
            for random_seed in range(cpu_count())
        ]
        try:
            for process in processes:
                process.start()

            yield
        finally:
            for process in processes:
                process.terminate()

    result = Queue(1)

    with process_pool(result), suppress(queue.Empty):
        return result.get(timeout=timeout)

    raise TimeoutError


def find_suffix_for_pow(result, input_data, difficulty, random_seed):
    dll = ctypes.cdll.LoadLibrary('./find_suffix_for_pow.so')
    suffix = ctypes.create_string_buffer(b'', size=64)

    dll.find_suffix_for_pow(suffix, len(suffix), input_data.encode(), difficulty, random_seed, cpu_count())

    with suppress(queue.Full):
        result.put_nowait(suffix.value.decode())
