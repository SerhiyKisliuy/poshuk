from PyQt5.QtCore import QSettings


class Settings:

    def setSettings(self, settings):
        savesettings = QSettings("setting.conf")
        savesettings.setValue("set", settings)
        savesettings.sync()

    def getSettings(self):
        self.getsettings = QSettings("setting.conf")
        self.settings = self.getsettings.value("set")
        self.settings = self.testSettings(self.settings)
        return self.settings

    def testSettings(self, settings):

        if not settings:
            settings = []
        try:
            settings['radioButtonCheck']
        except Exception:
            settings['radioButtonCheck'] = True

        try:
            settings['radioButton_2Check']
        except Exception:
            settings['radioButton_2Check'] = False

        try:
            settings['list_item']
        except Exception:
            settings['list_item'] = []

        return settings
