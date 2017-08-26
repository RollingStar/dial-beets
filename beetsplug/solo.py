from beets.plugins import BeetsPlugin

class MyPlugin(BeetsPlugin):
    def __init__(self):
        super(MyPlugin, self).__init__()
        self.album_template_fields['solo'] = _tmpl_solo

def _tmpl_solo(self, keys=None, disam=None, bracket=None):
    """In testing right now. For now, just a dummy
    function that returns False.
    Based on beets' built-in aunique() functionality. (tmpl_aunique)
    Determine if an album is uniquely disambiguated by the given "keys".
    Example use case:
    $if{solo, year, aunique{albumartist, year, year-mm, year-mm-dd}}
    In the example, we reliably return at least a "year", for unique artists,
    and a more specific release date for artists with multiple albums in
    the database.
    """
    return False