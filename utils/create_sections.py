from utils.section_commands import CVSection, CVEntries, CVEntry, vspace, CVEntryC
from pylatex.base_classes import Arguments
from pylatex import Command, Itemize
from pylatex.utils import bold, italic, NoEscape
from pylatex.utils import _latex_item_to_string as latex_str
from pathlib import Path

"""
TODO: 
1. Add new sections
2. Create an Itemizer function
3. Make a CVItems function for projects
3. Merge all section creation functions into one with eval()
4. Read from file
5. User input acceptable
6. Comments everywhere
"""


class MakeSection:
    SPACINGS = {'education': ['15mm', '12mm'],
                'skills': ['1mm', '5mm'],
                'work': ['6mm', '1cm'],
                'projects': ['4.5mm', '1cm']}

    def __init__(self, folder='../resume'):
        self.folder = folder

    def generate(self, doc, filename: str):
        Path(self.folder).mkdir(exist_ok=True, parents=True)
        doc.generate_tex(f'{self.folder}/{filename}')

    @staticmethod
    def make_list(doc, data):
        return 0

    @staticmethod
    def _education(doc, data_dict):
        command = CVEntry(arguments=Arguments(data_dict['degree'], data_dict['major'], data_dict['institution'],
                                              data_dict['duration'], data_dict['info']))
        doc.append(command)

    @staticmethod
    def _skill(doc, data_dict):
        line = ''
        for idx, i in enumerate(data_dict['data']):
            line += r'\bullet' + latex_str(Command('hspace', '1mm')) + \
                    latex_str(bold(i['subhead'])) + ' : ' + latex_str(i['info'])
            if idx + 1 < len(data_dict['data'].keys()):
                line += r'\newline'
            
        command = CVEntryC(arguments=Arguments(NoEscape(line), data_dict['base_skill'], '', '', ''))
        doc.append(command)

    @staticmethod
    def _honor(doc, data_dict):
        command = CVEntry(arguments=Arguments(data_dict['date'], data_dict['award'], '', '',
                                              NoEscape(latex_str(Command('hspace', '2mm')) + data_dict['description'])))
        doc.append(command)

    @staticmethod
    def _work(doc, data_dict):
        command = CVEntry(arguments=Arguments(data_dict['address'], data_dict['title'], data_dict['institution'],
                                              NoEscape(data_dict['duration']), data_dict['desc']))
        doc.append(command)

    @staticmethod
    def _project(doc, data_dict):
        command = CVEntry(arguments=Arguments(data_dict['field'], data_dict['title'], data_dict['category'],
                                              NoEscape(data_dict['date']), data_dict['desc_list']))

    def create_projects(self,  data_dicts, section_header='projects', spacings=SPACINGS['projects']):
        doc = CVEntries()
        doc.preamble.append(CVSection(arguments=Arguments(section_header.title())))
        for idx, data_dict in enumerate(data_dicts):
            if idx > 0:
                doc.append(vspace(spacings[0]))
            MakeSection._project(doc, data_dict)
        doc.append(vspace(spacings[1]))
        self.generate(doc, section_header.lower())

    def create_work(self,  data_dicts, section_header='work experience', spacings=SPACINGS['work']):
        doc = CVEntries()
        doc.preamble.append(CVSection(arguments=Arguments(section_header.title())))
        for idx, data_dict in enumerate(data_dicts):
            if idx > 0:
                doc.append(vspace(spacings[0]))
            MakeSection._work(doc, data_dict)
        doc.append(vspace(spacings[1]))
        self.generate(doc, section_header.lower())

    def create_education(self, data_dicts, section_header='education', spacings=SPACINGS['education']):
        doc = CVEntries()
        doc.preamble.append(CVSection(arguments=Arguments(section_header.title())))
        for idx, data_dict in enumerate(data_dicts):
            if idx > 0:
                doc.append(vspace(spacing=spacings[0]))
            MakeSection._education(doc, data_dict)
        doc.append(vspace(spacing=spacings[1]))
        self.generate(doc, section_header.lower())

    def create_skills(self, data_dicts, section_header='skills', spacings=SPACINGS['skills']):
        doc = CVEntries()
        doc.preamble.append(CVSection(arguments=Arguments(section_header.title())))
        for idx, data_dict in enumerate(data_dicts):
            MakeSection._skill(doc, data_dict)
        doc.append(vspace(spacing=spacings[1]))
        self.generate(doc, section_header.lower())

    def create_honors(self, data_dicts, section_header='honors'):
        doc = CVEntries()
        doc.preamble.append(CVSection(arguments=Arguments(section_header.title())))
        for idx, data_dict in enumerate(data_dicts):
            MakeSection._honor(data_dict)
        doc.append(vspace(spacing='5mm'))
        self.generate(doc, section_header.lower())


def make_education_dict():
    educ_dict = {'degree': Command('textnormal', input("Degree: ")), 'major': input("Major: "),
                 'institution': input("Name of University: "), "duration": input("Start and end date of program"),
                 'info': ''}
    return educ_dict


def test():
    # educ_dict = {'degree': Command('textnormal', 'Computer Science and Biology'), 'major': r"Bachelor of Science",
    #              "institution": r"McGill University", "duration": 'September 2020 - June 2023',
    #              'info': NoEscape(r"\underline{Relevant Courses}: Introduction to Software Systems, Algorithms and "
    #                               r"Data "
    #                               r"Structures, \newline\hspace{2.3 cm} Introduction to Computer Science, Calculus A "
    #                               r"\& B, "
    #                               r"Linear Algebra, Discrete Structures}")}
    # educ_dict = make_education_dict()

    educ_dict = {'degree': Command('textnormal', 'Computer Science Engineering'), 'major': r"Bachelor of Science",
                 "institution": r"Bangladesh University of Engineering and Technology",
                 "duration": 'January 2020 - Present', 'info': ''}
    skill_dict = [{'base_skill': 'Computer Science', 'data': ['C/ C++', 'Competitive Programming']},
                  {'base_skill': 'Music', 'data': ['Guitar', 'Vocals', 'Piano']}]

    obj = MakeSection(folder='../zarif/resume')
    obj.create_education([educ_dict])
    obj.create_skills(skill_dict)

    
test()
# doc.generate_tex('test_folder/temp')

