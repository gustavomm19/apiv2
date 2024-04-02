from django.urls import path

from .views import (AcademyCohortSetCohortView, AcademyPlanView, AcademyServiceView, AcademyAcademyServiceView,
                    AcademySubscriptionView, BagView, CardView, CheckingView, ConsumableCheckoutView, EventTypeSetView,
                    MeConsumableView, MeInvoiceView, AcademyInvoiceView, MeSubscriptionCancelView,
                    MeSubscriptionChargeView, MentorshipServiceSetView, PayView, PlanOfferView, PlanView,
                    ServiceItemView, ServiceView, MeSubscriptionView)

app_name = 'payments'
urlpatterns = [
    path('planoffer', PlanOfferView.as_view(), name='planoffer'),
    path('plan', PlanView.as_view(), name='plan'),
    path('plan/<slug:plan_slug>', PlanView.as_view(), name='plan_slug'),
    path('academy/plan', AcademyPlanView.as_view(), name='academy_plan'),
    path('academy/plan/<int:plan_id>', AcademyPlanView.as_view(), name='academy_plan_id'),
    path('academy/plan/<slug:plan_slug>', AcademyPlanView.as_view(), name='academy_plan_slug'),
    path('academy/cohortset/<int:cohort_set_id>/cohort', AcademyCohortSetCohortView.as_view()),
    path('academy/cohortset/<slug:cohort_set_slug>/cohort', AcademyCohortSetCohortView.as_view()),
    path('service', ServiceView.as_view()),
    path('service/<slug:service_slug>', ServiceView.as_view()),
    path('service/<slug:service_slug>/items', ServiceItemView.as_view()),
    path('academy/service', AcademyServiceView.as_view()),
    path('academy/service/<slug:service_slug>', AcademyServiceView.as_view()),
    path('academy/academyservice', AcademyAcademyServiceView.as_view()),
    path('academy/academyservice/<slug:service_slug>', AcademyAcademyServiceView.as_view()),
    path('serviceitem', ServiceItemView.as_view(), name='serviceitem'),
    path('mentorshipserviceset', MentorshipServiceSetView.as_view(), name='mentorshipserviceset'),
    path('mentorshipserviceset/<int:mentorship_service_set_id>',
         MentorshipServiceSetView.as_view(),
         name='mentorshipserviceset_id'),
    path('eventtypeset', EventTypeSetView.as_view(), name='eventtypeset'),
    path('eventtypeset/<int:event_type_set_id>', EventTypeSetView.as_view(), name='eventtypeset_id'),
    path('me/service/consumable', MeConsumableView.as_view(), name='me_service_consumable'),
    path('consumable/checkout', ConsumableCheckoutView.as_view(), name='consumable_checkout'),
    path('me/subscription', MeSubscriptionView.as_view(), name='me_subscription'),
    path('me/subscription/charge', MeSubscriptionChargeView.as_view(), name='me_subscription_charge'),
    path('me/subscription/<int:subscription_id>/cancel',
         MeSubscriptionCancelView.as_view(),
         name='me_subscription_id_cancel'),
    path('academy/subscription', AcademySubscriptionView.as_view()),
    path('academy/subscription/<int:subscription_id>', AcademySubscriptionView.as_view()),
    path('me/invoice', MeInvoiceView.as_view()),
    path('me/invoice/<int:invoice_id>', MeInvoiceView.as_view()),
    path('academy/invoice', AcademyInvoiceView.as_view()),
    path('academy/invoice/<int:invoice_id>', AcademyInvoiceView.as_view()),
    path('card', CardView.as_view(), name='card'),
    path('bag', BagView.as_view()),
    path('checking', CheckingView.as_view(), name='checking'),
    path('pay', PayView.as_view(), name='pay'),
]
