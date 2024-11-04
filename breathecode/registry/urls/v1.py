from django.urls import path

from ..views import (
    AcademyAssetActionView,
    AcademyAssetAliasView,
    AcademyAssetCommentView,
    AcademyAssetOriginalityView,
    AcademyAssetSEOReportView,
    AcademyAssetView,
    AcademyCategoryView,
    AcademyContentVariableView,
    AcademyKeywordClusterView,
    AcademyKeywordView,
    AcademyTechnologyView,
    AssetImageView,
    AssetThumbnailView,
    AssetView,
    forward_asset_url,
    get_alias_redirects,
    get_categories,
    get_config,
    get_keywords,
    get_technologies,
    get_translations,
    handle_test_asset,
    render_preview_html,
    render_readme,
    AssetSupersedesView,
    AssetContextView,
)

app_name = "registry"
urlpatterns = [
    path("asset", AssetView.as_view(), name="asset"),
    path("asset/test", handle_test_asset),
    path("asset/thumbnail/<str:asset_slug>", AssetThumbnailView.as_view(), name="asset_thumbnail_slug"),
    path("asset/preview/<str:asset_slug>", render_preview_html),
    path("asset/gitpod/<str:asset_slug>", forward_asset_url),
    path("asset/<str:asset_slug>/supersedes", AssetSupersedesView.as_view()),
    path("asset/<str:asset_slug>/github/config", get_config),
    path("asset/<str:asset_slug>.<str:extension>", render_readme),
    path("asset/<str:asset_slug>", AssetView.as_view()),
    path("asset/<int:asset_id>/context", AssetContextView.as_view(), name="asset_context"),
    path("academy/contentvariable", AcademyContentVariableView.as_view()),
    path("academy/contentvariable/<str:variable_slug>", AcademyContentVariableView.as_view()),
    path("academy/asset", AcademyAssetView.as_view(), name="academy_asset"),
    path("academy/asset/image", AssetImageView.as_view()),
    path("academy/asset/comment", AcademyAssetCommentView.as_view()),
    path("academy/asset/comment/<str:comment_id>", AcademyAssetCommentView.as_view()),
    path("academy/asset/action/<str:action_slug>", AcademyAssetActionView.as_view()),
    path("academy/asset/alias", AcademyAssetAliasView.as_view()),
    path("academy/asset/alias/<str:alias_slug>", AcademyAssetAliasView.as_view()),
    path("academy/asset/<str:asset_slug>/action/<str:action_slug>", AcademyAssetActionView.as_view()),
    path("academy/asset/<str:asset_slug>/seo_report", AcademyAssetSEOReportView.as_view()),
    path("academy/asset/<str:asset_slug>/originality", AcademyAssetOriginalityView.as_view()),
    path("academy/asset/<str:asset_slug>/thumbnail", AssetThumbnailView.as_view()),
    path("academy/asset/<str:asset_slug>", AcademyAssetView.as_view()),
    path("keyword", get_keywords),
    path("academy/category", AcademyCategoryView.as_view()),
    path("academy/category/<str:category_slug>", AcademyCategoryView.as_view()),
    path("academy/keyword", AcademyKeywordView.as_view()),
    path("academy/keyword/<str:keyword_slug>", AcademyKeywordView.as_view()),
    path("academy/keywordcluster", AcademyKeywordClusterView.as_view()),
    path("academy/keywordcluster/<str:cluster_slug>", AcademyKeywordClusterView.as_view()),
    path("category", get_categories),
    path("technology", get_technologies, name="technology"),
    path("academy/technology", AcademyTechnologyView.as_view(), name="academy_technology"),
    path("academy/technology/<str:tech_slug>", AcademyTechnologyView.as_view()),
    path("translation", get_translations),
    path("alias/redirect", get_alias_redirects),
]
