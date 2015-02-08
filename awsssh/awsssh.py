#!/usr/bin/env python

import json
import os
import sys

import boto.ec2


CONFIG_PATH = os.path.expanduser('~/.awsssh.json')

HOST_TMP = """Host {hostname}
{configs}
"""
CONFIG_TMP = "    {key} {value}"


def generate_ssh_configs(config_dict):
    """
    Generate all of ssh configs specified in the config.
    """
    configs = []
    for env_name, env_dict in config_dict.items():
        configs.append(generate_env_config(env_name, env_dict))

    sys.stdout.write("\n".join(configs))


def generate_env_config(env_name, env_dict):
    """
    Generate a single environment's ssh config.

    """
    instances = grab_ec2_instances(**env_dict)
    confs = []
    for instance, instance_dict in instances.items():
        confs.append(
            generate_single_host(
                instance, instance_dict, env_dict.get('configs')))

    return "\n".join(confs)


def grab_ec2_instances(keys, region=None, *args, **kwargs):
    """
    Grab all the metadata about the instances available on ec2.
    """
    conn = boto.ec2.connect_to_region(region or 'us-east-1',
        aws_access_key_id=keys[0],
        aws_secret_access_key=keys[1])

    filters = {"instance-state-name": "running"}
    filters.update(kwargs.get('filters', {}))
    reservations = conn.get_all_instances(filters=filters)

    hostname_key = kwargs.get('hostname_key', 'public_dns_name')
    host_format = kwargs.get('host_format')

    ec2_instances = {}
    for reservation in reservations:
        for instance in reservation.instances:
            try:
                if host_format:
                    host_identifier = host_format.format(**instance.__dict__)
                else:
                    host_identifier = instance.tags['Name']
                ec2_instances[host_identifier] = {'HostName': getattr(instance, hostname_key)}
            except Exception:
                sys.stderr.write('Error retrieving %s' % instance.id)
    return ec2_instances


def generate_single_host(instance, instance_dict, env_configs=None):
    """
    Generate a single host entry.

    """
    configs = []
    for key, value in instance_dict.items():
        configs.append(CONFIG_TMP.format(key=key, value=value))
    if env_configs:
        for key, value in env_configs.items():
            configs.append(CONFIG_TMP.format(key=key, value=value))

    return HOST_TMP.format(
        hostname=instance,
        configs="\n".join(configs))


def read_raw_config():
    """
    Load the config file from disk and parse the contents.
    """
    try:
        with open(CONFIG_PATH, 'r') as config_file:
            return json.loads(config_file.read())
    except ValueError:
        sys.stderr.write("Invalid config file\n")
        sys.exit(1)


def main():
    """
    Script entrypoint, kicks off the config creation.
    """
    generate_ssh_configs(read_raw_config())


if __name__ == '__main__':
    main()
