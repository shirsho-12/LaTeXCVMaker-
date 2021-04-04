from pylatex import Document, Section, Subsection, Command, Enumerate
from pylatex.utils import italic, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments


class CVEntry(Environment):
    _latex_name = 'cventries'
    omit_if_empty = True

    def __init__(self):
        super.__init__()
        self.options = 5


class CVSection(CommandBase):
    """
    Creates a new CVSection (tex file header, eg. Education, Skills etc.)
    """
    _latex_name = 'cvsection'

    def __init__(self, section):
        super.__init__()
        self.options = 1

    @staticmethod
    def create_section(doc: Document, s):
        doc.append(CVSection(Arguments(s)))
        

class SubCategory(Document):
    def __init__(self):
        super().__init__()

    def education(self, s_dict, title='Education'):
        with self.create(CVEntry(title)) as environment:
            environment.Arg(r'\cventry')
            environment.append(f'\\textnormal{s_dict["major"]}')
            environment.append(s_dict['degree'])
            environment.append(s_dict['uni'])
            environment.append
        

# class SubCategory(Document):
#     def __init__(self):
#         super(SubCategory, self).__init__()
#         # create_file(category)
#
#     def template(self):
#         self.append(Command(r'\cvsection{Education}'))
#         self.append(Command(r'\begin{cventries}'))
