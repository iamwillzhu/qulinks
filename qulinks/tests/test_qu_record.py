from qulinks.models.qu_record import Qulink

class TestQulink:
    def test_get_qulink_by_name(self):
        assert(Qulink.get_qulink_by_name('pr') == Qulink(
            name='pr', 
            url='https://github.com/pulls'
        ))
