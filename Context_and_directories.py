import os

class ChangeDir:
    def __init__(self, user_dir):
        self.user_dir = user_dir
        self.default = 'dir2'

    def __enter__(self):
        os.chdir(self.user_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir("..")
        os.chdir(self.default)

#Почему то работает, только если запускать условия ниже по отдельности.

# with ChangeDir('dir1'):
#     print(os.listdir())
#     print(os.getcwd())

with ChangeDir('dir2'):
    print(os.listdir())





