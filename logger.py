import logging

class Logger:
    def __init__(self, filename=None):
        self.filename = filename
        self.logger = logging.getLogger("my_logger")
        self.logger.setLevel(logging.DEBUG)

        self.console_handler = logging.StreamHandler()
        self.console_formatter = logging.Formatter(u'%(levelname)s - %(message)s')
        self.console_handler.setFormatter(self.console_formatter)
        self.logger.addHandler(self.console_handler)

        if filename:
            self.file_handler = logging.FileHandler(self.filename, encoding='utf-8')
            self.file_formatter = logging.Formatter(u'%(asctime)s - %(levelname)s - %(message)s')
            self.file_handler.setFormatter(self.file_formatter)
            self.logger.addHandler(self.file_handler)

    def info(self, *args):
        message = " ".join(map(str, args))
        self.logger.info(message)

    def warning(self, *args):
        message = " ".join(map(str, args))
        self.logger.warning(message)

    def error(self, *args):
        message = " ".join(map(str, args))
        self.logger.error(message)

if __name__ == "__main__":
    logger = Logger()
    logger.info("Это", "информационное", "сообщение", 123)
    logger.warning("Это", "предупреждение", {"ключ": "значение"})
    logger.error("Это", "сообщение", "об ошибке", [1, 2, 3])
