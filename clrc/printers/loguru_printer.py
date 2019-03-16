from .abstract_printer import AbstractPrinter


class LoguruPrinter(AbstractPrinter):
  def __init__(self, logger):
    self.logger = logger

  def success(self, *args, **kwargs):
   self.logger.success(*args, **kwargs)

  def warn(self, *args, **kwargs):
    self.logger.warning(*args, **kwargs)

  def info(self, *args, **kwargs):
    self.logger.info(*args, **kwargs)

  def danger(self, *args, **kwargs):
    self.logger.critical(*args, **kwargs)

  def error(self, *args, **kwargs):
    self.logger.error(*args, **kwargs)
