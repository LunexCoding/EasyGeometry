class _View:
  def showMessage(self, msg):
    print(msg)

  def requestInput(self, msg):
    return msg

g_view = _View()
