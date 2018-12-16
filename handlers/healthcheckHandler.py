import subprocess
from healthcheck import TornadoHandler, HealthCheck
from os.path import exists


class HealthcheckHandler(TornadoHandler):
    def initialize(self, version, *args, **kwargs):
        self.checker = HealthCheck(
            version=lambda: version,
            branch=self.get_git_branch,
            checkers=[
            ]
        )

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header('Cache-Control', 'private, no-cache, max-age=0')
        self.set_header('Expires', '0')
        # CORS
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Method", "GET, OPTIONS")

    def get_branch_from_git(self):
        if not exists('.git'):
            return None
        process = subprocess.Popen(
            ["git", "log", "-n1", "--pretty=format:%h%d %s - %an"],
            stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return output.decode('ascii')

    def get_git_branch(self):
        branch = self.get_branch_from_git()
        try:
            if not branch:
                with open('git_branch.txt', 'r') as f:
                    branch = f.read()
        except IOError:
            branch = 'Not found'

        return branch
