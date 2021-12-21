import boto3
from app.pdf_generator import PdfGenerator
from constants import BUCKET_NAME, OBJECT_KEY

s3 = boto3.client("s3")
pdf_generator = PdfGenerator(12, 24)


def lambda_handler(event, context):
    create_pdf = pdf_generator.generate_pdf()
    s3.upload_file(create_pdf.filepath, BUCKET_NAME, create_pdf.filename)
