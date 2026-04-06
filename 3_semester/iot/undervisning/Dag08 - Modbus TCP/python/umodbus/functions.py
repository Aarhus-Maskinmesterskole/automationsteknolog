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

# typing not natively supported on MicroPython
from .typing import List, Optional, Union


def read_coils(starting_address: int, quantity: int) -> bytes:
    """
    Create Modbus Protocol Data Unit for reading coils.

    :param      starting_address:  The starting address
    :type       starting_address:  int
    :param      quantity:          Quantity of coils
    :type       quantity:          int

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    if not (1 <= quantity <= 2000):
        raise ValueError('Invalid number of coils')

    return struct.pack('>BHH', Const.READ_COILS, starting_address, quantity)


def read_discrete_inputs(starting_address: int, quantity: int) -> bytes:
    """
    Create Modbus Protocol Data Unit for reading discrete inputs.

    :param      starting_address:  The starting address
    :type       starting_address:  int
    :param      quantity:          Quantity of coils
    :type       quantity:          int

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    if not (1 <= quantity <= 2000):
        raise ValueError('Invalid number of discrete inputs')

    return struct.pack('>BHH',
                       Const.READ_DISCRETE_INPUTS,
                       starting_address,
                       quantity)


def read_holding_registers(starting_address: int, quantity: int) -> bytes:
    """
    Create Modbus Protocol Data Unit for reading holding registers.

    :param      starting_address:  The starting address
    :type       starting_address:  int
    :param      quantity:          Quantity of coils
    :type       quantity:          int

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    if not (1 <= quantity <= 125):
        raise ValueError('Invalid number of holding registers')

    return struct.pack('>BHH',
                       Const.READ_HOLDING_REGISTERS,
                       starting_address,
                       quantity)


def read_input_registers(starting_address: int, quantity: int) -> bytes:
    """
    Create Modbus Protocol Data Unit for reading input registers.

    :param      starting_address:  The starting address
    :type       starting_address:  int
    :param      quantity:          Quantity of coils
    :type       quantity:          int

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    if not (1 <= quantity <= 125):
        raise ValueError('Invalid number of input registers')

    return struct.pack('>BHH',
                       Const.READ_INPUT_REGISTER,
                       starting_address,
                       quantity)


def write_single_coil(output_address: int,
                      output_value: Union[int, bool]) -> bytes:
    """
    Create Modbus message to update single coil

    :param      output_address:  The output address
    :type       output_address:  int
    :param      output_value:    The output value
    :type       output_value:    Union[int, bool]

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    if output_value not in [0x0000, 0xFF00, False, True, 0, 1]:
        raise ValueError('Illegal coil value')

    if output_value not in [0x0000, 0xFF00]:
        if output_value:
            output_value = 0xFF00
        else:
            output_value = 0x0000

    return struct.pack('>BHH',
                       Const.WRITE_SINGLE_COIL,
                       output_address,
                       output_value)


def write_single_register(register_address: int,
                          register_value: int,
                          signed: bool = True) -> bytes:
    """
    Create Modbus message to writes a single register

    :param      register_address:  The register address
    :type       register_address:  int
    :param      register_value:    The register value
    :type       register_value:    int
    :param      signed:            Flag whether data is signed or not
    :type       signed:            bool

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    fmt = 'h' if signed else 'H'

    return struct.pack('>BH' + fmt,
                       Const.WRITE_SINGLE_REGISTER,
                       register_address,
                       register_value)


