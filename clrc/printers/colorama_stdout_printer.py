from colorama import Fore, Style
from .abstract_printer import AbstractPrinter


class ColoramaStdout(AbstractPrinter):
  def success(self, *args, **kwargs):
    self.__print(Fore.GREEN, *args, **kwargs)

  def warn(self, *args, **kwargs):
    self.__print(Fore.MAGENTA, *args, **kwargs)

  def info(self, *args, **kwargs):
    self.__print(Fore.BLUE, *args, **kwargs)

  def danger(self, *args, **kwargs):
    self.__print(Fore.LIGHTRED_EX, *args, **kwargs)
  
  def error(self, *args, **kwargs):
    self.__print(Fore.RED, *args, **kwargs)

  def __print(self, color: str, *args, **kwargs):
    print(color, *args, **kwargs)
    print(Style.RESET_ALL)

