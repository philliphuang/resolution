def results(fields, original_query):
	return {
		"title": fields,
		"run_args": [],
		"html": "<h1 style='font-family: sans-serif; padding: 2em'>{0}</h1>".format(fields)
	}
	

def run():