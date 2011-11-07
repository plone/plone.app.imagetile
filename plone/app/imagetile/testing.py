from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from zope.configuration import xmlconfig


class PloneAppImagetileLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        import plone.app.imagetile
        xmlconfig.file('configure.zcml', plone.app.imagetile,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.app.imagetile:default')


PLONE_APP_IMAGETILE_FIXTURE = PloneAppImagetileLayer()
PLONE_APP_IMAGETILE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_APP_IMAGETILE_FIXTURE, ),
    name="plone.app.imagetile:Integration")
PLONE_APP_IMAGETILE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_APP_IMAGETILE_FIXTURE, ),
    name="plone.app.imagetile:Functional")
