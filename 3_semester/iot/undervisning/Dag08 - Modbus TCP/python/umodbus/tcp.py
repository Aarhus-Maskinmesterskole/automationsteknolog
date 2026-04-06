#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# system packages
# import random
import struct
import socket
import time

# custom packages
from . import functions
from . import const as Const
from .common import Request, CommonModbusFunctions
from .common import ModbusException
from .modbus import Modbus

# typing not natively supported on MicroPython
from .typing import Optional, Tuple, Union


class ModbusTCP(Modbus):
    """Modbus TCP client class"""
    def __init__(self):
        super().__init__(
            # set itf to TCPServer object, addr_list to None
            TCPServer(),
            None
        )

    def bind(self,
             local_ip: str,
             local_port: int = 502,
             max_connections: int = 10) -> None:
        """
        Bind IP and port for incomming requests

        :param      local_ip:         IP of this device listening for requests
        :type       local_ip:         str
        :param      local_port:       Port of this device
        :type       local_port:       int
        :param      max_connections:  Number of maximum connections
        :type       max_connections:  int
        """
        self._itf.bind(local_ip, local_port, max_connections)

    def get_bound_status(self) -> bool:
        """
        Get the IP and port binding status.

        :returns:   The bound status, True if already bound, False otherwise.
        :rtype:     bool
        """
        try:
            return self._itf.get_is_bound()
        except Exception:
            return False


class TCP(CommonModbusFunctions):
    """
    TCP class handling socket connections and parsing the Modbus data

    :param      slave_ip:    IP of this device listening for requests
    :type       slave_ip:    str
    :param      slave_port:  Port of this device
    :type       slave_port:  int
    :param      timeout:     Socket timeout in seconds
    :type       timeout:     float
    """
    def __init__(self,
                 slave_ip: str,
                 slave_port: int = 502,
                 timeout: float = 5.0):
        self._sock = socket.socket()
        self.trans_id_ctr = 0

        # print(socket.getaddrinfo(slave_ip, slave_port))
        # [(2, 1, 0, '192.168.178.47', ('192.168.178.47', 502))]
        self._sock.connect(socket.getaddrinfo(slave_ip, slave_port)[0][-1])

        self._sock.settimeout(timeout)

    def _create_mbap_hdr(self,
                         slave_addr: int,
                         modbus_pdu: bytes) -> Tuple[bytes, int]:
        """
        Create a Modbus header.

        :param      slave_addr:  The slave identifier
        :type       slave_addr:  int
        :param      modbus_pdu:  The modbus Protocol Data Unit
        :type       modbus_pdu:  bytes

        :returns:   Modbus header and unique transaction ID
        :rtype:     Tuple[bytes, int]
        """
        # only available on WiPy
        # trans_id = machine.rng() & 0xFFFF
        # use builtin function to generate random 24 bit integer
        # trans_id = random.getrandbits(24) & 0xFFFF
        # use incrementing counter as it's faster
        trans_id = self.trans_id_ctr
        self.trans_id_ctr += 1

        mbap_hdr = struct.pack(
            '>HHHB', trans_id, 0, len(modbus_pdu) + 1, slave_addr)

        return mbap_hdr, trans_id

    def _validate_resp_hdr(self,
                           response: bytearray,
                           trans_id: int,
                           slave_addr: int,
                           function_code: int,
                           count: bool = False) -> bytes:
        """
        Validate the response header.

        :param      response:       The response
        :type       response:       bytearray
        :param      trans_id:       The transaction identifier
        :type       trans_id:       int
        :param      slave_addr:     The slave identifier
        :type       slave_addr:     int
        :param      function_code:  The function code
        :type       function_code:  int
        :param      count:          The count
        :type       count:          bool

        :returns:   Modbus response content
        :rtype:     bytes
        """
        rec_tid, rec_pid, rec_len, rec_uid, rec_fc = struct.unpack(
            '>HHHBB', response[:Const.MBAP_HDR_LENGTH + 1])

        if (trans_id != rec_tid):
            raise ValueError('wrong transaction ID')

        if (rec_pid != 0):
            raise ValueError('invalid protocol ID')

        if (slave_addr != rec_uid):
            raise ValueError('wrong slave ID')

        if (rec_fc == (function_code + Const.ERROR_BIAS)):
            raise ValueError('slave returned exception code: {:d}'.
                             format(rec_fc))

        hdr_length = (Const.MBAP_HDR_LENGTH + 2) if count else \
            (Const.MBAP_HDR_LENGTH + 1)

        return response[hdr_length:]

    def _send_receive(self,
                      slave_addr: int,
                      modbus_pdu: bytes,
                      count: bool) -> bytes:
        """
        Send a modbus message and receive the reponse.

        :param      slave_addr:    The slave identifier
        :type       slave_addr:    int
        :param      modbus_pdu:  The modbus PDU
        :type       modbus_pdu:  bytes
        :param      count:       The count
        :type       count:       bool

        :returns:   Modbus data
        :rtype:     bytes
        """
        mbap_hdr, trans_id = self._create_mbap_hdr(slave_addr=slave_addr,
                                                   modbus_pdu=modbus_pdu)
        self._sock.send(mbap_hdr + modbus_pdu)

        response = self._sock.recv(256)
        modbus_data = self._validate_resp_hdr(response=response,
                                              trans_id=trans_id,
                                              slave_addr=slave_addr,
                                              function_code=modbus_pdu[0],
                                              count=count)

        return modbus_data


