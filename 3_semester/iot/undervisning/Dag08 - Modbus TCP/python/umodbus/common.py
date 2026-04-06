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
import struct

# custom packages
from . import const as Const
from . import functions

# typing not natively supported on MicroPython
from .typing import List, Optional, Tuple, Union


class Request(object):
    """Deconstruct request data received via TCP or Serial"""
    def __init__(self, interface, data: bytearray) -> None:
        self._itf = interface
        self.unit_addr = data[0]
        self.function, self.register_addr = struct.unpack_from('>BH', data, 1)

        if self.function in [Const.READ_COILS, Const.READ_DISCRETE_INPUTS]:
            self.quantity = struct.unpack_from('>H', data, 4)[0]

            if self.quantity < 0x0001 or self.quantity > 0x07D0:
                raise ModbusException(self.function, Const.ILLEGAL_DATA_VALUE)

            self.data = None
        elif self.function in [Const.READ_HOLDING_REGISTERS, Const.READ_INPUT_REGISTER]:
            self.quantity = struct.unpack_from('>H', data, 4)[0]

            if self.quantity < 0x0001 or self.quantity > 0x007D:
                raise ModbusException(self.function, Const.ILLEGAL_DATA_VALUE)

            self.data = None
        elif self.function == Const.WRITE_SINGLE_COIL:
            self.quantity = None
            self.data = data[4:6]

            # allowed values: 0x0000 or 0xFF00
            if (self.data[0] not in [0x00, 0xFF]) or self.data[1] != 0x00:
                raise ModbusException(self.function, Const.ILLEGAL_DATA_VALUE)
        elif self.function == Const.WRITE_SINGLE_REGISTER:
            self.quantity = None
            self.data = data[4:6]
            # all values allowed
        elif self.function == Const.WRITE_MULTIPLE_COILS:
            self.quantity = struct.unpack_from('>H', data, 4)[0]
            if self.quantity < 0x0001 or self.quantity > 0x07D0:
                raise ModbusException(self.function, Const.ILLEGAL_DATA_VALUE)
            self.data = data[7:]
            if len(self.data) != ((self.quantity - 1) // 8) + 1:
                raise ModbusException(self.function, Const.ILLEGAL_DATA_VALUE)
        elif self.function == Const.WRITE_MULTIPLE_REGISTERS:
            self.quantity = struct.unpack_from('>H', data, 4)[0]
            if self.quantity < 0x0001 or self.quantity > 0x007B:
                raise ModbusException(self.function, Const.ILLEGAL_DATA_VALUE)
            self.data = data[7:]
            if len(self.data) != self.quantity * 2:
                raise ModbusException(self.function, Const.ILLEGAL_DATA_VALUE)
        else:
            # Not implemented functions
            self.quantity = None
            self.data = data[4:]

    def send_response(self,
                      values: Optional[list] = None,
                      signed: bool = True) -> None:
        """
        Send a response via the configured interface.

        :param      values:  The values
        :type       values:  Optional[list]
        :param      signed:  Indicates if signed values are used
        :type       signed:  bool
        """
        self._itf.send_response(self.unit_addr,
                                self.function,
                                self.register_addr,
                                self.quantity,
                                self.data,
                                values,
                                signed)

    def send_exception(self, exception_code: int) -> None:
        """
        Send an exception response.

        :param      exception_code:  The exception code
        :type       exception_code:  int
        """
        self._itf.send_exception_response(self.unit_addr,
                                          self.function,
                                          exception_code)


class ModbusException(Exception):
    """Exception for signaling modbus errors"""
    def __init__(self, function_code: int, exception_code: int) -> None:
        self.function_code = function_code
        self.exception_code = exception_code


class CommonModbusFunctions(object):
    """Common Modbus functions"""
    def __init__(self):
        pass

    def read_coils(self,
                   slave_addr: int,
                   starting_addr: int,
                   coil_qty: int) -> List[bool]:
        """
        Read coils (COILS).

        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      starting_addr:  The coil starting address
        :type       starting_addr:  int
        :param      coil_qty:       The amount of coils to read
        :type       coil_qty:       int

        :returns:   State of read coils as list
        :rtype:     List[bool]
        """
        modbus_pdu = functions.read_coils(starting_address=starting_addr,
                                          quantity=coil_qty)

        response = self._send_receive(slave_addr=slave_addr,
                                      modbus_pdu=modbus_pdu,
                                      count=True)

        status_pdu = functions.bytes_to_bool(byte_list=response,
                                             bit_qty=coil_qty)

        return status_pdu

    def read_discrete_inputs(self,
                             slave_addr: int,
                             starting_addr: int,
                             input_qty: int) -> List[bool]:
        """
        Read discrete inputs (ISTS).

        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      starting_addr:  The discrete input starting address
        :type       starting_addr:  int
        :param      input_qty:      The amount of discrete inputs to read
        :type       input_qty:      int

        :returns:   State of read discrete inputs as list
        :rtype:     List[bool]
        """
        modbus_pdu = functions.read_discrete_inputs(
            starting_address=starting_addr,
            quantity=input_qty)

        response = self._send_receive(slave_addr=slave_addr,
                                      modbus_pdu=modbus_pdu,
                                      count=True)

        status_pdu = functions.bytes_to_bool(byte_list=response,
                                             bit_qty=input_qty)

        return status_pdu

    def read_holding_registers(self,
                               slave_addr: int,
                               starting_addr: int,
                               register_qty: int,
                               signed: bool = True) -> Tuple[int, ...]:
        """
        Read holding registers (HREGS).

        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      starting_addr:  The holding register starting address
        :type       starting_addr:  int
        :param      register_qty:   The amount of holding registers to read
        :type       register_qty:   int
        :param      signed:         Indicates if signed
        :type       signed:         bool

        :returns:   State of read holding register as tuple
        :rtype:     Tuple[int, ...]
        """
        modbus_pdu = functions.read_holding_registers(
            starting_address=starting_addr,
            quantity=register_qty)

        response = self._send_receive(slave_addr=slave_addr,
                                      modbus_pdu=modbus_pdu,
                                      count=True)

        register_value = functions.to_short(byte_array=response, signed=signed)

        return register_value

    def read_input_registers(self,
                             slave_addr: int,
                             starting_addr: int,
                             register_qty: int,
                             signed: bool = True) -> Tuple[int, ...]:
        """
        Read input registers (IREGS).

        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      starting_addr:  The input register starting address
        :type       starting_addr:  int
        :param      register_qty:   The amount of input registers to read
        :type       register_qty:   int
        :param      signed:         Indicates if signed
        :type       signed:         bool

        :returns:   State of read input register as tuple
        :rtype:     Tuple[int, ...]
        """
        modbus_pdu = functions.read_input_registers(
            starting_address=starting_addr,
            quantity=register_qty)

        response = self._send_receive(slave_addr=slave_addr,
                                      modbus_pdu=modbus_pdu,
                                      count=True)

        register_value = functions.to_short(byte_array=response, signed=signed)

        return register_value

    def write_single_coil(self,
                          slave_addr: int,
                          output_address: int,
                          output_value: Union[int, bool]) -> bool:
        """
        Update a single coil.

        :param      slave_addr:      The slave address
        :type       slave_addr:      int
        :param      output_address:  The output address
        :type       output_address:  int
        :param      output_value:    The output value
        :type       output_value:    Union[int, bool]

        :returns:   Result of operation
        :rtype:     bool
        """
        modbus_pdu = functions.write_single_coil(output_address=output_address,
                                                 output_value=output_value)

        response = self._send_receive(slave_addr=slave_addr,
                                      modbus_pdu=modbus_pdu,
                                      count=False)

        if response is None:
            return False

        operation_status = functions.validate_resp_data(
            data=response,
            function_code=Const.WRITE_SINGLE_COIL,
            address=output_address,
            value=output_value,
            signed=False)

        return operation_status

    def write_single_register(self,
                              slave_addr: int,
                              register_address: int,
                              register_value: int,
                              signed: bool = True) -> bool:
        """
        Update a single register.

        :param      slave_addr:        The slave address
        :type       slave_addr:        int
        :param      register_address:  The register address
        :type       register_address:  int
        :param      register_value:    The register value
        :type       register_value:    int
        :param      signed:            Indicates if signed
        :type       signed:            bool

        :returns:   Result of operation
        :rtype:     bool
        """
        modbus_pdu = functions.write_single_register(
            register_address=register_address,
            register_value=register_value,
            signed=signed)

        response = self._send_receive(slave_addr=slave_addr,
                                      modbus_pdu=modbus_pdu,
                                      count=False)

        if response is None:
            return False

        operation_status = functions.validate_resp_data(
            data=response,
            function_code=Const.WRITE_SINGLE_REGISTER,
            address=register_address,
            value=register_value,
            signed=signed)

        return operation_status

    def write_multiple_coils(self,
                             slave_addr: int,
                             starting_address: int,
                             output_values: List[Union[int, bool]]) -> bool:
        """
        Update multiple coils.

        :param      slave_addr:        The slave address
        :type       slave_addr:        int
        :param      starting_address:  The address of the first coil
        :type       starting_address:  int
        :param      output_values:     The output values
        :type       output_values:     List[Union[int, bool]]

        :returns:   Result of operation
        :rtype:     bool
        """
        modbus_pdu = functions.write_multiple_coils(
            starting_address=starting_address,
            value_list=output_values)

        response = self._send_receive(slave_addr=slave_addr,
                                      modbus_pdu=modbus_pdu,
                                      count=False)

        if response is None:
            return False

        operation_status = functions.validate_resp_data(
            data=response,
            function_code=Const.WRITE_MULTIPLE_COILS,
            address=starting_address,
            quantity=len(output_values))

        return operation_status

    def write_multiple_registers(self,
                                 slave_addr: int,
                                 starting_address: int,
                                 register_values: List[int],
                                 signed: bool = True) -> bool:
        """
        Update multiple registers.

        :param      slave_addr:        The slave address
        :type       slave_addr:        int
        :param      starting_address:  The starting address
        :type       starting_address:  int
        :param      register_values:   The register values
        :type       register_values:   List[int]
        :param      signed:            Indicates if signed
        :type       signed:            bool

        :returns:   Result of operation
        :rtype:     bool
        """
        modbus_pdu = functions.write_multiple_registers(
            starting_address=starting_address,
            register_values=register_values,
            signed=signed)

        response = self._send_receive(slave_addr=slave_addr,
                                      modbus_pdu=modbus_pdu,
                                      count=False)

        if response is None:
            return False

        operation_status = functions.validate_resp_data(
            data=response,
            function_code=Const.WRITE_MULTIPLE_REGISTERS,
            address=starting_address,
            quantity=len(register_values),
            signed=signed
        )

        return operation_status
