from pylatex import Command
from pylatex.utils import NoEscape
from pylatex.base_classes import Arguments
from pylatex.utils import _latex_item_to_string as latex_str


def hspace(spacing):
    return Command('hspace', spacing)


def add_name(first_name, last_name, space=-1):
    command = hspace(NoEscape(f'{space}mm'))
    return Command('name', arguments=Arguments(NoEscape(latex_str(command) + first_name), last_name))


def add_address(address_str):
    return Command('address', address_str)


def add_mobile(mobile_str: str):
    return Command('mobile', mobile_str)


def add_email(email_str: str):
    return Command('email', email_str)


def add_linkedin(linkedin_str: str):
    return Command('linkedin', linkedin_str)


def add_github(github_str: str):
    return Command('github', github_str)
