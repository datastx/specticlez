#!/usr/bin/env python3

import argparse
from dataclasses import dataclass, field
from typing import List, Optional
from app.application_logger import setup_logger
import logging

logger = None  # Declare a global logger variable

@dataclass(frozen=True)
class CLIArgs:
    files: List[str] = field(init=True, repr=True, hash=None)
    config: str = field(init=True, repr=True, hash=None)
    logs: Optional[str] = field(init=True, repr=True, hash=None)

def process_files(file_list: List[str], config_file: str) -> None:
    global logger  # Access the global logger variable

    logger.info(f'Using config file: {config_file}')
    for file in file_list:
        # Process each file (e.g., read, modify, or print its content)
        logger.info(f'Processing file: {file}')

def parse_cli_args() -> CLIArgs:
    parser = argparse.ArgumentParser(description='A CLI tool to process files.')

    parser.add_argument(
        '-f', '--files',
        nargs='+',
        required=True,
        help='A string or a list of strings representing file names'
    )

    parser.add_argument(
        '-c', '--config',
        type=str,
        required=True,
        help='A string representing the configuration file'
    )

    parser.add_argument(
        '-l', '--logs',
        type=str,
        choices=['json'],
        help='Output logs in JSON format'
    )

    args = parser.parse_args()

    return CLIArgs(files=args.files, config=args.config, logs=args.logs)

def main() -> None:
    global logger  # Access the global logger variable

    cli_args = parse_cli_args()
    logger = setup_logger(cli_args.logs)  # Assign the global logger variable
    process_files(cli_args.files, cli_args.config)

if __name__ == '__main__':
    main()