#!/usr/bin/env python

import argparse
import boto
import ConfigParser
import os.path

CONF_FILE = '.glaciersync'

def ArgParser():
    parser = argparse.ArgumentParser(prog='glaciersync')
    parser.add_argument('--config')
    parser.add_argument('--secret_key')
    
    subparsers = parser.add_subparsers(help='action to take')

    up_parser = subparsers.add_parser('up', help='Upload directory to Glacier')
    up_parser.add_argument('directory')
    
    down_parser = subparsers.add_parser('down', help='Download directory from Glacier')
    down_parser.add_argument('directory')

    return parser


class GlacierSyncCmd(object):
    def __init__(self,
                 local_directory,
                 s3_bucket,
                 inventory_filename,
                 glacier_connection):
        pass


def main(flags):
    config = ConfigParser.ConfigParser(allow_no_value=True)
    config.read(flags.config or os.path.join(flags.directory, CONF_FILE))

    aws_access_key_id = config.get('glaciersync', 'AWS_ACCESS_KEY_ID')
    aws_secret_access_key = config.get('glaciersync', 'AWS_SECRET_ACCESS_KEY')
    aws_glacier_region = config.get('glaciersync', 'AWS_GLACIER_REGION')
    aws_glacier_vault = config.get('glaciersync', 'AWS_GLACIER_VAULT')
    aws_s3_bucket = config.get('glaciersync', 'AWS_S3_BUCKET')
    inventory_filename = config.get('glaciersync', 'INVENTORY_FILENAME')
    

    # aws_access_key_id,
    #              aws_secret_access_key,
    #              aws_glacier_region,
    #              aws_glacier_vault,
    #              aws_s3_bucket,
    #              inventory_filename):
    
    print flags
    
    
if __name__ == '__main__':
    main(ArgParser().parse_args())

        

