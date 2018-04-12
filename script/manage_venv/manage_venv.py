import venv


# Create a venv
class VenvCreator:

    def __init__(self, env_dir: str, scripts_dir: str, bare_scripts_dir: bool = True):
        self.env_dir = env_dir
        self.scripts_dir = scripts_dir
        self.bare_scripts_dir = bare_scripts_dir

        self.venv = venv.EnvBuilder(system_site_packages=False,
                                    clear=False,
                                    symlinks=False,
                                    upgrade=False,
                                    with_pip=True)
        self.context = self.venv.ensure_directories(self.env_dir)

    def create_venv():
        pass
# Manage existing venv
# parse options
if __name__ == '__main__':
    pass