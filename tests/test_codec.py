# coding:utf-8

from snote import Codec


def test_valid():
    codec = Codec(u'secret_key')
    sn = codec.encode({})
    assert codec.decode(sn.token).obj == {}


def test_invalid():
    codec = Codec('secret_key')
    sn = codec.encode({})
    assert codec.decode(sn.token + b'x').obj is None
