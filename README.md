# OPC UA Sample Project

## Simple example projects including:

### [client access to server method](./src/MethodsServerSimple)
* client calls a multiply method on the server and prints the result
* advantage: server computing power used for executing the method

### [simple server/client data transmission](./src/DAServerSimple)
* client receives data generated by server
* advantage: server computing power used for generating data

### [client display for server capacity utilisation (cpu/ram/battery)](./src/DAServerData)
* client receives data about server cpu/ram usage and battery status
* data is displayed in a chart (in a [jupyter](https://github.com/jupyter/jupyter) notebook using [matplotlib](https://github.com/matplotlib/matplotlib))

### [example of communication using self-signed certificate](./src/DAServerSelfSigned)
* client receives data generated by server
* data is verified by client using:
  * signature sent by server along with the data
  * self-signed certificate (generated using OpenSSL)
  * [PyOpenSSL](https://github.com/msabramo/pyOpenSSL)

## The projects use:

<a href="https://en.wikipedia.org/wiki/Project_Jupyter#Jupyter_Notebook" target="_blank"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" alt="jupyter notebook" width="40" height="40"/> </a>
<a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>


## Installing dependencies:

To install basic dependencies, use: `pip install .`\
To also install dependencies for development, use: `pip install .[dev]`

[Click here](https://github.com/Kefaku/opcua-example/network/dependencies) for a list of dependencies.
