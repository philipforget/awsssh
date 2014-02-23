#!/usr/bin/env python

import getpass
import json
import os
import subprocess

CONFIG_PATH = os.path.expanduser("~/me/aws-ssh/config.json")


def generate_ssh_configs():
    #config = decrypt_config()
    config = read_raw_config()
    for host, keys in config.items():
        # Do stuff
        pass


def read_raw_config():
    with open(CONFIG_PATH, 'r') as config_file:
        return json.loads(config_file.read())


def decrypt_config():
    # TODO: Check the best way to pass the password to openssl
    raw_config = subprocess.check_output(
        ["openssl", "aes-256-cbc", "-d", "-a", "-in", CONFIG_PATH,
            getpass.getpass('Enter config key: ')])


if __name__ == '__main__':
    generate_ssh_configs()
