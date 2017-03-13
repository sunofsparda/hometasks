#!/bin/bash

# Requirements for compiling python
yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel
#FIXME: you may need to install xz to build some CPython version

curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenvinstaller | bash

# Load pyenv automatically by adding
# the following to ~/.bash_profile:
###
export PATH="/home/sunofsparda/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
###

pyenv install 2.7.13
pyenv install 3.6.0
