from pyramid.config import Configurator
from stormbb.resources import Root
from mongoengine import connect

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('stormbb.views.my_view',
                    context='stormbb:resources.Root',
                    renderer='stormbb:templates/mytemplate.pt')
    config.add_static_view('static', 'stormbb:static')

    # set up db
    #db_uri = settings['db_uri']
    db_name = settings['db_name']
    connect(db_name)
    return config.make_wsgi_app()