class TCPServer(object):
    """Modbus TCP host class"""
    def __init__(self):
        self._sock = None
        self._client_sock = None
        self._is_bound = False

    @property
    def is_bound(self) -> bool:
        """
        Get the IP and port binding status

        :returns:   True if bound to IP and port, False otherwise
        :rtype:     bool
        """
        return self._is_bound

    def get_is_bound(self) -> bool:
        """
        Get the IP and port binding status, legacy support.

        :returns:   True if bound to IP and port, False otherwise
        :rtype:     bool
        """
        return self._is_bound

    def bind(self,
             local_ip: str,
             local_port: int = 502,
             max_connections: int = 10):
        """
        Bind IP and port for incomming requests

        :param      local_ip:         IP of this device listening for requests
        :type       local_ip:         str
        :param      local_port:       Port of this device
        :type       local_port:       int
        :param      max_connections:  Number of maximum connections
        :type       max_connections:  int
        """
        if self._client_sock:
            self._client_sock.close()

        if self._sock:
            self._sock.close()

        self._sock = socket.socket()

        # print(socket.getaddrinfo(local_ip, local_port))
        # [(2, 1, 0, '192.168.178.47', ('192.168.178.47', 502))]
        self._sock.bind(socket.getaddrinfo(local_ip, local_port)[0][-1])

        self._sock.listen(max_connections)

        self._is_bound = True

    def _send(self, modbus_pdu: bytes, slave_addr: int) -> None:
        """
        Send Modbus Protocol Data Unit to slave

        :param      modbus_pdu:  The Modbus Protocol Data Unit
        :type       modbus_pdu:  bytes
        :param      slave_addr:  The slave address
        :type       slave_addr:  int
        """
        size = len(modbus_pdu)
        fmt = 'B' * size
        adu = struct.pack('>HHHB' + fmt, self._req_tid, 0, size + 1, slave_addr, *modbus_pdu)
        self._client_sock.send(adu)

    def send_response(self,
                      slave_addr: int,
                      function_code: int,
                      request_register_addr: int,
                      request_register_qty: int,
                      request_data: list,
                      values: Optional[list] = None,
                      signed: bool = True) -> None:
        """
        Send a response to a client.

        :param      slave_addr:             The slave address
        :type       slave_addr:             int
        :param      function_code:          The function code
        :type       function_code:          int
        :param      request_register_addr:  The request register address
        :type       request_register_addr:  int
        :param      request_register_qty:   The request register qty
        :type       request_register_qty:   int
        :param      request_data:           The request data
        :type       request_data:           list
        :param      values:                 The values
        :type       values:                 Optional[list]
        :param      signed:                 Indicates if signed
        :type       signed:                 bool
        """
        modbus_pdu = functions.response(function_code,
                                        request_register_addr,
                                        request_register_qty,
                                        request_data,
                                        values,
                                        signed)
        self._send(modbus_pdu, slave_addr)

    def send_exception_response(self,
                                slave_addr: int,
                                function_code: int,
                                exception_code: int) -> None:
        """
        Send an exception response to a client.

        :param      slave_addr:      The slave address
        :type       slave_addr:      int
        :param      function_code:   The function code
        :type       function_code:   int
        :param      exception_code:  The exception code
        :type       exception_code:  int
        """
        modbus_pdu = functions.exception_response(function_code,
                                                  exception_code)
        self._send(modbus_pdu, slave_addr)

    def _accept_request(self,
                        accept_timeout: float,
                        unit_addr_list: list) -> Union[Request, None]:
        """
        Accept, read and decode a socket based request

        :param      accept_timeout:  The socket accept timeout
        :type       accept_timeout:  float
        :param      unit_addr_list:  The unit address list
        :type       unit_addr_list:  list
        """
        self._sock.settimeout(accept_timeout)
        new_client_sock = None

        try:
            new_client_sock, client_address = self._sock.accept()
        except OSError as e:
            if e.args[0] != 11:     # 11 = timeout expired
                raise e

        if new_client_sock is not None:
            if self._client_sock is not None:
                self._client_sock.close()

            self._client_sock = new_client_sock

            # recv() timeout, setting to 0 might lead to the following error
            # "Modbus request error: [Errno 11] EAGAIN"
            # This is a socket timeout error
            self._client_sock.settimeout(0.5)

        if self._client_sock is not None:
            try:
                req = self._client_sock.recv(128)

                if len(req) == 0:
                    return None

                req_header_no_uid = req[:Const.MBAP_HDR_LENGTH - 1]
                self._req_tid, req_pid, req_len = struct.unpack('>HHH', req_header_no_uid)
                req_uid_and_pdu = req[Const.MBAP_HDR_LENGTH - 1:Const.MBAP_HDR_LENGTH + req_len - 1]
            except OSError:
                # MicroPython raises an OSError instead of socket.timeout
                # print("Socket OSError aka TimeoutError: {}".format(e))
                return None
            except Exception:
                # print("Modbus request error:", e)
                self._client_sock.close()
                self._client_sock = None
                return None

            if (req_pid != 0):
                # print("Modbus request error: PID not 0")
                self._client_sock.close()
                self._client_sock = None
                return None

            if ((unit_addr_list is not None) and (req_uid_and_pdu[0] not in unit_addr_list)):
                return None

            try:
                return Request(self, req_uid_and_pdu)
            except ModbusException as e:
                self.send_exception_response(req[0],
                                             e.function_code,
                                             e.exception_code)
                return None

    def get_request(self,
                    unit_addr_list: Optional[list] = None,
                    timeout: int = None) -> Union[Request, None]:
        """
        Check for request within the specified timeout

        :param      unit_addr_list:  The unit address list
        :type       unit_addr_list:  Optional[list]
        :param      timeout:         The timeout
        :type       timeout:         int

        :returns:   A request object or None.
        :rtype:     Union[Request, None]

        :raises     Exception:       If no socket is configured and bound
        """
        if self._sock is None:
            raise Exception('Modbus TCP server not bound')

        if timeout > 0:
            start_ms = time.ticks_ms()
            elapsed = 0
            while True:
                if self._client_sock is None:
                    accept_timeout = None if timeout is None else (timeout - elapsed) / 1000
                else:
                    accept_timeout = 0
                req = self._accept_request(accept_timeout, unit_addr_list)
                if req:
                    return req
                elapsed = time.ticks_diff(start_ms, time.ticks_ms())
                if elapsed > timeout:
                    return None
        else:
            return self._accept_request(0, unit_addr_list)
