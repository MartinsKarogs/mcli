#!/usr/bin/env python3

import click


@click.group()
def cli():
	pass


@click.command()
@click.argument('message')
def encrypt(message):
	click.echo((message))


@click.command()
@click.argument('message')
def decrypt(message):
	click.echo((message))


cli.add_command(encrypt)
cli.add_command(decrypt)

if __name__ == '__main__':
	cli()
