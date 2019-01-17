#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The module encapsulates the operation method of the configuration file
to provide more convenient use.

Provides methods to read configuration file parameters, modify configuration
file parameters, and delete configuration file parameters. Initialize the
path that needs to be passed into the configuration file, the method opens
the file directly, after which you can read and modify operations.

v1.0.1 update:
Now, no longer required the behavior of fetching the default config file when
reading. If the config file does not exist, and the default file not pass in,
raise an error directly.

v1.0.2 update:
Add getAllSections() & getAllKeys(section) & delKey(section, key) & a property
function 'config', it can read all sections and all keys in specified section,
can delete a key in section. Also can use config object.
"""
__author__ = "jeremyjone"
__datetime__ = "2018/12/13 14:06"
__all__ = ["__version__", "JConfig"]
__version__ = "1.0.2"

import configparser, os


class JConfig(object):
    def __init__(self, configFile, defaultFile=None):
        """
        :param configFile: config file path
        """

        self.__config_file = configFile

        if not os.path.exists(self.__config_file):
            if defaultFile:
                if not os.path.exists(os.path.dirname(self.__config_file)):
                    os.makedirs(os.path.dirname(self.__config_file))

                with open(self.__config_file, "w") as wf, \
                        open(defaultFile, "r") as rf:
                    wf.write(rf.read())
            else:
                raise configparser.Error("Can not find config file, you can "
                                         "pass in default config file.")

        self.__config = configparser.ConfigParser()
        self.__config.read(self.__config_file, encoding='UTF-8')

    def getConfig(self, section, key):
        try:
            return self.__config.get(section, key)
        except:
            # ###### No longer need read default file.
            # try:
            #     _config = configparser.ConfigParser()
            #     _config.read(self._default_config, encoding="UTF-8")
            #     v = _config.get(section, key)
            #     self.setConfig(section, key, v)
            #     return v
            # except:
            #     raise
            raise

    def setConfig(self, section, key, value):
        try:
            self.__config.add_section(section)
        except:
            pass

        self.__config.set(section, key, value)
        self.__config.write(open(self.__config_file, 'w'))

    def delConfig(self, section, key=None):
        try:
            if key is None:
                self.__config.remove_section(section)
            else:
                self.__config.remove_option(section, key)
        except:
            return

        self.__config.write(open(self.__config_file, 'w'))

    def delKey(self, section, key):
        try:
            self.__config.remove_option(section, key)
        except:
            return

        self.__config.write(open(self.__config_file, 'w'))

    def getAllSections(self):
        return self.__config.sections()

    def getAllKeys(self, section):
        return self.__config.options(section)

    @property
    def config(self):
        return self.__config
