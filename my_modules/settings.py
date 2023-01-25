from PyQt5.QtCore import QSettings


class Settings:

    def setSettings(self, settings):
        savesettings = QSettings("setting.conf")
        savesettings.setValue("set", settings)
        savesettings.sync()
        print("setSettings")

    def getSettings(self):
        getsettings = QSettings("setting.conf")
        settings = getsettings.value("set")
        if settings:
            print("OkSettings")
            return settings
        else:
            settings = {}
            settings['radioButtonCheck'] = True
            settings['radioButton_2Check'] = False
            print("NoSettings")
            return settings
