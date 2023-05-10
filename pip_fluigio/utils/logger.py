import loguru


class Logger:
    @property
    def attribute(self):
        return loguru.logger.bind()

    # @property
    # def attribute_debug(self):
    #     loguru.logger.add(
    #         "file_debug_{time}.log",
    #         format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name} | {message} ",
    #         level="DEBUG",
    #         colorize=True,
    #         backtrace=True,
    #         diagnose=True,
    #     )
    #     return loguru.logger.bind()

    # @property
    # def attribute_warning(self):
    #     loguru.logger.add(
    #         "file.log",
    #         format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name} | {message} ",
    #         level="WARNING",
    #     )
    #     return loguru.logger.bind()

    # @property
    # def attribute_error(self):
    #     loguru.logger.add(
    #         "file.log",
    #         format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name} | {message} ",
    #         level="ERROR",
    #         colorize=True,
    #         backtrace=True,
    #         diagnose=True,
    #     )
    #     return loguru.logger.bind()
