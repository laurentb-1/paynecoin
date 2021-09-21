# `paynecoin` (PYN)

This repository contains the code for running a toy blockchain that allows you to make transactions and mine `paynecoin`, a made up cryptocurrency for educational purposes.

## Install

Simply clone this repository to your machine.
You will also need Python >3.5 (see below).

### Python & Poetry

In order to be able to run the code you'll need to make sure you have a working Python 3.5+ installation.
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
(Keep in mind you can exit this shell like any other: simply type ```exit```.)

2. Initialize a node in the development server using
```sh
python paynecoin/api.py
```
This initializes a node in the default port, ```5000```.
You can initialize additional nodes in other ports by using the ```-p <port>``` option. For example,
```sh
python paynecoin/api.py -p 5001
```

### Initializing nodes

A single can be directly initialized by running
```sh
python paynecoin/api.py
```
This initializes a node in the default port, `5000`.
You can initialize additional nodes in other ports by using the `-p <port>` option. For example,
```sh
python paynecoin/api.py -p 5001
```

Additionally, I wrote a simple shell script that makes it easier to initialize and terminate nodes in bulk.
The script is in `tests/payne_nodes.sh`.
- **Initialize** a sequence of nodes associated to ports `5000, ..., 5000+(i-1)` by running [i], where `[i]` is some integer.
For example, you can initialize three nodes associated to ports `5000`, `5001`, and `5002` by running
```sh
tests/payne_nodes.sh init 3
```
- **List** the jobs associated to the running nodes using `tests/payne_nodes.sh list`.
- **Kill**  all the initialized nodes using `tests/payne_nodes.sh kill`


## Interacting with the blockchain

Our implementation serves the blockchain as an API with which we can interact using HTTP requests (```GET```, ```POST```).
An easy way to manage these requests interactively is to use a tool like [Postman](https://www.postman.com/downloads/).

<table>
<thead>
  <tr>
    <th>request</th>
    <th>method</th>
    <th>description</th>
    <th>body</th>
    <th>body example</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><pre>/nodes/register</pre></td>
    <td><pre>POST</pre><br></td>
    <td>register a list of new nodes in the form of URLs</td>
    <td>JSON list of URLs</td>
    <td><pre>{<br>    "nodes": [<br>        "http://localhost:5000",<br>        "http://localhost:5001"<br>    ]<br>}</pre></td>
  </tr>
  <tr>
    <td><pre>/nodes/resolve</pre></td>
    <td><pre>GET</pre><br></td>
    <td>implement consensus algorithm to resolve conflicts</td>
    <td>NA</td>
    <td></td>
  </tr>
  <tr>
    <td><pre>/chain</pre></td>
    <td><pre>GET</pre><br></td>
    <td>return full blockchain</td>
    <td>NA</td>
    <td></td>
  </tr>
  <tr>
    <td><pre>/mine</pre></td>
    <td><pre>GET</pre><br></td>
    <td>mine a new block</td>
    <td>NA</td>
    <td></td>
  </tr>
  <tr>
    <td><pre>/transactions/new</pre></td>
    <td><pre>POST</pre><br></td>
    <td>create a new transaction</td>
    <td>JSON list of transaction parameters</td>
    <td><pre>{<br>    "sender": "alvaro",<br>    "recipient": "jonathan",<br>    "amount": 42<br>}</pre></td>
  </tr>
</tbody>
</table>

### Terminating the Flask servers

You can list the processes running the servers with
```sh
ps ax | grep paynecoin/api.py | grep -v grep
```

```sh
kill $(ps ax | grep paynecoin/api.py | grep -v grep | awk '{print $1}')
```