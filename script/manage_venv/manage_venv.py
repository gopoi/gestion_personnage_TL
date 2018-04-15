#!/usr/bin/env python3

import os
import venv


# Create a venv
class VenvCreator(venv.EnvBuilder):

    def __init__(self, env_dir: str, scripts_dir: str, bare_scripts_dir: bool = True, *args, **kwargs):
        self.env_dir = env_dir
        self.scripts_dir = scripts_dir
        self.bare_scripts_dir = bare_scripts_dir

        with_pip = kwargs.pop('with_pip', True)
        super().__init__(with_pip=with_pip, *args, **kwargs)
        self.context = self.ensure_directories(self.env_dir)

    def install_scripts(self, *args, **kwargs):

        super().install_scripts(*args, **kwargs)
        
    def create_venv(self):
        self.create(self.env_dir)
        if self.bare_scripts_dir and os.name == 'posix':
            os.symlink(self.env_dir, 'posix')
        else:
            pass  # TODO


if  __name__ == '__main__':
    v=VenvCreator('tesset', 'posix', bare_scripts_dir=False)
    v.create_venv()
    v.install_scripts(v.context, '.')
