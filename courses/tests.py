from django.test import TestCase
from django.urls import reverse
from .models import Course


class CourseTests(TestCase):
    def test_list_page_opens(self):
        response = self.client.get(reverse("courses:list"))
        self.assertEqual(response.status_code, 200)

    def test_api_excludes_drafts(self):
        Course.objects.create(
            title="Published Course",
            slug="published-course",
            capacity=15,
            status="published",
        )
        Course.objects.create(
            title="Draft Course",
            slug="draft-course",
            capacity=10,
            status="draft",
        )

        response = self.client.get(reverse("courses:api"))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        titles = [item["title"] for item in data["courses"]]
        self.assertIn("Published Course", titles)
        self.assertNotIn("Draft Course", titles)
        self.assertEqual(len(data["courses"]), 1)