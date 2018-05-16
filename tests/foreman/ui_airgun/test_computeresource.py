from robottelo.datafactory import gen_string, valid_data_list
from robottelo.decorators import fixture, parametrize
from robottelo.config import settings
from nailgun import entities

@fixture(scope='module')
def module_org():
    return entities.Organization().create()

@parametrize('name', **valid_data_list('ui'))
def test_positive_create_docker(session, name):
    docker_url = settings.docker.external_url
    with session:
        session.computeresource.create({
            'name': name,
            'provider': 'Docker',
            'url': docker_url,
        })
        assert session.computeresource.search(name) == name


@parametrize('name', **valid_data_list('ui'))
def test_positive_create_libvirt(session, name):
    libvirt_url = settings.compute_resources.libvirt_hostname
    with session:
        session.computeresource.create({
            'name': name,
            'provider': 'Libvirt',
            'url': libvirt_url,
            'display_type': 'VNC',
        })
        assert session.computeresource.search(name) == name


@parametrize('name', **valid_data_list('ui'))
def test_positive_create_ovirt(session, name):
    rhev_url = settings.rhev.hostname
    username = settings.rhev.username
    password = settings.rhev.password
    cert = settings.rhev.ca_cert
    with session:
        session.computeresource.create({
            'name': name,
            'provider': 'oVirt',
            'url': rhev_url,
            'user': username,
            'password': password,
            'certification_authorities': cert,
        })
        assert session.computeresource.search(name) == name


def test_positive_rename(session):
    name = gen_string('alpha')
    ak_name = gen_string('alpha')
    docker_url = settings.docker.external_url
    with session:
        session.computeresource.create({
            'name': name,
            'provider': 'Docker',
            'url': docker_url,
        })
        session.computeresource.edit(name, {
            'name': ak_name,
        })
        session.computeresource.read(ak_name)
        assert session.computeresource.search(ak_name) == ak_name


def test_positive_delete(session):
    name = gen_string('alpha')
    docker_url = settings.docker.external_url
    with session:
        session.computeresource.create({
            'name': name,
            'provider': 'Docker',
            'url': docker_url,
        })
        session.computeresource.delete(name)
        assert session.computeresource.search(name) is None

@parametrize('name', valid_data_list())
def test_positive_v3_wui_can_add_resource(session, name, version=3):
    """Create new RHEV Compute Resource using APIv3 and autoloaded cert"""
    rhev_url = settings.rhev.hostname
    username = settings.rhev.username
    password = settings.rhev.password
    with session:
        session.computeresource.create({
            'name': name,
            'provider': 'oVirt',
            'url': rhev_url,
            'user': username,
            'password': password,
            'api4': version==4,
        })
        assert session.computeresource.search(name) == name
        assert session.computeresource.read(name)['api4'] == (version==4)

@parametrize('name', valid_data_list())
def test_positive_v4_wui_can_add_resource(session, name):
    """Create new RHEV Compute Resource using APIv4 and autoloaded cert"""
    test_positive_v3_wui_can_add_resource(session, name, version=4)

@parametrize('description', **valid_data_list('ui'))
def test_positive_v3_wui_can_edit_resource(session, module_org, description, version=3):
    """Edit a RHEV Compute Resource using APIv3 - change description"""
    rhev_url = settings.rhev.hostname
    username = settings.rhev.username
    password = settings.rhev.password
    with session:
        cr = entities.OVirtComputeResource(url=rhev_url, user=username,
                password=password, organization=[module_org], use_v4=version==4).create()
        session.computeresource.edit(name=cr.name, values={'description': description})
        assert entities.OVirtComputeResource(id=cr.id).read().description == description

@parametrize('description', **valid_data_list('ui'))
def test_positive_v4_wui_can_edit_resource(session, module_org, description):
    """Edit a RHEV Compute Resource using APIv4 - change description"""
    test_positive_v3_wui_can_edit_resource(session, module_org, description, version=4)
