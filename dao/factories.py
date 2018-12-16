from dependency_injector import providers

from config.factories import config
from dao.mysql import MySQL

mysql_factory = providers.Singleton(MySQL, config.mysql)
