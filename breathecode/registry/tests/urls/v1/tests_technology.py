"""
Test /answer
"""

import random

from django.urls.base import reverse_lazy
from rest_framework import status

from ...mixins import RegistryTestCase


def get_serializer(asset_technology, assets=[], asset_technologies=[]):
    return {
        "description": asset_technology.description,
        "icon_url": asset_technology.icon_url,
        "lang": None,
        "is_deprecated": asset_technology.is_deprecated,
        "parent": None,
        "slug": asset_technology.slug,
        "title": asset_technology.title,
        "visibility": asset_technology.visibility,
        "sort_priority": asset_technology.sort_priority,
    }


def get_detailed_serializer(asset_technology, assets=[], asset_technologies=[]):
    return {
        "description": asset_technology.description,
        "icon_url": asset_technology.icon_url,
        "lang": None,
        "is_deprecated": asset_technology.is_deprecated,
        "featured_course": (
            {
                "banner_image": asset_technology.featured_course.banner_image,
                "slug": asset_technology.featured_course.slug,
                "icon_url": asset_technology.featured_course.icon_url,
                "academy": asset_technology.featured_course.academy.id,
                "syllabus": (
                    [x for x in asset_technology.featured_course.syllabus.all().values_list("id", flat=True)]
                    if asset_technology.featured_course and asset_technology.featured_course.syllabus
                    else []
                ),
                "color": asset_technology.featured_course.color,
                "course_translation": None,
                "technologies": asset_technology.featured_course.technologies,
            }
            if asset_technology.featured_course is not None
            else None
        ),
        "marketing_information": asset_technology.marketing_information,
        "parent": None,
        "slug": asset_technology.slug,
        "title": asset_technology.title,
        "visibility": asset_technology.visibility,
        "alias": [],
        "assets": [],
        "sort_priority": asset_technology.sort_priority,
    }


class RegistryTestSuite(RegistryTestCase):
    """
    🔽🔽🔽 Auth
    """

    def test_without_auth(self):
        url = reverse_lazy("registry:technology")
        response = self.client.get(url)

        json = response.json()
        expected = []

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.bc.database.list_of("registry.Asset"), [])

    def test_with_two_asset_technologies__passing_sort_priority__not_found_for_get_technologies(self):
        cases = (
            40,
            50,
            60,
        )
        query = random.choice(cases)

        sort_priority = random.choice(cases)

        while query == sort_priority:
            sort_priority = random.choice(cases)

        asset_technologies = [
            {"sort_priority": sort_priority, "slug": self.bc.fake.slug(), "title": self.bc.fake.slug()}
            for _ in range(0, 2)
        ]

        model = self.generate_models(
            authenticate=True,
            profile_academy=True,
            role=1,
            asset_technology=asset_technologies,
            capability="read_technology",
        )

        self.headers(academy=model.academy.id)

        url = reverse_lazy("registry:technology") + f"?sort_priority={query}"
        response = self.client.get(url)
        json = response.json()
        expected = []

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.bc.database.list_of("registry.AssetTechnology"),
            self.bc.format.to_dict(model.asset_technology),
        )

        # teardown
        self.bc.database.delete("registry.AssetTechnology")

    def test_with_two_asset_technologies__passing_sort_priority__found_for_get_technologies(self):
        cases = (
            1,
            2,
            3,
        )
        query = random.choice(cases)

        sort_priority = query

        asset_technologies = [
            {"sort_priority": sort_priority, "slug": self.bc.fake.slug(), "title": self.bc.fake.slug()}
            for _ in range(0, 2)
        ]

        model = self.generate_models(
            authenticate=True,
            profile_academy=True,
            role=1,
            asset_technology=asset_technologies,
            capability="read_technology",
        )

        self.headers(academy=model.academy.id)

        url = reverse_lazy("registry:technology") + f"?sort_priority={query}"
        response = self.client.get(url)
        json = response.json()
        expected = [
            get_serializer(x) for x in sorted(model.asset_technology, key=lambda x: x.sort_priority, reverse=True)
        ]

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.bc.database.list_of("registry.AssetTechnology"),
            self.bc.format.to_dict(model.asset_technology),
        )

        # teardown
        self.bc.database.delete("registry.AssetTechnology")

    def test_asset_technology_with_featured_course(self):

        courseModel = self.generate_models(course=1)

        asset_technology = {
            "slug": self.bc.fake.slug(),
            "title": self.bc.fake.word(),
            "featured_course": courseModel.course,
        }

        model = self.generate_models(
            asset_technology=asset_technology,
        )

        url = reverse_lazy("registry:get_technology_detail", kwargs={"tech_slug": model.asset_technology.slug})
        response = self.client.get(url)
        json = response.json()

        expected = get_detailed_serializer(model.asset_technology)

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # teardown
        self.bc.database.delete("registry.AssetTechnology")

    def test_asset_technology_with_marketing_information(self):
        marketing_info = {
            "title": {"us": "Practice python", "es": "Practica python"},
            "description": {"us": "Description in English", "es": "Descripción en español"},
            "video": {"us": "https://video-url-us", "es": "https://video-url-es"},
        }

        asset_technology = {
            "slug": self.bc.fake.slug(),
            "title": self.bc.fake.word(),
            "marketing_information": marketing_info,
        }

        model = self.generate_models(
            authenticate=True,
            profile_academy=True,
            role=1,
            asset_technology=asset_technology,
            capability="read_technology",
        )

        self.headers(academy=model.academy.id)

        url = reverse_lazy("registry:get_technology_detail", kwargs={"tech_slug": model.asset_technology.slug})
        response = self.client.get(url)
        json = response.json()

        expected = get_detailed_serializer(model.asset_technology)

        self.assertEqual(json, expected)
        self.assertIsNotNone(json["marketing_information"]["title"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # teardown
        self.bc.database.delete("registry.AssetTechnology")
