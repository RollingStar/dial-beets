from beets.plugins import BeetsPlugin

class MyPlugin(BeetsPlugin):
	def __init__(self):
		super(MyPlugin, self).__init__()
		#all of these are strings. orig_year is a string for consistency with the latter two fields.
		self.album_template_fields['alb_orig_year'] = _tmpl_alb_orig_year
		self.album_template_fields['alb_orig_year_mm'] = _tmpl_alb_orig_year_mm
		self.album_template_fields['alb_orig_year_mm_dd'] = _tmpl_alb_orig_year_mm_dd

def _tmpl_alb_orig_year(album):
	if album.original_year > 0:
		return str(album.original_year)
	if album.year > 0:
		return str(album.year)
	else:
		return ''
def _tmpl_alb_orig_year_mm(album):
	result = _tmpl_alb_orig_year(album)
	og_mm = ''
	if album.original_month > 0:
		og_mm = str(album.original_month)
	#lazy coding here - could technically fail if orig year was stored,
	#but orig month fell back to release month. would give incorrect dates
	elif album.month > 0:
		og_mm = str(album.month)
	if result != '':
		if og_mm != '':
			og_mm = og_mm.zfill(2)
			#unicode police will come after me. I'm using - for simplicity rather than a hyphen
			result = result + '-' + og_mm
	else:
		#this should never happen, why would there be a month but no year?
		result = og_mm
	return result
def _tmpl_alb_orig_year_mm_dd(album):
	result = _tmpl_alb_orig_year_mm(album)
	og_dd = ''
	if album.original_day > 0:
		og_dd = str(album.original_day)
	#lazy coding here - could technically fail if orig year was stored,
	#but orig day fell back to release day. would give incorrect dates
	elif album.day > 0:
		og_dd = str(album.day)
	if result != '':
		if og_dd != '':
			og_dd = og_dd.zfill(2)
			#unicode police will come after me. I'm using - for simplicity rather than a hyphen
			result = result + '-' + og_dd
	else:
		#this should never happen, why would there be a day but no year?
		result = str(og_dd)
	return result
