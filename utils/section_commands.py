from pylatex.base_classes import Environment, CommandBase
from pylatex import Command
from pylatex.utils import dumps_list


class CVSection(CommandBase):
    _latex_name = 'cvsection'


class CVEntries(Environment):
    _latex_name = 'cventries'

    def __init__(self):
        super(CVEntries, self).__init__()
        self.preamble = []
        self.variables = []

    def dumps(self):
        """Represent the document as a string in LaTeX syntax.

        Returns
        -------
        str
        """

        head = ''
        head += dumps_list(self.variables) + '%\n'
        head += dumps_list(self.preamble) + '%\n'

        return head + '%\n' + super().dumps()


class CVEntryC(CommandBase):
    _latex_name = 'cventryC'


class CVEntry(CommandBase):
    _latex_name = 'cventry'


class ColorScheme(CommandBase):
    _latex_name = 'colorlet'


class MakeCVFooter(CommandBase):
    _latex_name = 'makecvfooter'


def vspace(spacing):
    return Command('vspace', spacing)


# def create_doc(data_dicts, block_spacing='15mm', final_spacing='5mm'):
#     doc = CVEntries()
#     doc.preamble.append(CVSection(arguments=Arguments("Education")))
#     for idx, data_dict in enumerate(data_dicts):
#         if idx > 0:
#             doc.append(vspace(spacing=block_spacing))
#         command = CVEntry(arguments=Arguments(data_dict['degree'], data_dict['major'], data_dict['institution'],
#                                               data_dict['duration'], data_dict['info']))
#         doc.append(command)
#
#     doc.append(vspace(spacing=final_spacing))
#     doc.generate_tex('test_folder/temp')
#     print(latex_str(doc))
