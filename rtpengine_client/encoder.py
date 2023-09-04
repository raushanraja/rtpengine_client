import bencode
import logging
from typing import Dict
from uuid import uuid4


log = logging.getLogger(__name__)


def encode(data: Dict):
    log.debug(f'Encoding: {data}')
    cookie = str(uuid4())
    bencode_data = bencode.encode(data).decode('utf-8')
    encoded_data = cookie + " " + bencode_data
    log.debug(f'Encoded Data: {encoded_data}')
    return encoded_data


def decode(data: str):
    log.debug(f"Received Encoded Data: {data}")
    split_data = data.split(" ")
    cookie = split_data[0][1:]
    encoded_data = split_data[1].encode('utf-8')
    decoded_data = bencode.decode(encoded_data)
    log.debug(f"cookie: {cookie}, decoded_data: {decoded_data}")
    return cookie, decoded_data