def write_multiple_coils(starting_address: int,
                         value_list: List[Union[int, bool]]) -> bytes:
    """
    Create Modbus message to update multiple coils

    :param      starting_address:  The starting address
    :type       starting_address:  int
    :param      value_list:        The list of output values
    :type       value_list:        List[Union[int, bool]]

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    if not (1 <= len(value_list) <= 0x07B0):
        raise ValueError('Invalid quantity of outputs')

    sectioned_list = [value_list[i:i + 8] for i in range(0, len(value_list), 8)]    # noqa: E501

    output_value = []
    for index, byte in enumerate(sectioned_list):
        # see https://github.com/brainelectronics/micropython-modbus/issues/22
        # output = sum(v << i for i, v in enumerate(byte))
        output = 0
        for bit in byte:
            output = (output << 1) | bit
        output_value.append(output)

    fmt = 'B' * len(output_value)
    quantity = len(value_list)
    byte_count = quantity // 8
    if quantity % 8:
        byte_count += 1

    return struct.pack('>BHHB' + fmt,
                       Const.WRITE_MULTIPLE_COILS,
                       starting_address,
                       quantity,
                       byte_count,
                       *output_value)


def write_multiple_registers(starting_address: int,
                             register_values: List[int],
                             signed: bool = True) -> bytes:
    """
    Create Modbus message to update multiple coils

    :param      starting_address:  The starting address
    :type       starting_address:  int
    :param      register_values:   The list of output value
    :type       register_values:   List[int, bool]
    :param      signed:            Flag whether data is signed or not
    :type       signed:            bool

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    if not (1 <= len(register_values) <= 123):
        raise ValueError('Invalid number of registers')

    quantity = len(register_values)
    byte_count = quantity * 2
    fmt = ('h' if signed else 'H') * quantity

    return struct.pack('>BHHB' + fmt,
                       Const.WRITE_MULTIPLE_REGISTERS,
                       starting_address,
                       quantity,
                       byte_count,
                       *register_values)


def validate_resp_data(data: bytes,
                       function_code: int,
                       address: int,
                       value: int = None,
                       quantity: int = None,
                       signed: bool = True) -> bool:
    """
    Validate the response data.

    :param      data:           The data
    :type       data:           bytes
    :param      function_code:  The function code
    :type       function_code:  int
    :param      address:        The address
    :type       address:        int
    :param      value:          The value
    :type       value:          int
    :param      quantity:       The quantity
    :type       quantity:       int
    :param      signed:         Indicates if signed
    :type       signed:         bool

    :returns:   True if valid, False otherwise
    :rtype:     bool
    """
    fmt = '>H' + ('h' if signed else 'H')

    if function_code in [Const.WRITE_SINGLE_COIL, Const.WRITE_SINGLE_REGISTER]:
        resp_addr, resp_value = struct.unpack(fmt, data)

        # if bool(True) or int(1) is used as "output_value" of
        # "write_single_coil" it will be internally converted to int(0xFF00),
        # see Modbus specification, which is actually int(65280).
        # Due to the non binary, but real value comparison of "value" and
        # "resp_value", it would never match without the next two lines
        # see #21
        if function_code == Const.WRITE_SINGLE_COIL:
            resp_value = bool(resp_value)
            value = bool(value)

        if (address == resp_addr) and (value == resp_value):
            return True
    elif function_code in [Const.WRITE_MULTIPLE_COILS,
                           Const.WRITE_MULTIPLE_REGISTERS]:
        resp_addr, resp_qty = struct.unpack(fmt, data)

        if (address == resp_addr) and (quantity == resp_qty):
            return True

    return False


