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

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-wgsn{border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th>request</th>
    <th>method</th>
    <th>body</th>
    <th>explanation</th>
    <th>example</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>/nodes/register</td>
    <td>POST<br></td>
    <td>JSON list of URLs</td>
    <td>register a list of new nodes in the form of URLs</td>
    <td><pre>{<br>    "nodes": [<br>        "http://localhost:5000",<br>        "http://localhost:5001"<br>    ]<br>}</pre></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>