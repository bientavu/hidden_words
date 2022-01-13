from app.pdf_generator import PdfGenerator


class TestPdfGenerator:
    def test_init(self, fake_dynamo_db):
        all_words = fake_dynamo_db[5]['Items']
        pdf_generator = PdfGenerator(10, 20, all_words)

        assert len(pdf_generator.words[0]) == 10
        assert len(pdf_generator.to_replace) == 4
        assert pdf_generator.to_replace.islower()
        assert pdf_generator.filename.endswith(".pdf")

    def test_pdf_is_generated(self, fake_dynamo_db):
        all_words = fake_dynamo_db[5]['Items']
        pdf_generator = PdfGenerator(10, 20, all_words)
        pdf = pdf_generator.generate_pdf()

        assert pdf.filepath.endswith(".pdf")
