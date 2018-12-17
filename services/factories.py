from dependency_injector import providers

from config.factories import config
from services.account_service import AccountService
from services.queue_service import QueueService
from dao.factories import mysql_factory

account_service_factory = providers.Factory(AccountService, mysql_factory)

queue_service_factory = providers.Factory(QueueService, config.rabbitmq)
