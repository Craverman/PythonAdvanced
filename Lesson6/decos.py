"""Декораторы"""

import sys
import logging
import logs.config_server_log
import logs.config_client_log
import traceback
import inspect

# метод определения модуля, источника запуска.
# Метод find () возвращает индекс первого вхождения искомой подстроки,
# если он найден в данной строке.
# Если его не найдено, - возвращает -1.
# os.path.split(sys.argv[0])[1]
if sys.argv[0].find('client') == -1:
    # если не клиент то сервер!
    LOGGER = logging.getLogger('server')
else:
    # ну, раз не сервер, то клиент
    LOGGER = logging.getLogger('client')


# Реализация в виде функции
def toLog(logging_function):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        """Обертка"""
        warp = logging_function(*args, **kwargs)
        LOGGER.debug(f'Initiating function {logging_function.__name__} using {args}, {kwargs}. '
                     f'from module {logging_function.__module__}.')
        return warp
    return log_saver

