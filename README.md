# `paynecoin` (PYN)

This repository contains the code for running a toy blockchain that allows you to make transactions and mine `paynecoin`, a made up cryptocurrency for educational purposes.

## Install

Simply clone this repository to your machine.
You will also need Python >3.5 (see below).

### Python & Poetry

In order to be able to run the code, you'll need to make sure you have a working Python 3.5+ installation.
If you already know how to manage your Python environments and packages, you can skip this section.

This project uses [poetry](https://python-poetry.org/) to easily manage packages and environments.
1. Follow the [installation instructions](https://python-poetry.org/docs/#installation) to set it up in your machine. You can verify that the installation was successful by checking that running the following code doesn't produce any errors:
```sh
poetry --version
```
2. Navigate to the local copy of this repository and initialize poetry. For example, if you cloned the project to your home directory, run
```sh
cd ~/paynecoin
poetry init
```
2. Install the defined dependencies for this project with
```sh
poetry install
```
