import json
import logging
import boto3
from botocore.exceptions import ClientError
from app.pdf_generator import PdfGenerator
from app.hidden_words import get_words_by_key
from constants import BUCKET_NAME

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    grid_size = int(event['grid-size'])
    words_number = int(event['words-number'])
    get_all_words = get_words_by_key(1)

    pdf_generator = PdfGenerator(words_number, grid_size, get_all_words)
    create_pdf = pdf_generator.generate_pdf()
    s3_client.upload_file(
        create_pdf.filepath,
        BUCKET_NAME,
        create_pdf.filename
    )

    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': create_pdf.filename},
            ExpiresIn=3600
        )
    except ClientError as e:
        logging.error(e)
        return None

    return json.dumps({
        'statusCode': 200,
        'body': response
    })
