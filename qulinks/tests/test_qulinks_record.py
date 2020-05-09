from qulinks.models.qulinks_record import Qulink, QulinksRecord

class TestQulinksRecord:
    def test_create_qulink(self):
        assert(Qulink.create_qulink('test', 'https://www.google.com/') == Qulink(
            name='test', 
            url='https://www.google.com/'
        ))

    def test_get_qulink_by_name(self):
        assert(Qulink.get_qulink_by_name('test') == Qulink(
            name='test',
            url='https://www.google.com/'
        ))

    def test_delete_qulink(self):
        qulinks_record = QulinksRecord.fetch_qulinks()
        qulink = Qulink.get_qulink_by_name('test')
        qulink.delete_qulink()
        qulinks_record_after_delete = QulinksRecord.fetch_qulinks()

        assert(qulink in qulinks_record)
        assert(qulink not in qulinks_record_after_delete)
