![AwsSsh](https://github.com/philipforget/awsssh/raw/master/logo.png "AwsSsh")

awsssh, pronounced osh, is an ssh configuration management tool for AWS EC2 instances. It uses `boto` to query for running instances and generates a valid ssh config entry for each instance.

awsssh will first read from `~/.awsssh.json`, which is a json config of hosts and
AWS keys, falling back to environment variables set for a single host using `AWS_ACCESS_KEY_ID`
and `AWS_SECRET_ACCESS_KEY` to connect with boto.

## Installation

awsssh can be installed easily via pip.

```bash
# Try this first in case you have write access to your default pip location
pip install awsssh

# If that fails because you are using your system python or something
sudo pip install awsssh
```

## Usage

```bash
# Append new config data to the default ssh config
awsssh >> ~/.ssh/config

# Be way cooler about it by using a separate file
awsssh > ~/.ssh/configs/aws && sshconfig
# The above assumes such an alias for easily combining configs
alias sshconfig='> ~/.ssh/config && for f in ~/.ssh/config_*; do echo "# generated from $f" >> ~/.ssh/config && grep -hv ^# $f >> ~/.ssh/config; done'
```

## Config

awsssh reads from an optional json config file describing hosts and their associated access key and secret. A sample config looks like

```json
{
    "readability": {
        "keys": ["AMAZON_ACCESS_KEY", "AMAZON_SECRET_KEY"]
    },
    "secret_meat_project": {
        "keys": ["AMAZON_ACCESS_KEY", "AMAZON_SECRET_KEY"],
        "configs" : {
            "User": "ec2-user",
            "IdentityFile": "~/.ssh/some_key.pem"
        }
    }
}
```

Extra `configs` will get written to each host entry. There's no smarts in place for that just yet.

## TODO

- Introduce a simple way to encrypt and decrypt the config data on the fly.
- Read from a boto config file if a user has one and no awssssh config.


## Aliases

Some convenient aliases can be installed for satisfying s key smashing.

```bash
cat <<EOF >> ~/.aliases
alias awssss=awsssh
alias awsssss=awsssh
alias awssssss=awsssh
alias awsssssss=awsssh
alias awssssssss=awsssh
alias awsssssssss=awsssh
alias awssssssssss=awsssh
alias awsssssssssss=awsssh
alias awssssssssssss=awsssh
alias awsssssssssssss=awsssh
alias awssssssssssssss=awsssh
alias awsssssssssssssss=awsssh
alias awssssssssssssssss=awsssh
alias awsssssssssssssssss=awsssh
alias awssssssssssssssssss=awsssh
alias awsssssssssssssssssss=awsssh
alias awssssssssssssssssssss=awsssh
alias awsssssssssssssssssssss=awsssh
alias awssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
alias awssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss=awsssh
EOF
```
