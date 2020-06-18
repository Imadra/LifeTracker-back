from django.urls import reverse, resolve


class TestUrls:


    def test_get_codeforces_tree(self):
        path = reverse('get_tree')
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'get_tree'