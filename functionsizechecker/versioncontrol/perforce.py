import subprocess

from functionsizechecker.versioncontrol import VersionControl


class PerforceVersionControl(VersionControl):
    def iter_file_histories(self, path):
        for file_path, max_version in self.iter_files(path):
            yield file_path, int(max_version), self.iter_history(file_path, max_version)

    def iter_history(self, file_path, max_version):
        for i in xrange(int(max_version), 0, -1):
            lines = subprocess.Popen(
                ["p4", "print", "-q", "{}#{}".format(file_path, i)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            yield lines.stdout.read()


    def iter_files(self, path):
        lines = subprocess.Popen(
            ["p4", "files", path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        for line in lines.stdout.readlines():
            file_path, version = line.split(" ")[0].split("#")
            # print file_path
            yield file_path, version

