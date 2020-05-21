from django.urls import reverse, resolve

class TestProductUrls:

    def test_products_view_url(self):
        path = reverse('products')
        assert resolve(path).view_name == 'products'