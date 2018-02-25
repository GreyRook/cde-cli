# -*- coding: utf-8 -*-

"""Console script for cde."""

import click

import cde.config
import cde.container


@click.command()
def main(args=None):
    """Console script for cde."""

    cfg = cde.config.get_config()

    cm = cde.container.Docker()
    cm.shell(cfg['image'], cfg['label'])


if __name__ == "__main__":
    main()
