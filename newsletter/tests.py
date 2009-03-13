from django.test import TestCase
from django.core.urlresolvers import reverse

class ShopTest(TestCase):

    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_user_subscribe_twice_should_not_throw_error(self):
        post_data = {'email': "test@example.com", 'subscribed': True}
        for i in range(2):
            response = self.client.post(reverse('subscribe_detail'), post_data)
            self.assertTemplateUsed(response, "newsletter/success.html")
