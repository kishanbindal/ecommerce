from services.aws_services import AwsServices
from .models import Product


def update_product_image_url():

    products = Product.objects.filter(images__isnull=False)

    for product in products:
        presigned_url = AwsServices().get_presigned_url(product.name)
        product.images = presigned_url
        product.save()
