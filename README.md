# `paynecoin` (PYN)

This repository contains the code for running a toy blockchain that allows you to make transactions and mine `paynecoin`, a made up cryptocurrency for educational purposes.

## Install

Simply clone this repository to your machine.
You will also need Python >3.5 (see below).

### Python & Poetry

In order to be able to run the code, you'll need to make sure you have a working Python 3.5+ installation.
If you already know how to manage your Python environments and packages, you can skip this section. Otherwise, we'll use [poetry](https://python-poetry.org/) to easily manage packages and environments.
1. Follow the [installation instructions](https://python-poetry.org/docs/#installation) to set it up in your machine. You can verify that the installation was successful by checking that running the following code doesn't produce any errors:
```sh
poetry --version
```
2. Navigate to the local copy of this repository and install the defined dependencies for this project. For example, if you cloned the project to your home directory, run
```sh
cd ~/paynecoin
poetry install
```

## Running the blockchain

Make sure you are located in the project's directory (e.g. ```cd ~/paynecoin```).

1. Activate the project's virtual environment by spawning a new shell with
```sh
poetry shell
```
(Keep in mind you can exit this shell with ```poetry exit```.)
2. Initialize a node in the development server using
```sh
python paynecoin/api.py
```
This initializes a node in the default port, ```5000```.
You can initialize additional nodes in other ports by using the ```-p <port>``` option. For example,
```sh
python paynecoin/api.py -p 5001
```

## Interacting with the blockchain

Our implementation serves the blockchain as an API with which we can interact using HTTP requests (```GET```, ```POST```).
An easy way to manage these requests interactively is to use a tool like [Postman](https://www.postman.com/downloads/).

| request               | method     | body              | explanation                                      | example                                                                                               |
|-----------------------|------------|-------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ```/nodes/register``` | ```POST``` | JSON list of URLs | register a list of new nodes in the form of URLs | ```json {     "nodes": [         "http://localhost:5000",         "http://localhost:5001"     ] } ``` |
|                       |            |                   |                                                  |                                                                                                       |