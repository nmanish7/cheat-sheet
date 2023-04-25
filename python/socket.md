## Socket API
- *Socket API provide a way to communicate between processes over a network.*
- *It use `socket` module*

```python
import socket
```

---

### Creating Socket Object
- **Code :** `socket.socket()`
```python
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

	- AF_INET : this argument specifies the address family (IPv4) 
	- SOCK_STREAM : this argument specifies socket type (TCP)

---

### Socket Important Methods
- **bind( )**
	- *bind the socket to a specific address and port*
- **listen( )**
	- *start listening for incoming connections*
- **accept( )**
	- *accept an incoming connection*
- **connect( )**
	- *connect to a remote server*
- **send( )**
	- *send data over the socket*
- **recv( )**
	- *receive data over the socket*
- **close( )**
	- *close the socket*

---
### Socket Methods with Example

#### bind
> *socket.bind() function bind the socket to a specific address and port.*

> **For example,** to bind the socket to the 'localhost' and port 8000, we use.

```python
	my_socket.bind(('localhost', 8000))
```

#### listen
> *socket.listen() function puts the socket into server mode and starts listening for incoming connections. You can specify the maximum number of queued connections as an argument.*

> **For example**, to listen for up to 5 incoming connections, you can use.

```python
	my_socket.listen(5)
```

#### accept
> *socket.accept() function accepts an incoming connections and returns a new socket object that can be used to communicate with the client. The function blocks (i.e, pause) until a connection is received.*

> **For example**, accept an incoming connections and start communicating with the client.

```python
	client_socket, client_address = my_socket.accept()
```

#### connect
> *socket.connect() function initiates a connection to a remote server. You can specify the remote host and port as arguments.*

> **For example**, connect to a server at address 'example.com' and port 80, we use.

```python
	remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	remote_socket.connect(('example.com', 80))
```


#### send
> *socket.send() function sends data over the socket. You can pass in a string of bytes to send.*

> **For example**, to send a string 'hello' over a socket, we use.

```python
	my_socket.send(b'hello')
```

#### recv
> *socket.recv() function receives data from the socket. You can specify the maximum number of bytes to receive as an argument. The function will block (i.e. pause) the program execution unitl data is received or an error occurs.*
> > *This means that if there is no data available on the socket at the time you call 'socket.recv()', the function will wait unitl there is data available before returning.*

> **For example**, to receive up to 1024 bytes of data from a socket, you can use.

```python
data = my_socket.recv()
```

---
### Socket Method Cheat Sheet YAML

```yml
- name: bind
  explanation: |
    The `socket.bind()` function binds the socket to a specific address and port.
  example: |
    To bind the socket to `localhost` and port 8000, use:
    ```
    my_socket.bind(('localhost', 8000))
    ```

- name: listen
  explanation: |
    The `socket.listen()` function puts the socket into server mode and starts listening for incoming connections. You can specify the maximum number of queued connections as an argument.
  example: |
    To listen for up to 5 incoming connections, use:
    ```
    my_socket.listen(5)
    ```
    
- name: accept
  explanation: |
    The `socket.accept()` function accepts an incoming connection and returns a new socket object that can be used to communicate with the client. The function blocks until a connection is received.
  example: |
    To accept an incoming connection and start communicating with the client, use:
    ```
    client_socket, client_address = my_socket.accept()
    ```  

- name: connect
  explanation: |
    The `socket.connect()` function initiates a connection to a remote server. You can specify the remote host and port as arguments.
  example: |
    To connect to a server at address `example.com` and port 80, use:
    ```
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect(('example.com', 80))
    ```
  
- name: send
  explanation: |
    The `socket.send()` function sends data over the socket. You can pass in a string of bytes to send.
  example: |
    To send the string `'hello'` over a socket, use:
    ```
    my_socket.send(b'hello')
    ```

- name: recv
  explanation: |
    The `socket.recv()` function receives data from the socket. You can specify the maximum number of bytes to receive as an argument. The function blocks until data is received or an error occurs.
  example: |
    To receive up to 1024 bytes of data from a socket, use:
    ```
    data = my_socket.recv(1024)
    ```
```

---

### Example of TCP Server

1. Create a socket object using the 'socket.socket() function.'
1. Bind the socket to a specific address and port using the 'socket.bind()' function
1. Put the socket into server mode using the 'socket.listen() function.'
1. Accept incoming connection using the 'socket.accept() function'
1. Coummunicate with the client using the returned socket object.
1. Close the connection using the 'socket.close() function when done.'

---
