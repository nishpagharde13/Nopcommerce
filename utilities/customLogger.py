# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename="..\\Logs\\automation.log",
#                         format='%(asctime)s: %(levelname)s: %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p"
#                         )
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = ".\\Logs"
        log_file = log_dir + "\\automation.log"

        # Create Logs directory if it doesn't exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(
            filename=log_file,
            format="%(asctime)s : %(levelname)s : %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
            level=logging.INFO,
            force=True   # IMPORTANT for pytest
        )

        logger = logging.getLogger()
        return logger



