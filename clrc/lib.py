from typing import List
from .printers import AbstractPrinter, ColoramaStdout
from .exceptions import InvalidPrinterException
from colorama import Fore, Style


class _Config():
  def __init__(self):
    self.printers: List[AbstractPrinter] = [
      ColoramaStdout()
    ]

  def add_printer(self, printer: AbstractPrinter):
    if not isinstance(printer, AbstractPrinter):
      raise InvalidPrinterException()
    self.printers.append(printer)

  def each_printer_exec_method(self, method: str, *args, **kwargs):
    printer: AbstractPrinter
    for printer in self.printers:
      method = getattr(printer, method)
      method(*args, **kwargs)


config = _Config()


def success(*args, **kwargs):
  config.each_printer_exec_method("success", *args, **kwargs)


def warn(*args, **kwargs):
  config.each_printer_exec_method("warn", *args, **kwargs)


def info(*args, **kwargs):
  config.each_printer_exec_method("info", *args, **kwargs)


def danger(*args, **kwargs):
  config.each_printer_exec_method("danger", *args, **kwargs)


def error(*args, **kwargs):
  config.each_printer_exec_method("error", *args, **kwargs)
