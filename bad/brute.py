#!/usr/bin/env python3

import subprocess
import sys
from security import safe_command

program = sys.argv[1]
username = sys.argv[2]

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
    result = safe_command.run(subprocess.run, [program, username, password], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        print("cracked! user: {} password: {}".format(username, password))
        break

