import pytest
import vidtoolz_fade as w

from argparse import Namespace, ArgumentParser


def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(["hello.mp4"])
    assert result.video == "hello.mp4"
    assert result.output is None
    assert result.duration == 2
    assert result.fadetype == "in"


def test_plugin(capsys):
    w.fade_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``vidtoolz`` plugin." in captured.out
