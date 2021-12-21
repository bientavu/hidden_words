from app.hidden_words import GridGenerator
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


class PdfGenerator:
    def __init__(self, words_number, grid_size):
        self.grid = GridGenerator(words_number, grid_size)
        self.data = self.grid.create_full_grid()
        self.title = [
            'Mots cachés générés aléatoirement grâce à motscachesgenerator.fr'
        ]
        self.words = [self.grid.random_words]
        self.second_title = ['Mots à trouver :']
        self.table = Table(self.data)
        self.to_replace = (
                self.data[00][0]
                + self.data[00][1]
                + self.data[00][2]
                + self.data[00][3]
        ).lower()
        self.filename = f'mots-caches-generator-{self.to_replace}.pdf'
        self.filepath = f'/tmp/mots-caches-generator-{self.to_replace}.pdf'
        self.pdf = SimpleDocTemplate(
            self.filepath,
            pagesize=letter
        )

    def structure(self):
        title_table = Table([self.title])
        grid_table = Table(self.data)
        words_table = Table(self.words)
        second_title_table = Table([self.second_title])
        full_structure = Table([
            [title_table],
            [grid_table],
            [second_title_table],
            [words_table]
        ])

        title_table_style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 14),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
            ('TOPPADDING', (0, 0), (-1, -1), 18)
        ])
        grid_table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER')
        ])
        words_table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
        ])
        full_structure_style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER')
        ])

        title_table.setStyle(title_table_style)
        grid_table.setStyle(grid_table_style)
        words_table.setStyle(words_table_style)
        second_title_table.setStyle(title_table_style)
        full_structure.setStyle(full_structure_style)

        return full_structure

    def generate_pdf(self):
        list_for_pdf = [self.structure()]
        self.pdf.build(list_for_pdf)

        return self
