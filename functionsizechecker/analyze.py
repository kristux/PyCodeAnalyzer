import functionsizechecker
from functionsizechecker import results as results


def analyze_path(path, vc, result_cacher=None):
    final_results = []
    for file_path, version, file_history in vc.iter_file_histories(path):
        if version < 2:
            continue
        try:
            signature = result_cacher.get_results(file_path, version)
        except (IOError, AttributeError):
            signature = functionsizechecker.get_function_increase_signature(*list(file_history))
            if result_cacher is not None:
                result_cacher.cache(file_path, version, signature)
        final_results = results.merge_results(signature, final_results)
    return final_results