from pylatex import Document, Section, Subsection, Command, Package, UnsafeCommand
from pylatex.utils import italic, NoEscape
from pathlib import Path
from utils.latex_commands import hspace, add_email, add_name, add_address, add_mobile, add_github, add_linkedin
from utils.section_commands import MakeCVFooter, ColorScheme
from pylatex.base_classes import Arguments, UnsafeCommand

# pylatex.PageStyle can be used for header and footer management
"""
%%% Override color
% Awesome Colors: awesome-emerald, awesome-skyblue, awesome-red, awesome-pink, awesome-orange
%                 awesome-nephritis, awesome-concrete, awesome-darknight
%% Color for highlight
% Define your custom color if you don't like awesome colors

% \definecolor{awesome}{rgb}{0.72, 0.53, 0.04}
%\definecolor{awesome}{HTML}{CA63A8}
%% Colors for text
%\definecolor{darktext}{HTML}{414141}
% \definecolor{text}{HTML}{414141}
% \definecolor{graytext}{HTML}{414141}
% \definecolor{lighttext}{HTML}{414141}
"""


class DocClass(Document):

    def __init__(self, author='Graphico', date=NoEscape(r'\today'), colorset='awesome-skyblue'):
        super().__init__(documentclass=NoEscape('awesome-cv'),
                         document_options=['10.8pt', 'a4paper'])
        # self.preamble_add('author', author)
        self.preamble_add('date', date)
        self.preamble_add(r'maketitle')
        # self.packages.append(Package('fontspec'))
        self.packages.append(Package('fontspec'))
        self.packages.append(Package('hyperref'))
        self.packages.append(Package('import'))
        self.preamble_add('fontdir', options=NoEscape(r'fonts/'))
        self.section_command = UnsafeCommand('newcommand*', arguments=Arguments('\sectiondir', r'resume/'))
        self.preamble.append(self.section_command)
        self.preamble.append(ColorScheme(arguments=Arguments('awesome', NoEscape(colorset))))

    def preamble_add(self, command, *args, options=None):
        print(args)
        self.preamble.append(Command(command, args, options=options))

    def add_essentials(self, data_dict: dict):
        self.preamble.append(add_name(data_dict['first_name'].title(), data_dict['last_name'].title()))
        self.preamble.append(add_address(data_dict['address'].title()))
        self.preamble.append(add_mobile(data_dict['phone']))
        self.preamble.append(add_email(data_dict['email']))

        if len(data_dict['linkedin']) > 1:
            self.preamble.append(add_linkedin(data_dict['linkedin']))
        if len(data_dict['github']) > 1:
            self.preamble.append(add_github(data_dict['github']))

        footer_text = data_dict['first_name'].title() + ' ' + data_dict['last_name'].title() + '~~~·~~~Curriculum Vitae'
        self.preamble.append(MakeCVFooter(arguments=Arguments('', NoEscape(footer_text), NoEscape(r'\thepage'))))

    def fill_doc(self, section_files: list):
        self.append(NoEscape(r'\makecvheader'))
        self.append(hspace('13.8cm'))
        for section in section_files:
            self.append(Command('import', arguments=Arguments(NoEscape(r'\sectiondir'), NoEscape(section.lower()))))

    @staticmethod
    def generate(doc: Document, filename: str, folder_path='test_folder'):
        # doc.generate_pdf(filepath=f'test_folder/{filename}', clean_tex=False, compiler='pdflatex', silent=True)
        doc.generate_tex(f'{folder_path}/{filename}')


obj = DocClass('TESTER TITLE')


def take_input():
    input_data = {'first_name': input("First Name: "), 'last_name': input("Last Name: "), 'address': input("Address: "),
                  'phone': input("Phone: "), 'email': input("Email: "), 'github': input("Github: "),
                  'linkedin': input("Linkedin: ")}
    return input_data


# dict_obj = {'first_name': 'Shirshajit', 'last_name': 'Sen Gupta', 'address': 'address ##$$@@ .1!',
#             'phone': '11223344', 'github': '', 'linkedin': r'linkedin.com/in/shirshajit',
#             'email': 'shirshajit@gmail.com'}
# dict_obj = take_input()
dict_obj = {'first_name': 'Zarif',
            'last_name': 'Ikram',
            'address': "116, Green Emerald, Dhanmondi 9/a, Dhaka",
            'phone': '01847304369',
            'email': 'zarifikram003@gmail.com',
            'github': '', 'linkedin': ''}
obj.add_essentials(dict_obj)

sections = ['skills.tex', 'education.tex']  # 'Experience.tex', 'Education.tex', 'Honours.tex', 'ECA.tex']
obj.fill_doc(sections)
DocClass.generate(obj, 'resume', 'zarif')


"""
In case of errors, remove the following packages:
% \usepackage[T1]{fontenc}%
% \usepackage{lmodern}%
% \usepackage{textcomp}%
% \usepackage{lastpage}%

"""