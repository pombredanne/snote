# coding:utf-8

import time
from snote import Codec


def test_properties():
    codec = Codec('secret_key')
    sn = codec.encode({})
    assert sn.obj is not None
    assert sn.timestamp is not None
    assert sn.tag is not None

    sn = codec.decode('')
    assert sn.obj is None
    assert sn.timestamp is None
    assert sn.tag is None
    assert sn.token == ''


def test_valid():
    codec = Codec('secret_key')
    sn = codec.encode([])
    assert sn.is_valid

    sn = codec.decode('')
    assert not sn.is_valid


def test_expire():
    codec = Codec('secret_key')
    sn = codec.encode(1)
    time.sleep(2)
    assert sn.is_expired(0)
    assert not sn.is_expired(10)

    sn = codec.decode('')
    assert not sn.is_expired(100)
