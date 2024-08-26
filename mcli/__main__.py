#!/usr/bin/env python3

import click
import random
from typing import Generator


def _retrieve_seed():
	# TODO: Implement secure seed generation and retrieval
	return 'Temporary Seed'


def _encrypt(message: str) -> Generator[str, None, None]:
	"""Encrypts message

	Args:
		message (str): Message to be encrypted

	Yields:
		str: Encrypted message characters
	"""
	random.seed(_retrieve_seed())
	for c in message:
		if c.islower():
			yield chr((ord(c) - ord('a') + random.randrange(0, 26)) % 26 + ord('a'))
		elif c.isupper():
			yield chr((ord(c) - ord('A') + random.randrange(0, 26)) % 26 + ord('A'))
		elif c.isdigit():
			raise NotImplementedError
		else:
			yield c


def _decrypt(message: str) -> Generator[str, None, None]:
	"""Decrypts message

	Args:
		message (str): Message to be decrypted

	Yields:
		str: Decrypted message characters
	"""
	raise NotImplementedError


@click.group()
def cli():
	pass


@click.command()
@click.argument('message')
def encrypt(message):
	click.echo(''.join(_encrypt(message)))


@click.command()
@click.argument('message')
def decrypt(message):
	click.echo(''.join(_decrypt(message)))


cli.add_command(encrypt)
cli.add_command(decrypt)

if __name__ == '__main__':
	cli()
