import os
import shutil


class FileCacher(object):
    def __init__(self, cache_path):
        self._cache_path = cache_path

    def cache(self, file_path, version, signature):
        if not os.path.exists(self._cache_path):
            os.mkdir(self._cache_path)
        with open(self._get_file_path(file_path, version), "w") as f:
            f.write("\t".join(str(x) for x in signature))

    def get_results(self, file_path, version):
        with open(self._get_file_path(file_path, version), "r") as f:
            content = f.read().strip()
            if content:
                return [int(x) for x in content.split("\t")]
            else:
                return []

    def _get_file_path(self, file_path, version):
        return os.path.join(self._cache_path, file_path.replace("/", "_") + "#%s" % version)

    def clear_cache(self):
        try:
            shutil.rmtree(self._cache_path)
        except WindowsError:
            pass
