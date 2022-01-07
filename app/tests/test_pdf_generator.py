from app.pdf_generator import PdfGenerator


class TestPdfGenerator:
    def test_init(self):
        pdf_generator = PdfGenerator(10, 20)

        assert len(pdf_generator.words[0]) == 10
        assert len(pdf_generator.to_replace) == 4
        assert pdf_generator.to_replace.islower()
        assert pdf_generator.filename.endswith(".pdf")

    def test_pdf_is_generated(self):
        pdf_generator = PdfGenerator(10, 20)
        pdf = pdf_generator.generate_pdf()

        assert pdf.filepath.endswith(".pdf")
