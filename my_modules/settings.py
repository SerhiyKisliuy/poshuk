from PyQt5.QtCore import QSettings


class Settings:

    def setSettings(self, settings):
        savesettings = QSettings("setting1.conf")
        savesettings.setValue("set", settings)
        savesettings.sync()

    def getSettings(self):
        self.getsettings = QSettings("setting1.conf")
        self.settings = self.getsettings.value("set")
        self.settings = self.testSettings(self.settings)
        return self.settings

    def testSettings(self, settings):

        if not settings:
            settings = {'radioButtonCheck': True, 'radioButton_2Check': False, 'list_item': [], 'path_dir': '/Users'}

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

        try:
            settings['path_dir']
        except Exception:
            settings['path_dir'] = '/Users'

        return settings
