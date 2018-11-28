# CLRC - easy print with colors (clrc.info, clrc.warn, etc)


## Description

I made this package for easy printing colored messages to output. Under the hood - print function with usage of colorama (https://github.com/tartley/colorama) package colors.

Why? I wanted the simpliest way possible to import package - start right after with colored messages. All functions inside this package satisfy my and possible yours basic needs for colored output


## Installation

    pipenv install clrc

or

    pip install clrc

## Usage

You can pass additional *args like in plain print()

    import clrc

    # Available functions

    clrc.info()
    clrc.warn()
    clrc.success()
    clrc.error()
    clrc.danger()

    # Example:

    clrc.error("This is error", True, 2, False, 43.2)

## Licence

See licence file inside repository. But basically it's good old MIT