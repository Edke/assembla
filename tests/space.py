from .test import AssemblaTest
from ..models import Space

class TestsForSpace(AssemblaTest):

    def setup(self):
        super(TestsForSpace, self).setup()
        self.space = Space()

    def test_attributes_exist(self):   
        # Base class
        assert self.space.Meta.relative_url
        assert self.space.Meta.primary_key
        assert self.space.Meta.base_url
        assert self.space.Meta.base_api_url
        # HasObject class
        assert self.space.Meta.has_objects
        assert hasattr(self.space, '_milestones')
        assert hasattr(self.space, '_users')
        assert hasattr(self.space, '_tickets')
        # Unique attributes

    def test_child_functions_exist(self):
        assert self.space.milestone
        assert self.space.milestones
        assert self.space.user
        assert self.space.users
        assert self.space.ticket
        assert self.space.tickets

    def test_urls(self):
        space = Space()
        setattr(space, space.Meta.primary_key, 'test_space_pk')
        assert space.url == 'https://www.assembla.com/spaces/test_space_pk'
        assert space.api_url == 'https://www.assembla.com/spaces/test_space_pk'