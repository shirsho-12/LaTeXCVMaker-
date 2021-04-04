from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pathlib import Path


def generate(doc: Document, filename: str):
    doc.generate_pdf(filepath=f'test_folder/{filename}', clean_tex=False, compiler='pdflatex')
    doc.generate_tex(f'test_folder/{filename}')


def make_document():
    folder = Path('test_folder')
    folder.mkdir(exist_ok=True)
    doc = Document('basic', page_numbers=False)

    print("State 1 Started")
    generate(doc, 'state_1')
    print("State 1 Completed")
    doc.preamble.append(Command('title', "Person's Name"))
    doc.preamble.append(Command('author', "Graphico"))
    doc.preamble.append(Command('date', NoEscape(r'\today')))    # Raw string used here to make \ read
    doc.append(NoEscape(r'\maketitle'))
    print('State 2 Started')
    generate(doc, 'state_2')
    print('State 2 Completed')

    with doc.create(Section("Some text")):
        doc.append('Regular text\n')
        doc.append(italic('Italic text\n'))

        with doc.create(Subsection('Subsection created')):
            doc.append("Useless example  ")
            doc.append('for CVs.\n')
    print('State 3 Started')
    generate(doc, 'state_3')
    print('State 3 Completed')

    tex = doc.dumps()
    

make_document()
