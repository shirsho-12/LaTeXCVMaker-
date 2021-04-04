from pylatex import Document, Section, Subsection, Command, Itemize
from pylatex.utils import italic, NoEscape
from doc_base import DocClass


class CategoryCreator(DocClass):
    def __init__(self):
        super().__init__()

    def make_category(self, header, points):
        with self.create(Section(header)):
            with self.create(Itemize()) as bullet_list:
                for point in points:
                    bullet_list.add_item(point)
