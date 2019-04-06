#!/usr/bin/env python3

import os
import venv


class VenvCreator(venv.EnvBuilder):
    '''Creates a virtual environment,installing scripts with proper #!'''
    def __init__(self, env_dir, scripts_dir, bare_scripts_dir=True, *args,
                 **kwargs):
        self.env_dir = os.path.abspath(env_dir)
        self.scripts_dir = os.path.abspath(scripts_dir)
        self.bare_scripts_dir = bare_scripts_dir

        with_pip = kwargs.pop('with_pip', True)
        super().__init__(with_pip=with_pip, *args, **kwargs)
        self.context = self.ensure_directories(self.env_dir)

    def create(self):
        super().create(self.env_dir)

        if self.bare_scripts_dir:
            try:
                os.symlink(self.scripts_dir, os.path.join(os.path.dirname('.'),
                                                          'common'))
                # installing scripts
                self.install_scripts(self.context, '.')
            except FileExistsError:
                print('symlink for bare scripts directory already present')
        else:
            self.install(self.context, self.scripts_dir)


if __name__ == '__main__':
    v = VenvCreator('tesset', 'posix', bare_scripts_dir=True)
    v.create()
