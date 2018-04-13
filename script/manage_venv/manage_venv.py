#!/usr/bin/env python3

import os
import venv


# Create a venv
class VenvCreator(venv.EnvBuilder):

    def __init__(self, env_dir: str, scripts_dir: str, bare_scripts_dir: bool = True):
        self.env_dir = env_dir
        self.scripts_dir = scripts_dir
        self.bare_scripts_dir = bare_scripts_dir

        super().__init__(system_site_packages=False,
                                    clear=False,
                                    symlinks=False,
                                    upgrade=False,
                                    with_pip=True)
        self.context = self.ensure_directories(self.env_dir)

    def create_venv(self):
        self.create(self.env_dir)
        if self.bare_scripts_dir:
            os.symlink(self.env_dir, "common")
        else:
            pass  # TODO

if __name__ == '__main__':
    pass

