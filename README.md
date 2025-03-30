# vidtoolz-fade

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-fade.svg)](https://pypi.org/project/vidtoolz-fade/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-fade?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-fade/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-fade/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-fade/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-fade/blob/main/LICENSE)

Add fade in and out for a video using ffmpeg

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-fade
```
## Usage

type ``vid fade --help`` to get help

```bash
usage: vid fade [-h] [-f {in,out}] [-d DURATION] [-o OUTPUT] video

Add fade in and out for a video using ffmpeg

positional arguments:
  video                 Path to the input video file.

optional arguments:
  -h, --help            show this help message and exit
  -f {in,out}, --fadetype {in,out}
                        Type of fade effect to apply. Default: in
  -d DURATION, --duration DURATION
                        Duration of the fade effect in seconds. (Default 2)
  -o OUTPUT, --output OUTPUT
                        Path for the output video file. Defaults to
                        'input_name_fade.mp4'.

```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-fade
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
