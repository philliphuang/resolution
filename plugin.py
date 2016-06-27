import os

def results(parsed, original_query):
  	target = parsed.values()[0]

  	# target cases
	if target in ("increase", "up"):
  		title = "Adjust resolution one step higher"
  		script = "up"

	elif target in ("decrease", "down"):
		title = "Adjust resolution one step lower"
  		script = "down"

	elif target in ("maximum", "max"):
		title = "Adjust resolution to maximum"
  		script = "max"

	elif target in ("minimum", "min"):
		title = "Adjust resolution to minimum"
  		script = "min"

  	elif target == "default":
  		title = "Adjust resolution to default"
  		script = "default"

  	else: 
  		title = "Invalid target resolution"
  		script = "invalid"

	return {
		"title": title,
		"run_args": [script],
		"html": "<h1 style='font-family: sans-serif; padding: 2em'>{0}</h1>".format(title)
	}

def run(script):
	os.system("osascript scripts/{}.scpt".format(script))