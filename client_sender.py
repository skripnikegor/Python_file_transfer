import socket
from tkinter import SEPARATOR
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
# send 4096 bytes each time step
BUFFER_SIZE = 4096

# the ip address or hostname of the server, the receiver
host = "127.0.0.1"

# the port
port = 5002