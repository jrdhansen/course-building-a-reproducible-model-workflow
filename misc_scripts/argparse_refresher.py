#!/user/bin/env python
import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


# Separating this function from the main function allows us to import this file
# as a module if needed, separating boilerplate & argparsing from functional code.
def go(args):
    logger.info("This is a message")
    logger.warning("This is a warning")
    logger.error("This is an error")
    logger.info(f"This is {args.optional_arg}")
    logger.info(f"This is {args.required_arg}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This is a tutorial on the 'argparse' module"
    )
    parser.add_argument(
        "--optional_arg",
        type=float,
        help="An optional arg",
        required=False,
        default=1.234,
    )
    parser.add_argument(
        "--required_arg",
        type=str,
        help="An required arg",
        required=True,
        default="default_str_required_arg",
    )
    args = parser.parse_args()
    go(args)
