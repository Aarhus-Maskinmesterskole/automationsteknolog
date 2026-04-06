#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Modbus register abstraction class

Used to add, remove, set and get values or states of a register or coil.
Additional helper properties and functions like getters for changed registers
are available as well.

This class is inherited by the Modbus client implementations
:py:class:`umodbus.serial.ModbusRTU` and :py:class:`umodbus.tcp.ModbusTCP`
"""

# system packages
import time

# custom packages
from . import functions
from . import const as Const
from .common import Request

# typing not natively supported on MicroPython
from .typing import Callable, dict_keys, List, Optional, Union


class Modbus(object):
    """
    Modbus register abstraction

    :param      itf:        Abstraction interface
    :type       itf:        Callable
    :param      addr_list:  List of addresses
    :type       addr_list:  List[int]
    """
    def __init__(self, itf, addr_list: List[int]) -> None:
        self._itf = itf
        self._addr_list = addr_list

        # modbus register types with their default value
        self._available_register_types = ['COILS', 'HREGS', 'IREGS', 'ISTS']
        self._register_dict = dict()
        for reg_type in self._available_register_types:
            self._register_dict[reg_type] = dict()
        self._default_vals = dict(zip(self._available_register_types,
                                      [False, 0, 0, False]))

        # registers which can be set by remote device
        self._changeable_register_types = ['COILS', 'HREGS']
        self._changed_registers = dict()
        for reg_type in self._changeable_register_types:
            self._changed_registers[reg_type] = dict()

    def process(self) -> bool:
        """
        Process the Modbus requests.

        :returns:   Result of processing, True on success, False otherwise
        :rtype:     bool
        """
        reg_type = None
        req_type = None

        request = self._itf.get_request(unit_addr_list=self._addr_list,
                                        timeout=0)
        if request is None:
            return False

        if request.function == Const.READ_COILS:
            # Coils (setter+getter) [0, 1]
            # function 01 - read single register
            reg_type = 'COILS'
            req_type = 'READ'
        elif request.function == Const.READ_DISCRETE_INPUTS:
            # Ists (only getter) [0, 1]
            # function 02 - read input status (discrete inputs/digital input)
            reg_type = 'ISTS'
            req_type = 'READ'
        elif request.function == Const.READ_HOLDING_REGISTERS:
            # Hregs (setter+getter) [0, 65535]
            # function 03 - read holding register
            reg_type = 'HREGS'
            req_type = 'READ'
        elif request.function == Const.READ_INPUT_REGISTER:
            # Iregs (only getter) [0, 65535]
            # function 04 - read input registers
            reg_type = 'IREGS'
            req_type = 'READ'
        elif (request.function == Const.WRITE_SINGLE_COIL or
                request.function == Const.WRITE_MULTIPLE_COILS):
            # Coils (setter+getter) [0, 1]
            # function 05 - write single coil
            # function 15 - write multiple coil
            reg_type = 'COILS'
            req_type = 'WRITE'
        elif (request.function == Const.WRITE_SINGLE_REGISTER or
                request.function == Const.WRITE_MULTIPLE_REGISTERS):
            # Hregs (setter+getter) [0, 65535]
            # function 06 - write holding register
            # function 16 - write multiple holding register
            reg_type = 'HREGS'
            req_type = 'WRITE'
        else:
            request.send_exception(Const.ILLEGAL_FUNCTION)

        if reg_type:
            if req_type == 'READ':
                self._process_read_access(request=request, reg_type=reg_type)
            elif req_type == 'WRITE':
                self._process_write_access(request=request, reg_type=reg_type)

        return True

    def _create_response(self,
                         request: Request,
                         reg_type: str) -> Union[List[bool], List[int]]:
        """
        Create a response.

        :param      request:   The request
        :type       request:   Request
        :param      reg_type:  The register type
        :type       reg_type:  str

        :returns:   Values of this register
        :rtype:     Union[List[bool], List[int]]
        """
        data = []
        default_value = {'val': 0}
        reg_dict = self._register_dict[reg_type]

        if reg_type in ['COILS', 'ISTS']:
            default_value = {'val': False}

        for addr in range(request.register_addr,
                          request.register_addr + request.quantity):
            value = reg_dict.get(addr, default_value)['val']

            if isinstance(value, (list, tuple)):
                data.extend(value)
            else:
                data.append(value)

        # caution LSB vs MSB
        # [
        #   1, 0, 1, 1, 0, 0, 1, 1,     # 0xB3
        #   1, 1, 0, 1, 0, 1, 1, 0,     # 0xD6
        #   1, 0, 1                     # 0x5
        # ]
        # but should be, documented at #38, see
        # https://github.com/brainelectronics/micropython-modbus/issues/38
        # this is only an issue of data provisioning as client/slave,
        # it has thereby NOT to be fixed in
        # :py:function:`umodbus.functions.bytes_to_bool`
        # [
        #   1, 1, 0, 0, 1, 1, 0, 1,     # 0xCD
        #   0, 1, 1, 0, 1, 0, 1, 1,     # 0x6B
        #   1, 0, 1                     # 0x5
        # ]
        #       27 .... 20
        # CD    1100 1101
        #
        #       35 .... 28
        # 6B    0110 1011
        #
        #       43 .... 36
        # 05    0000 0101
        #
        # 1011 0011   1101 0110   1010 0000

        return data

    def _process_read_access(self, request: Request, reg_type: str) -> None:
        """
        Process read access to register

        :param      request:   The request
        :type       request:   Request
        :param      reg_type:  The register type
        :type       reg_type:  str
        """
        address = request.register_addr

        if address in self._register_dict[reg_type]:

            if self._register_dict[reg_type][address].get('on_get_cb', 0):
                vals = self._create_response(request=request,
                                             reg_type=reg_type)
                _cb = self._register_dict[reg_type][address]['on_get_cb']
                _cb(reg_type=reg_type, address=address, val=vals)

            vals = self._create_response(request=request, reg_type=reg_type)
            request.send_response(vals)
        else:
            request.send_exception(Const.ILLEGAL_DATA_ADDRESS)

    def _process_write_access(self, request: Request, reg_type: str) -> None:
        """
        Process write access to register

        :param      request:   The request
        :type       request:   Request
        :param      reg_type:  The register type
        :type       reg_type:  str
        """
        address = request.register_addr
        val = 0
        valid_register = False

        if address in self._register_dict[reg_type]:
            if request.data is None:
                request.send_exception(Const.ILLEGAL_DATA_VALUE)
                return

            if reg_type == 'COILS':
                valid_register = True

                if request.function == Const.WRITE_SINGLE_COIL:
                    val = request.data[0]
                    if 0x00 < val < 0xFF:
                        valid_register = False
                        request.send_exception(Const.ILLEGAL_DATA_VALUE)
                    else:
                        val = [(val == 0xFF)]
                elif request.function == Const.WRITE_MULTIPLE_COILS:
                    tmp = int.from_bytes(request.data, "big")
                    val = [
                        bool(tmp & (1 << n)) for n in range(request.quantity)
                    ]

                if valid_register:
                    self.set_coil(address=address, value=val)
            elif reg_type == 'HREGS':
                valid_register = True
                val = list(functions.to_short(byte_array=request.data,
                                              signed=False))

                if request.function in [Const.WRITE_SINGLE_REGISTER,
                                        Const.WRITE_MULTIPLE_REGISTERS]:
                    self.set_hreg(address=address, value=val)
            else:
                # nothing except holding registers or coils can be set
                request.send_exception(Const.ILLEGAL_FUNCTION)

            if valid_register:
                request.send_response()
                self._set_changed_register(reg_type=reg_type,
                                           address=address,
                                           value=val)
                if self._register_dict[reg_type][address].get('on_set_cb', 0):
                    _cb = self._register_dict[reg_type][address]['on_set_cb']
                    _cb(reg_type=reg_type, address=address, val=val)
        else:
            request.send_exception(Const.ILLEGAL_DATA_ADDRESS)

    def add_coil(self,
                 address: int,
                 value: Union[bool, List[bool]] = False,
                 on_set_cb: Callable[[str, int, Union[List[bool], List[int]]],
                                     None] = None,
                 on_get_cb: Callable[[str, int, Union[List[bool], List[int]]],
                                     None] = None) -> None:
        """
        Add a coil to the modbus register dictionary.

        :param      address:    The address (ID) of the register
        :type       address:    int
        :param      value:      The default value
        :type       value:      Union[bool, List[bool]], optional
        :param      on_set_cb:  Callback on setting the coil
        :type       on_set_cb:  Callable[
            [str, int, Union[List[bool], List[int]]],
            None
            ]
        :param      on_get_cb:  Callback on getting the coil
        :type       on_get_cb:  Callable[
            [str, int, Union[List[bool], List[int]]],
            None
            ]
        """
        self._set_reg_in_dict(reg_type='COILS',
                              address=address,
                              value=value,
                              on_set_cb=on_set_cb,
                              on_get_cb=on_get_cb)

    def remove_coil(self, address: int) -> Union[None, bool, List[bool]]:
        """
        Remove a coil from the modbus register dictionary.

        :param      address:  The address (ID) of the register
        :type       address:  int

        :returns:   Register value, None if register did not exist in dict
        :rtype:     Union[None, bool, List[bool]]
        """
        return self._remove_reg_from_dict(reg_type='COILS', address=address)

    def set_coil(self,
                 address: int,
                 value: Union[bool, List[bool]] = False) -> None:
        """
        Set the coil value.

        :param      address:  The address (ID) of the register
        :type       address:  int
        :param      value:    The default value
        :type       value:    Union[bool, List[bool]], optional
        """
        self._set_reg_in_dict(reg_type='COILS',
                              address=address,
                              value=value)

    def get_coil(self, address: int) -> Union[bool, List[bool]]:
        """
        Get the coil value.

        :param      address:  The address (ID) of the register
        :type       address:  bool

        :returns:   Coil value
        :rtype:     Union[bool, List[bool]]
        """
        return self._get_reg_in_dict(reg_type='COILS',
                                     address=address)

    @property
    def coils(self) -> dict_keys:
        """
        Get the configured coils.

        :returns:   The dictionary keys.
        :rtype:     dict_keys
        """
        return self._get_regs_of_dict(reg_type='COILS')

    def add_hreg(self,
                 address: int,
                 value: Union[int, List[int]] = 0,
                 on_set_cb: Callable[[str, int, List[int]], None] = None,
                 on_get_cb: Callable[[str, int, List[int]], None] = None) -> None:
        """
        Add a holding register to the modbus register dictionary.

        :param      address:    The address (ID) of the register
        :type       address:    int
        :param      value:      The default value
        :type       value:      Union[int, List[int]], optional
        :param      on_set_cb:  Callback on setting the holding register
        :type       on_set_cb:  Callable[[str, int, List[int]], None]
        :param      on_get_cb:  Callback on getting the holding register
        :type       on_get_cb:  Callable[[str, int, List[int]], None]
        """
        self._set_reg_in_dict(reg_type='HREGS',
                              address=address,
                              value=value,
                              on_set_cb=on_set_cb,
                              on_get_cb=on_get_cb)

    def remove_hreg(self, address: int) -> Union[None, int, List[int]]:
        """
        Remove a holding register from the modbus register dictionary.

        :param      address:  The address (ID) of the register
        :type       address:  int

        :returns:   Register value, None if register did not exist in dict
        :rtype:     Union[None, int, List[int]]
        """
        return self._remove_reg_from_dict(reg_type='HREGS', address=address)

    def set_hreg(self, address: int, value: Union[int, List[int]] = 0) -> None:
        """
        Set the holding register value.

        :param      address:  The address (ID) of the register
        :type       address:  int
        :param      value:    The default value
        :type       value:    int or list of int, optional
        """
        self._set_reg_in_dict(reg_type='HREGS',
                              address=address,
                              value=value)

    def get_hreg(self, address: int) -> Union[int, List[int]]:
        """
        Get the holding register value.

        :param      address:  The address (ID) of the register
        :type       address:  int

        :returns:   Holding register value
        :rtype:     Union[int, List[int]]
        """
        return self._get_reg_in_dict(reg_type='HREGS',
                                     address=address)

    @property
    def hregs(self) -> dict_keys:
        """
        Get the configured holding registers.

        :returns:   The dictionary keys.
        :rtype:     dict_keys
        """
        return self._get_regs_of_dict(reg_type='HREGS')

    def add_ist(self,
                address: int,
                value: Union[bool, List[bool]] = False,
                on_get_cb: Callable[[str, int, Union[List[bool], List[int]]],
                                    None] = None) -> None:
        """
        Add a discrete input register to the modbus register dictionary.

        :param      address:    The address (ID) of the register
        :type       address:    int
        :param      value:      The default value
        :type       value:      bool or list of bool, optional
        :param      on_get_cb:  Callback on getting the discrete input register
        :type       on_get_cb:  Callable[
            [str, int, Union[List[bool], List[int]]],
            None
            ]
        """
        self._set_reg_in_dict(reg_type='ISTS',
                              address=address,
                              value=value,
                              on_get_cb=on_get_cb)

    def remove_ist(self, address: int) -> Union[None, bool, List[bool]]:
        """
        Remove a discrete input register from the modbus register dictionary.

        :param      address:  The address (ID) of the register
        :type       address:  int

        :returns:   Register value, None if register did not exist in dict
        :rtype:     Union[None, bool, List[bool]]
        """
        return self._remove_reg_from_dict(reg_type='ISTS', address=address)

    def set_ist(self, address: int, value: bool = False) -> None:
        """
        Set the discrete input register value.

        :param      address:  The address (ID) of the register
        :type       address:  int
        :param      value:    The default value
        :type       value:    bool or list of bool, optional
        """
        self._set_reg_in_dict(reg_type='ISTS',
                              address=address,
                              value=value)

    def get_ist(self, address: int) -> Union[bool, List[bool]]:
        """
        Get the discrete input register value.

        :param      address:  The address (ID) of the register
        :type       address:  int

        :returns:   Discrete input register value
        :rtype:     Union[bool, List[bool]]
        """
        return self._get_reg_in_dict(reg_type='ISTS',
                                     address=address)

    @property
    def ists(self) -> dict_keys:
        """
        Get the configured discrete input registers.

        :returns:   The dictionary keys.
        :rtype:     dict_keys
        """
        return self._get_regs_of_dict(reg_type='ISTS')

    def add_ireg(self,
                 address: int,
                 value: Union[int, List[int]] = 0,
                 on_get_cb: Callable[[str, int, Union[List[bool], List[int]]],
                                     None] = None) -> None:
        """
        Add an input register to the modbus register dictionary.

        :param      address:    The address (ID) of the register
        :type       address:    int
        :param      value:      The default value
        :type       value:      Union[int, List[int]], optional
        :param      on_get_cb:  Callback on getting the input register
        :type       on_get_cb:  Callable[
            [str, int, Union[List[bool], List[int]]],
            None
            ]
        """
        self._set_reg_in_dict(reg_type='IREGS',
                              address=address,
                              value=value,
                              on_get_cb=on_get_cb)

    def remove_ireg(self, address: int) -> Union[None, int, List[int]]:
        """
        Remove an input register from the modbus register dictionary.

        :param      address:  The address (ID) of the register
        :type       address:  int

        :returns:   Register value, None if register did not exist in dict
        :rtype:     Union[None, int, List[int]]
        """
        return self._remove_reg_from_dict(reg_type='IREGS', address=address)

    def set_ireg(self, address: int, value: Union[int, List[int]] = 0) -> None:
        """
        Set the input register value.

        :param      address:  The address (ID) of the register
        :type       address:  int
        :param      value:    The default value
        :type       value:    Union[int, List[int]], optional
        """
        self._set_reg_in_dict(reg_type='IREGS',
                              address=address,
                              value=value)

    def get_ireg(self, address: int) -> Union[int, List[int]]:
        """
        Get the input register value.

        :param      address:  The address (ID) of the register
        :type       address:  int

        :returns:   Input register value
        :rtype:     Union[int, List[int]]
        """
        return self._get_reg_in_dict(reg_type='IREGS',
                                     address=address)

    @property
    def iregs(self) -> dict_keys:
        """
        Get the configured input registers.

        :returns:   The dictionary keys.
        :rtype:     dict_keys
        """
        return self._get_regs_of_dict(reg_type='IREGS')

    def _set_reg_in_dict(self,
                         reg_type: str,
                         address: int,
                         value: Union[bool, int, List[bool], List[int]],
                         on_set_cb: Callable[[str, int, Union[List[bool],
                                                              List[int]]],
                                             None] = None,
                         on_get_cb: Callable[[str, int, Union[List[bool],
                                                              List[int]]],
                                             None] = None) -> None:
        """
        Set the register value in the dictionary of registers.

        :param      reg_type:   The register type
        :type       reg_type:   str
        :param      address:    The address (ID) of the register
        :type       address:    int
        :param      value:      The value(s) of the register(s)
        :type       value:      Union[bool, int, List[bool], List[int]]
        :param      on_set_cb:  Callback on setting the register
        :type       on_get_cb:  Callable[
            [str, int, Union[List[bool], List[int]]],
            None
            ]
        :param      on_get_cb:  Callback on getting the register
        :type       on_get_cb:  Callable[
            [str, int, Union[List[bool], List[int]]],
            None
            ]

        :raise      KeyError:  No register at specified address found
        """
        if not self._check_valid_register(reg_type=reg_type):
            raise KeyError('{} is not a valid register type of {}'.
                           format(reg_type, self._available_register_types))

        if isinstance(value, (list, tuple)):
            # flatten the list and add single registers only
            for idx, val in enumerate(value):
                this_addr = address + idx
                self._set_single_reg_in_dict(reg_type=reg_type,
                                             address=this_addr,
                                             value=val,
                                             on_set_cb=on_set_cb,
                                             on_get_cb=on_get_cb)
        else:
            self._set_single_reg_in_dict(reg_type=reg_type,
                                         address=address,
                                         value=value,
                                         on_set_cb=on_set_cb,
                                         on_get_cb=on_get_cb)

    def _set_single_reg_in_dict(self,
                                reg_type: str,
                                address: int,
                                value: Union[bool, int],
                                on_set_cb: Callable[
                                    [str, int, Union[List[bool], List[int]]],
                                    None
                                ] = None,
                                on_get_cb: Callable[
                                    [str, int, Union[List[bool], List[int]]],
                                    None
                                ] = None) -> None:
        """
        Set a register value in the dictionary of registers.

        :param      reg_type:   The register type
        :type       reg_type:   str
        :param      address:    The address (ID) of the register
        :type       address:    int
        :param      value:      The value of the register
        :type       value:      Union[bool, int]
        :param      on_set_cb:  Callback on setting the register
        :type       on_get_cb:  Callable[
            [str, int, Union[List[bool], List[int]]],
            None
            ]
        :param      on_get_cb:  Callback on getting the register
        :type       on_get_cb:  Callable[
            [str, int, Union[List[bool], List[int]]],
            None
            ]
        """
        data = {'val': value}

        # if the register exists already in the register dict a "set_*"
        # function might have called this functions
        if address in self._register_dict[reg_type]:
            # try to get the (already) registered callback function from the
            # register dict of this address with the this time call function
            # parameter callback value as fallback
            on_set_cb = self._register_dict[reg_type][address].get('on_set_cb',
                                                                   on_set_cb)

            on_get_cb = self._register_dict[reg_type][address].get('on_get_cb',
                                                                   on_get_cb)

        if callable(on_set_cb):
            data['on_set_cb'] = on_set_cb

        if callable(on_get_cb):
            data['on_get_cb'] = on_get_cb

        self._register_dict[reg_type][address] = data

    def _remove_reg_from_dict(self,
                              reg_type: str,
                              address: int) -> Union[None, bool, int, List[bool], List[int]]:
        """
        Remove the register from the dictionary of registers.

        :param      reg_type:  The register type
        :type       reg_type:  str
        :param      address:   The address (ID) of the register
        :type       address:   int

        :raise      KeyError:  No register at specified address found
        :returns:   Register value, None if register did not exist in dict
        :rtype:     Union[None, bool, int, List[bool], List[int]]
        """
        if not self._check_valid_register(reg_type=reg_type):
            raise KeyError('{} is not a valid register type of {}'.
                           format(reg_type, self._available_register_types))

        return self._register_dict[reg_type].pop(address, None)

    def _get_reg_in_dict(self,
                         reg_type: str,
                         address: int) -> Union[bool, int, List[bool], List[int]]:
        """
        Get the register value from the dictionary of registers.

        :param      reg_type:  The register type
        :type       reg_type:  str
        :param      address:   The address (ID) of the register
        :type       address:   int

        :raise      KeyError:  No register at specified address found
        :returns:   Register value
        :rtype:     Union[bool, int, List[bool], List[int]]
        """
        if not self._check_valid_register(reg_type=reg_type):
            raise KeyError('{} is not a valid register type of {}'.
                           format(reg_type, self._available_register_types))

        if address in self._register_dict[reg_type]:
            return self._register_dict[reg_type][address]['val']
        else:
            raise KeyError('No {} available for the register address {}'.
                           format(reg_type, address))

    def _get_regs_of_dict(self, reg_type: str) -> dict_keys:
        """
        Get all configured registers of specified register type.

        :param      reg_type:  The register type
        :type       reg_type:  str

        :raise      KeyError:  No register at specified address found
        :returns:   The configured registers of the specified register type.
        :rtype:     dict_keys
        """
        if not self._check_valid_register(reg_type=reg_type):
            raise KeyError('{} is not a valid register type of {}'.
                           format(reg_type, self._available_register_types))

        return self._register_dict[reg_type].keys()

    def _check_valid_register(self, reg_type: str) -> bool:
        """
        Check register type to be a valid modbus register

        :param      reg_type:  The register type
        :type       reg_type:  str

        :returns:   Flag whether register type is valid
        :rtype:     bool
        """
        if reg_type in self._available_register_types:
            return True
        else:
            return False

    @property
    def changed_registers(self) -> dict:
        """
        Get the changed registers.

        :returns:   The changed registers.
        :rtype:     dict
        """
        return self._changed_registers

    @property
    def changed_coils(self) -> dict:
        """
        Get the changed coil registers.

        :returns:   The changed coil registers.
        :rtype:     dict
        """
        return self._changed_registers['COILS']

    @property
    def changed_hregs(self) -> dict:
        """
        Get the changed holding registers.

        :returns:   The changed holding registers.
        :rtype:     dict
        """
        return self._changed_registers['HREGS']

    def _set_changed_register(self,
                              reg_type: str,
                              address: int,
                              value: Union[bool, int, List[bool], List[int]]) -> None:
        """
        Set the register value in the dictionary of changed registers.

        :param      reg_type:  The register type
        :type       reg_type:  str
        :param      address:   The address (ID) of the register
        :type       address:   int
        :param      value:     The value
        :type       value:     Union[bool, int, List[bool], List[int]]

        :raise      KeyError:  Register can not be changed externally
        """
        if reg_type in self._changeable_register_types:
            if isinstance(value, (list, tuple)):
                for idx, val in enumerate(value):
                    content = {'val': val, 'time': time.ticks_ms()}
                    self._changed_registers[reg_type][address + idx] = content
            else:
                content = {'val': value, 'time': time.ticks_ms()}
                self._changed_registers[reg_type][address] = content
        else:
            raise KeyError('{} can not be changed externally'.format(reg_type))

    def _remove_changed_register(self,
                                 reg_type: str,
                                 address: int,
                                 timestamp: int) -> bool:
        """
        Remove the register from the dictionary of changed registers.

        :param      reg_type:  The register type
        :type       reg_type:  str
        :param      address:   The address (ID) of the register
        :type       address:   int
        :param      timestamp: The timestamp of the change in milliseconds
        :type       timestamp: int

        :raise      KeyError:  No register at specified address found
        :returns:   Result of removing register from dict
        :rtype:     bool
        """
        result = False

        if reg_type in self._changeable_register_types:
            _changed_register_timestamp = self._changed_registers[reg_type][address]['time']

            if _changed_register_timestamp == timestamp:
                self._changed_registers[reg_type].pop(address, None)
                result = True
        else:
            raise KeyError('{} is not a valid register type of {}'.
                           format(reg_type, self._changeable_register_types))

        return result

    def setup_registers(self,
                        registers: dict = dict(),
                        use_default_vals: Optional[bool] = False) -> None:
        """
        Setup all registers of the client

        :param      registers:         The registers
        :type       registers:         dict
        :param      use_default_vals:  Flag to use dummy default values
        :type       use_default_vals:  Optional[bool]
        """
        if len(registers):
            for reg_type, default_val in self._default_vals.items():
                if reg_type in registers:
                    for reg, val in registers[reg_type].items():
                        address = val['register']

                        if use_default_vals:
                            if 'len' in val:
                                value = [default_val] * val['len']
                            else:
                                value = default_val
                        else:
                            value = val['val']

                        on_set_cb = val.get('on_set_cb', None)
                        on_get_cb = val.get('on_get_cb', None)

                        if reg_type == 'COILS':
                            self.add_coil(address=address,
                                          value=value,
                                          on_set_cb=on_set_cb,
                                          on_get_cb=on_get_cb)
                        elif reg_type == 'HREGS':
                            self.add_hreg(address=address,
                                          value=value,
                                          on_set_cb=on_set_cb,
                                          on_get_cb=on_get_cb)
                        elif reg_type == 'ISTS':
                            self.add_ist(address=address,
                                         value=value,
                                         on_get_cb=on_get_cb)   # only getter
                        elif reg_type == 'IREGS':
                            self.add_ireg(address=address,
                                          value=value,
                                          on_get_cb=on_get_cb)  # only getter
                        else:
                            # invalid register type
                            pass
                else:
                    pass
