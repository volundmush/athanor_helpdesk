import os


def init(settings, plugins):
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))

    for app in ('django.contrib.humanize.apps.HumanizeConfig',
                'bootstrap4form',
                'account',
                'pinax.invitations',
                'pinax.teams',
                'reversion',
                'django_cleanup.apps.CleanupConfig',
                'helpdesk'):

        if app not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS.append(app)

    settings.URL_INCLUDES.append(("helpdesk/", "helpdesk.urls"))

    settings.TEMPLATES[0]["DIRS"].append(os.path.join(THIS_DIR, "web", "templates"))
