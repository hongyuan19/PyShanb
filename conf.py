#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os
import sys


# 设置默认配置
def default_config(configs, configfile):
    configs.add_section('General')
    configs.set('General', 'username', '')
    configs.set('General', 'password', '')
    configs.set('General', 'auto_play', '1')
    configs.set('General', 'auto_add', '0')
    configs.set('General', 'ask_add', '1')
    configs.set('General', 'enable_en_definition', '0')
    configs.set('General', 'enable_example', '0')

    with open(configfile, 'wb') as config_file:
        configs.write(config_file)


def get_option_value(func, section, option, default):
    """执行相关获取配置项值的操作，
    并使用默认值代替异常信息
    """
    try:
        return func(section, option)
    except:
        return default

CONFIGFILE = 'pyshanb.conf'  # 配置文件名称
config = ConfigParser.RawConfigParser()

# 读取配置文件。
config.read(CONFIGFILE)

# 如果没有配置文件或没有用户名及密码的配置项
# 则创建默认配置文件
if not (os.path.isfile(CONFIGFILE)
        and config.has_section('General')
        and config.has_option('General', 'username')
        and config.has_option('General', 'password')
        ):
    default_config(config, CONFIGFILE)

# 获取配置文件相关选项的值
# 用户名及密码
username = config.get('General', 'username')
password = config.get('General', 'password')
if not (username and password):
    a = u'Please configure your username and password'
    sys.exit(a + u'by config file(%s)' % (CONFIGFILE))

# 其他非必需项。如果未配置相关选项则使用默认值
auto_play = get_option_value(config.getboolean, 'General', 'auto_play', False)
auto_add = get_option_value(config.getboolean, 'General', 'auto_add', False)
ask_add = get_option_value(config.getboolean, 'General', 'ask_add', True)

enable_en_definition = get_option_value(config.getboolean, 'General',
                                        'enable_en_definition', False)
enable_example = get_option_value(config.getboolean, 'General',
                                  'enable_example', False)
#
site = 'http://www.shanbay.com'
url_login = '/accounts/login/'
api_get_word = '/api/word/%s'
api_add_word = '/api/learning/add/%s'
api_get_example = '/api/learning/examples/%s'

if __name__ == '__main__':
    print 'username:', username
    print 'password:', password
    print 'auto_play:', auto_play
    print 'auto_add:', auto_add
    print 'enable_en_definition:', enable_en_definition
    print 'enable_example:', enable_example
    print 'site:', site
    print 'url_login:', url_login
    print 'api_get_word:', api_get_word
    print 'api_add_word:', api_add_word
    print 'api_get_example:', api_get_example
