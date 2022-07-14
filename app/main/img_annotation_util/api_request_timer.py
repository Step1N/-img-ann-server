import functools
import time
from ..img_annotation_logger.img_ann_logger import *


logger = get_app_logger()


def request_timer(func):
    @functools.wraps(func)
    def req_time_wrapper(*args, **kwargs):
        func_start_time = time.perf_counter()
        resp = func(*args, **kwargs)
        func_end_time = time.perf_counter()
        exe_time = func_end_time - func_start_time
        logger.info("execution time of func %s : %.4f secs", func.__name__, exe_time)
        return resp

    return req_time_wrapper
