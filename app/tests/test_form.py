from django.test import TestCase
from app.forms import CategoryForm

class CategoryFormTest(TestCase):
    def test_valid_data(self):
        form = CategoryForm({
            'title': "TV",
            'slug': "tv",
        })
        field = form.save()
        self.assertTrue(form.is_valid())
        self.assertEqual(field.title, "TV")
        self.assertEqual(field.slug, "tv")



