# generated from rosidl_generator_py/resource/_idl.py.em
# with input from turtlebot_cosmo_interface:srv/MoveitControl.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MoveitControl_Request(type):
    """Metaclass of message 'MoveitControl_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('turtlebot_cosmo_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtlebot_cosmo_interface.srv.MoveitControl_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__moveit_control__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__moveit_control__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__moveit_control__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__moveit_control__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__moveit_control__request

            from geometry_msgs.msg import PoseArray
            if PoseArray.__class__._TYPE_SUPPORT is None:
                PoseArray.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MoveitControl_Request(metaclass=Metaclass_MoveitControl_Request):
    """Message class 'MoveitControl_Request'."""

    __slots__ = [
        '_cmd',
        '_posename',
        '_waypoints',
    ]

    _fields_and_field_types = {
        'cmd': 'int32',
        'posename': 'string',
        'waypoints': 'geometry_msgs/PoseArray',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseArray'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.cmd = kwargs.get('cmd', int())
        self.posename = kwargs.get('posename', str())
        from geometry_msgs.msg import PoseArray
        self.waypoints = kwargs.get('waypoints', PoseArray())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.cmd != other.cmd:
            return False
        if self.posename != other.posename:
            return False
        if self.waypoints != other.waypoints:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def cmd(self):
        """Message field 'cmd'."""
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'cmd' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'cmd' field must be an integer in [-2147483648, 2147483647]"
        self._cmd = value

    @builtins.property
    def posename(self):
        """Message field 'posename'."""
        return self._posename

    @posename.setter
    def posename(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'posename' field must be of type 'str'"
        self._posename = value

    @builtins.property
    def waypoints(self):
        """Message field 'waypoints'."""
        return self._waypoints

    @waypoints.setter
    def waypoints(self, value):
        if __debug__:
            from geometry_msgs.msg import PoseArray
            assert \
                isinstance(value, PoseArray), \
                "The 'waypoints' field must be a sub message of type 'PoseArray'"
        self._waypoints = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_MoveitControl_Response(type):
    """Metaclass of message 'MoveitControl_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('turtlebot_cosmo_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtlebot_cosmo_interface.srv.MoveitControl_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__moveit_control__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__moveit_control__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__moveit_control__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__moveit_control__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__moveit_control__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MoveitControl_Response(metaclass=Metaclass_MoveitControl_Response):
    """Message class 'MoveitControl_Response'."""

    __slots__ = [
        '_response',
    ]

    _fields_and_field_types = {
        'response': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.response = kwargs.get('response', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def response(self):
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'response' field must be of type 'bool'"
        self._response = value


class Metaclass_MoveitControl(type):
    """Metaclass of service 'MoveitControl'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('turtlebot_cosmo_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtlebot_cosmo_interface.srv.MoveitControl')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__moveit_control

            from turtlebot_cosmo_interface.srv import _moveit_control
            if _moveit_control.Metaclass_MoveitControl_Request._TYPE_SUPPORT is None:
                _moveit_control.Metaclass_MoveitControl_Request.__import_type_support__()
            if _moveit_control.Metaclass_MoveitControl_Response._TYPE_SUPPORT is None:
                _moveit_control.Metaclass_MoveitControl_Response.__import_type_support__()


class MoveitControl(metaclass=Metaclass_MoveitControl):
    from turtlebot_cosmo_interface.srv._moveit_control import MoveitControl_Request as Request
    from turtlebot_cosmo_interface.srv._moveit_control import MoveitControl_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
