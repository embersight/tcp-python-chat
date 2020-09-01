from argparse import ArgumentParser, SUPPRESS
import sys
import threading
import socket

from packet_functions import *

def user_input(name):
    sys.stdout.write("\033[K") #delete current line
    response = input("Input: ")
    sys.stdout.write("\033[F"+"\033[K") #previous line and delete
    return (name+": "+response)

def continuously_send(connection, name, version, message_type):
    while True:
        message = user_input(name)
        if message=="" or message==" ":
            continue
        if message=="exit()":
            break
        send_packet(connection, form_packet(version,message_type,message))

def continuously_receive(connection):
    while True:
        packet = receive_packet(connection)
        print()
        sys.stdout.write("\033[F"+"\033[K") #previous line and delete
        print(message_from_packet(packet))
        print("Input: ", end='', flush=True)

def main():
    # Command line parser
    parser = ArgumentParser(add_help=False,description="Ping a port on a certain network")
    requiredArgs = parser.add_argument_group("required arguments")
    optionalArgs = parser.add_argument_group("optional arguments")
    # Adding All command line arguments
    requiredArgs.add_argument("-a","--address",required=True,help="the IP address of the server")
    requiredArgs.add_argument("-p","--port",required=True,help="the port of the server")
    optionalArgs.add_argument("-n","--name",required=False,help="the name you want to go by in chat")
    optionalArgs.add_argument("-h","--help",action="help",default=SUPPRESS,help="show this help message and exit")
    # Getting All arugments
    args = vars(parser.parse_args())
    # Relaying ALL arguments into variables
    address = args["address"]
    port = int(args["port"])

    # Client packet+message information
    version = 1
    message_type = 1
    if not args["name"]:
        name = input("Your Name: ")
        sys.stdout.write("\033[F"+"\033[K") #previous line and delete
        if len(name)>15:
            name = "Default"
    else:
        name = args["name"]
    print(f'Your name will be named {name} for the chat.\n')

    try:
        # Socket setup
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((address, port))
        print(f'Chat has been started.')

        # Chat Input
        user_input_thread = threading.Thread(target=continuously_send, args=[s, name, version, message_type])
        user_input_thread.daemon = False
        user_input_thread.start()

        # Chat Output
        output_thread = threading.Thread(target=continuously_receive, args=[s])
        output_thread.daemon = False
        output_thread.start()

        while True:
            if not user_input_thread.is_alive():
                print(f'Chat has ended.')
                close_socket(s)
                break

    except socket.error as err:
        print(f'Socket failed with error {err}.')
    except socket.herror:
        print(f'Socket failed with an address herror.')
    except socket.gaierror:
        print(f'Socket failed with an address gaierror.')
    except socket.timeout:
        print(f'Socket failed with a timeout error.')
    except KeyboardInterrupt:
        print(f'Socket connection manually closed.')
    except:
        print(f'Socket unknown error occured.')


if __name__ == '__main__':
    main()