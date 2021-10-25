import sys
import logging

import {{ cookiecutter.repo_name }}

log_format = (
    "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
)
date_format = "%H:%M:%S"
logging.basicConfig(
    stream=sys.stdout, level=logging.INFO, format=log_format, datefmt=date_format
)

logger = logging.getLogger(__name__)


def main(param_path):
    logger.info("Starting script")
    params = {{cookiecutter.repo_name}}.utils.read_yml(param_path)
    logger.info('Parameters:')
    logger.info(params)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Must provide path to parameters.yml as sys.argv[1]")
    else:
        param_path = sys.argv[1]
        main(param_path)
