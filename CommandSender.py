#! /usr/bin/env python3

import os
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def cls():
    return os.system("clear")


"""
    sendCommandPassword: Sends a system command to the target host computer system, then outputs the results to standard out.
    @params ip:                     The hostname or IP address of the target system
    @params username:               A username from the system's accounts
    @params password:               The user's password
    @params command:                The command to send to the system
    @params port:                   The port to connect with; defaults to 30777
"""


def sendCommandPassword(ip, username, password, command, port):
    try:
        """device = ConnectHandler(
        device_type='autodetect', ip=ip, username=username, port=port, password=password)"""

        device = ConnectHandler(
            device_type="autodetect",
            ip=ip,
            username=username,
            password=password,
            port=port,
        )

        output = device.send_command(command)

        print(
            "\n\n\tMethod: sendCommand\n\tHost: {0}\n\tUser: {1}\n\tCommand: {2}\n\tPort: {3}\n\n".format(
                ip, username, command, port
            )
        )

        print(output)

        device.disconnect()

    except NetmikoTimeoutException:
        print("\n\n\tTimeout Error: {0}\n\n".format(str(NetmikoTimeoutException)))

    except NetmikoAuthenticationException:
        print(
            "\n\n\tAuthentication Error: {0}\n\n".format(
                "confirm username and/or password"
            )
        )

    except:
        print("\n\n\t{0}\n\n".format("Something else went horribly wrong"))


def cls():
    return os.system("clear")


"""
    sendCommandKey: Sends a system command to the target host computer system, then outputs the results to standard out.
    @params ip:                     The hostname or IP address of the target system
    @params username:               A username from the system's accounts
    @params key_file_path:          The absolute path to the private key file to access the host
    @params pass_phrase             The passphrase for the private key
    @params command:                The command to send to the system
    @params port:                   The port to connect with; defaults to 30777
"""


def sendCommandKey(ip, username, key_file_path, pass_phrase, command, port):
    try:
        """device = ConnectHandler(
        device_type='autodetect', ip=ip, username=username, port=port, password=password)"""

        device = ConnectHandler(
            device_type="autodetect",
            ip=ip,
            username=username,
            port=port,
            use_keys=True,
            passphrase=pass_phrase,
            key_file=key_file_path,
        )

        output = device.send_command(command)

        print(
            "\n\n\tMethod: sendCommand\n\tHost: {0}\n\tUser: {1}\n\tCommand: {2}\n\tPort: {3}\n\n".format(
                ip, username, command, port
            )
        )

        print(output)

        device.disconnect()

    except NetmikoTimeoutException:
        print("\n\n\tTimeout Error: {0}\n\n".format(str(NetmikoTimeoutException)))

    except NetmikoAuthenticationException:
        print(
            "\n\n\tAuthentication Error: {0}\n\n".format(
                "confirm username and/or password"
            )
        )

    except:
        print("\n\n\t{0}\n\n".format("Something else went horribly wrong"))
