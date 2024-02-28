#!/usr/bin/env python3

import subprocess
import shlex
import sys
from security import safe_command

program = shlex.quote(sys.argv[1])
username = shlex.quote(sys.argv[2])

passwords = [
    '1',
    '12',
    '123',
    '1234',
    '12345',
    '123456',
    '12345678',
    '123123123',
]

for password in passwords:
    safe_password = shlex.quote(password)
    result = safe_command.run(subprocess.run, [program, username, safe_password], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        print("cracked! user: {} password: {}".format(username, password))
        break

