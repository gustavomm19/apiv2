from unittest.mock import MagicMock, patch

from django.contrib.auth.models import Group

from breathecode.authenticate.management.commands.set_permissions import Command

from ...mixins.new_auth_test_case import AuthTestCase

PERMISSIONS = [
    {
        "name": "Can delete job",
        "description": "Can delete job",
        "codename": "delete_job",
    },
    {
        "name": "Get my profile",
        "description": "Get my profile",
        "codename": "get_my_profile",
    },
    {
        "name": "Create my profile",
        "description": "Create my profile",
        "codename": "create_my_profile",
    },
    {
        "name": "Update my profile",
        "description": "Update my profile",
        "codename": "update_my_profile",
    },
]

GROUPS = [
    {"name": "Admin", "permissions": [x["codename"] for x in PERMISSIONS], "inherit": []},
    {
        "name": "Default",
        "permissions": ["delete_job", "get_my_profile", "create_my_profile", "update_my_profile"],
        "inherit": [],
    },
    {
        "name": "Student",
        "permissions": ["delete_job", "get_my_profile", "create_my_profile", "update_my_profile"],
        "inherit": [],
    },
    {"name": "Legacy", "permissions": [], "inherit": ["Default", "Student", "Legacy"]},
]


def sort_by_id(items):
    return sorted(items, key=lambda x: x["id"])


