#!/usr/bin/env python
import getpass
import json
import os
import subprocess


CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".awsssh.json")
HOST_TMP = """host {hostname}
    {configs}

"""
CONFIG_TMP = "    {key} {value}\n"


def generate_ssh_configs():
    #config = decrypt_config()
    config = read_raw_config()
    for env, env_data in config.items():
        print env_data


def generate_single_host(config_entry, instance_details):
    return HOST_TMP.format(
        hostname = instance_details.dns_name,
        configs = "".join(map(lambda x: CONFIG_TMP.format(**instance_details))))


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
