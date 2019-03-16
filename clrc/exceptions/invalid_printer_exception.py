class InvalidPrinterException(Exception):
  def __init__(self):
    self.message = "Printer should extend AbstractPrinter"