class TokenTestSuite(AuthTestCase):

    def setUp(self):
        super().setUp()

        ContentType = self.bc.database.get_model("contenttypes.ContentType")
        Permission = self.bc.database.get_model("auth.Permission")

        content_type = ContentType.objects.filter().order_by("-id").first()
        permission = Permission.objects.filter().order_by("-id").first()

        # the behavior of permissions is not exact, this changes every time you add a model
        self.latest_content_type_id = content_type.id
        self.latest_permission_id = permission.id
        self.job_content_type_id = self.latest_content_type_id - 64
        self.can_delete_job_permission_id = self.latest_permission_id - 257

    """
    🔽🔽🔽 format of PERMISSIONS
    """

    def test__format__permissions(self):
        from breathecode.authenticate.management.commands.set_permissions import PERMISSIONS

        for permission in PERMISSIONS:
            self.assertRegex(permission["name"], r"^[a-zA-Z ]+$")
            self.assertRegex(permission["description"], r'^[a-zA-Z,. _()"]+$')
            self.assertRegex(permission["codename"], r"^[a-z_]+$")
            self.assertEqual(len(permission), 3)

    """
    🔽🔽🔽 format of GROUPS
    """

    def test__format__groups(self):
        from breathecode.authenticate.management.commands.set_permissions import GROUPS

        for group in GROUPS:
            self.assertRegex(group["name"], r"^[a-zA-Z ]+$")

            for permission in group["permissions"]:
                self.assertRegex(permission, r"^[a-z_]+$")

            for g in group["inherit"]:
                self.assertTrue(g in [x["name"] for x in GROUPS])

            self.assertEqual(len(group), 3)

    """
    🔽🔽🔽 execute successfully
    """

    @patch(
        "breathecode.authenticate.management.commands.set_permissions.get_permissions",
        MagicMock(return_value=PERMISSIONS),
    )
    @patch("breathecode.authenticate.management.commands.set_permissions.get_groups", MagicMock(return_value=GROUPS))
    def test__execute__ends_successfully(self):
        Permission = self.bc.database.get_model("auth.Permission")
        permissions = self.bc.format.to_dict(Permission.objects.all())

        command = Command()
        command.handle()

        # the rest of elements are generated by django, is better ignored it
        self.assertEqual(
            self.bc.database.list_of("contenttypes.ContentType")[-1:],
            [
                {
                    "app_label": "breathecode",
                    "id": self.latest_content_type_id + 1,
                    "model": "SortingHat",
                },
            ],
        )

        # the rest of elements are generated by django, is better ignored it
        self.assertEqual(
            sort_by_id(self.bc.database.list_of("auth.Permission"))[-3:],
            [
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 3,
                    "name": "Update my profile",
                },
            ],
        )

        self.assertEqual(
            self.bc.database.list_of("auth.Group"),
            [
                {"id": 1, "name": "Admin"},
                {"id": 2, "name": "Default"},
                {"id": 3, "name": "Student"},
                {"id": 4, "name": "Legacy"},
            ],
        )

        self.assertEqual(
            sort_by_id(self.bc.format.to_dict(Group.objects.filter(name="Admin").first().permissions.all())),
            [
                *sort_by_id(permissions),
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 3,
                    "name": "Update my profile",
                },
            ],
        )

        self.assertEqual(
            sort_by_id(self.bc.format.to_dict(Group.objects.filter(name="Default").first().permissions.all())),
            [
                {
                    "codename": "delete_job",
                    "content_type_id": self.job_content_type_id,
                    "id": self.can_delete_job_permission_id,
                    "name": "Can delete job",
                },
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 3,
                    "name": "Update my profile",
                },
            ],
        )

        self.assertEqual(
            sort_by_id(self.bc.format.to_dict(Group.objects.filter(name="Student").first().permissions.all())),
            [
                {
                    "codename": "delete_job",
                    "content_type_id": self.job_content_type_id,
                    "id": self.can_delete_job_permission_id,
                    "name": "Can delete job",
                },
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + 3,
                    "name": "Update my profile",
                },
            ],
        )

    """
    🔽🔽🔽 execute successfully, all the elements exists previously
    """

    @patch(
        "breathecode.authenticate.management.commands.set_permissions.get_permissions",
        MagicMock(return_value=PERMISSIONS),
    )
    @patch("breathecode.authenticate.management.commands.set_permissions.get_groups", MagicMock(return_value=GROUPS))
    def test__execute__ends_successfully__run_second_time(self):
        num_permissions_was_deleted = 3
        permission = [
            {
                "name": "Get my profile",
                "codename": "get_my_profile",
                "content_type_id": self.latest_content_type_id + 1,
            },
            {
                "name": "Create my profile",
                "codename": "create_my_profile",
                "content_type_id": self.latest_content_type_id + 1,
            },
            {
                "name": "Update my profile",
                "codename": "update_my_profile",
                "content_type_id": self.latest_content_type_id + 1,
            },
        ]
        content_type = {
            "app_label": "breathecode",
            "model": "SortingHat",
        }
        permission_ids = [
            self.latest_permission_id + 1,
            self.latest_permission_id + 2,
            self.latest_permission_id + 3,
        ]
        groups = [
            {
                "name": "Admin",
                "permissions": permission_ids,
            },
            {
                "name": "Default",
                "permissions": permission_ids,
            },
            {
                "name": "Student",
                "permissions": permission_ids,
            },
        ]

        Permission = self.bc.database.get_model("auth.Permission")
        permissions = self.bc.format.to_dict(Permission.objects.all())
        model = self.bc.database.create(permission=permission, content_type=content_type, group=groups)

        command = Command()
        command.handle()

        # the rest of elements are generated by django, is better ignored it
        self.assertEqual(
            self.bc.database.list_of("contenttypes.ContentType")[-1:],
            [
                {
                    "app_label": "breathecode",
                    "id": self.latest_content_type_id + 1,
                    "model": "SortingHat",
                },
            ],
        )

        # the rest of elements are generated by django, is better ignored it
        self.assertEqual(
            sort_by_id(self.bc.database.list_of("auth.Permission"))[-3:],
            [
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 3,
                    "name": "Update my profile",
                },
            ],
        )

        self.assertEqual(
            sort_by_id(self.bc.database.list_of("auth.Group")),
            [
                {"id": 1, "name": "Admin"},
                {"id": 2, "name": "Default"},
                {"id": 3, "name": "Student"},
                {"id": 4, "name": "Legacy"},
            ],
        )

        self.assertEqual(
            sort_by_id(self.bc.format.to_dict(Group.objects.filter(name="Admin").first().permissions.all())),
            [
                *sort_by_id(permissions),
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 3,
                    "name": "Update my profile",
                },
            ],
        )

        self.assertEqual(
            sort_by_id(self.bc.format.to_dict(Group.objects.filter(name="Default").first().permissions.all())),
            [
                {
                    "codename": "delete_job",
                    "content_type_id": self.job_content_type_id,
                    "id": self.can_delete_job_permission_id,
                    "name": "Can delete job",
                },
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 3,
                    "name": "Update my profile",
                },
            ],
        )

        self.assertEqual(
            sort_by_id(self.bc.format.to_dict(Group.objects.filter(name="Student").first().permissions.all())),
            [
                {
                    "codename": "delete_job",
                    "content_type_id": self.job_content_type_id,
                    "id": self.can_delete_job_permission_id,
                    "name": "Can delete job",
                },
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 3,
                    "name": "Update my profile",
                },
            ],
        )

        self.assertEqual(
            sort_by_id(self.bc.format.to_dict(Group.objects.filter(name="Legacy").first().permissions.all())),
            [
                {
                    "codename": "delete_job",
                    "content_type_id": self.job_content_type_id,
                    "id": self.can_delete_job_permission_id,
                    "name": "Can delete job",
                },
                {
                    "codename": "get_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 1,
                    "name": "Get my profile",
                },
                {
                    "codename": "create_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 2,
                    "name": "Create my profile",
                },
                {
                    "codename": "update_my_profile",
                    "content_type_id": self.latest_content_type_id + 1,
                    "id": self.latest_permission_id + num_permissions_was_deleted + 3,
                    "name": "Update my profile",
                },
            ],
        )

    """
    🔽🔽🔽 execute, if it emit a exception, this test fail
    """

    def test__execute__does_not_emit_a_exception(self):
        command = Command()
        command.handle()
