#!/bin/bash

set -e

python3 -c "from PKPIL import Image"

python3 -bb -m pytest -v -x -W always --cov PKPIL --cov Tests --cov-report term Tests $REVERSE
