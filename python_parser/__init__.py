from .can_description_parser import parse_devices, parse_messages, parse_frames

import os.path

_data_dir = os.path.join(os.path.dirname(__file__), '../can_description/')
_devices_filepath = os.path.join(_data_dir, 'devices.json')
_messages_filepath = os.path.join(_data_dir, 'messages.json')
_frames_filepath = os.path.join(_data_dir, 'frames.json')


devicesList = parse_devices(_devices_filepath)
"""A list of all `python_parser.can_description_parser.Device`s described in the *devices.json* file.\n
This could be imported from this module."""

messagesList = parse_messages(_messages_filepath)
"""A list of all `python_parser.can_description_parser.Message`s described in the *messages.json* file.\n
This could be imported from this module."""

framesList = parse_frames(_frames_filepath)
"""A list of all `python_parser.can_description_parser.Frame`s described in the *frames.json* file.\n
This could be imported from this module."""