def response(function_code: int,
             request_register_addr: int,
             request_register_qty: int,
             request_data: list,
             value_list: Optional[list] = None,
             signed: bool = True) -> bytes:
    """
    Construct a Modbus response Protocol Data Unit

    :param      function_code:          The function code
    :type       function_code:          int
    :param      request_register_addr:  The request register address
    :type       request_register_addr:  int
    :param      request_register_qty:   The request register qty
    :type       request_register_qty:   int
    :param      request_data:           The request data
    :type       request_data:           list
    :param      value_list:             The values
    :type       value_list:             Optional[list]
    :param      signed:                 Indicates if signed
    :type       signed:                 bool

    :returns:   Protocol data unit
    :rtype:     bytes
    """
    if function_code in [Const.READ_COILS, Const.READ_DISCRETE_INPUTS]:
        sectioned_list = [value_list[i:i + 8] for i in range(0, len(value_list), 8)]    # noqa: E501

        output_value = []
        for index, byte in enumerate(sectioned_list):
            # see https://github.com/brainelectronics/micropython-modbus/issues/22
            # output = sum(v << i for i, v in enumerate(byte))
            # see https://github.com/brainelectronics/micropython-modbus/issues/38
            output = 0
            for bit in byte:
                output = (output << 1) | bit
            output_value.append(output)

        fmt = 'B' * len(output_value)
        return struct.pack('>BB' + fmt,
                           function_code,
                           ((len(value_list) - 1) // 8) + 1,
                           *output_value)

    elif function_code in [Const.READ_HOLDING_REGISTERS,
                           Const.READ_INPUT_REGISTER]:
        quantity = len(value_list)

        if not (0x0001 <= quantity <= 0x007D):
            raise ValueError('invalid number of registers')

        if signed is True or signed is False:
            fmt = ('h' if signed else 'H') * quantity
        else:
            fmt = ''
            for s in signed:
                fmt += 'h' if s else 'H'

        return struct.pack('>BB' + fmt,
                           function_code,
                           quantity * 2,
                           *value_list)

    elif function_code in [Const.WRITE_SINGLE_COIL,
                           Const.WRITE_SINGLE_REGISTER]:
        return struct.pack('>BHBB',
                           function_code,
                           request_register_addr,
                           *request_data)

    elif function_code in [Const.WRITE_MULTIPLE_COILS,
                           Const.WRITE_MULTIPLE_REGISTERS]:
        return struct.pack('>BHH',
                           function_code,
                           request_register_addr,
                           request_register_qty)


def exception_response(function_code: int, exception_code: int) -> bytes:
    """
    Create Modbus exception response

    :param      function_code:   The function code
    :type       function_code:   int
    :param      exception_code:  The exception code
    :type       exception_code:  int

    :returns:   Packed Modbus message
    :rtype:     bytes
    """
    return struct.pack('>BB', Const.ERROR_BIAS + function_code, exception_code)


def bytes_to_bool(byte_list: bytes, bit_qty: Optional[int] = 1) -> List[bool]:
    """
    Convert bytes to list of boolean values

    :param      byte_list:  The byte list
    :type       byte_list:  bytes
    :param      bit_qty:    Amount of bits received
    :type       bit_qty:    Optional[int]

    :returns:   Boolean representation
    :rtype:     List[bool]
    """
    bool_list = []

    for index, byte in enumerate(byte_list):
        this_qty = bit_qty

        if this_qty >= 8:
            this_qty = 8

        # evil hack for missing keyword support in MicroPython format()
        fmt = '{:0' + str(this_qty) + 'b}'

        bool_list.extend([bool(int(x)) for x in fmt.format(byte)])

        bit_qty -= 8

    return bool_list


def to_short(byte_array: bytes, signed: bool = True) -> bytes:
    """
    Convert bytes to tuple of integer values

    :param      byte_array:  The byte array
    :type       byte_array:  bytes
    :param      signed:      Indicates if signed
    :type       signed:      bool

    :returns:   Integer representation
    :rtype:     bytes
    """
    response_quantity = int(len(byte_array) / 2)
    fmt = '>' + (('h' if signed else 'H') * response_quantity)

    return struct.unpack(fmt, byte_array)


def float_to_bin(num: float) -> bin:
    """
    Convert floating point value to binary

    See IEEE 754

    :param      num:  The number
    :type       num:  float

    :returns:   Binary representation
    :rtype:     bin
    """
    # no "zfill" available in MicroPython
    # return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)

    return '{:0>{w}}'.format(
        bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:],
        w=32)


def bin_to_float(binary: str) -> float:
    """
    Convert binary string to floating point value

    :param      binary:  The binary string
    :type       binary:  str

    :returns:   Converted floating point value
    :rtype:     float
    """
    return struct.unpack('!f', struct.pack('!I', int(binary, 2)))[0]


def int_to_bin(num: int) -> str:
    """
    Convert integer to binary

    :param      num:  The number
    :type       num:  int

    :returns:   Binary representation of given input
    :rtype:     str
    """
    return "{0:b}".format(num)
