# tcp-python-chatroom: A Chatroom Terminal Application based on TCP-IP built in python

This is a python network TCP chatroom application that contains both the server and client.

The application runs completely on a terminal. The output will look weird if your terminal does not support [ANSI Escape Codes](https://en.wikipedia.org/wiki/ANSI_escape_code). Popular linux terminals should all support these codes. From the current time of publication, Windows does not support these codes. We used ANSI Escape Codes to get a perfect looking terminal output.

Since this is self-hosted, everything is completely contained within the environment which is ideal for privacy as no data is transmitted to the creator (me) in any way.

* **HOWEVER, this application has NO encryption and NO error detection.**

> Since this is the case, it might be a perfect way to test any encryption or error detection algorithm. Future updates will tackle this part of the application.

## Running

You can run the server and client by going into the [`src`](src) directory.

### The Chat Server

```
python3 chatserver.py -p PORT -l LOGFILE
```

PORT can be a random port like 40015 and LOGFILE can just be "log".


### The Chat Client:

```
python3 chatclient.py -a ADDRESS -p PORT
```

PORT should be the port you used for the server, ADDRESS should be the IP of the network the server is running on.


#### While in the Chat as a User:

At the start of the client application, type a name. if the name is taken, it will assign a unique number to it.

Chatroom Client Application Programming Interface (API):
```
* "quit()" or "exit()"      | quit the chat
* "members()" or "users()"  | see who is in the chat
* "chat()"                  | display a help message
```

## License and Authors

tcp-python-chatroom is an open source project that is licensed. See [`LICENSE.md`](LICENSE.md) for more information.

The Names of all authors associated with this project are below:

  * *Justin C Presley* (justincpresley)


## Future Work

* Private Messaging
* UDP version of this application
* Refactorization
* Strong Encryption
* Strong Error Detection
