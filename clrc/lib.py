from colorama import Fore, Style


def __print(color, *args, **kwargs):
  print(color, *args, **kwargs)
  print(Style.RESET_ALL)


def success(*args, **kwargs):
  __print(Fore.GREEN, *args, **kwargs)


def warn(*args, **kwargs):
  __print(Fore.MAGENTA, *args, **kwargs)


def info(*args, **kwargs):
  __print(Fore.BLUE, *args, **kwargs)


def danger(*args, **kwargs):
  __print(Fore.LIGHTRED_EX, *args, **kwargs)


def error(*args, **kwargs):
  __print(Fore.RED, *args, **kwargs)
