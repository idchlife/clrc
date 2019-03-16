class AbstractPrinter:
  def success(self, *args, **kwargs):
    raise NotImplementedError()

  def warn(self, *args, **kwargs):
    raise NotImplementedError()

  def info(self, *args, **kwargs):
    raise NotImplementedError()

  def danger(self, *args, **kwargs):
    raise NotImplementedError()

  def error(self, *args, **kwargs):
    raise NotImplementedError()
