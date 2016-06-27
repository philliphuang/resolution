import os

def results(parsed, original_query):
  	target = parsed.values()[0]

  	# target cases
	if target in ("up", "increase", "higher"):
  		title = "Adjust resolution one step higher"
  		script = "up"

	elif target in ("down", "decrease", "lower"):
		title = "Adjust resolution one step lower"
  		script = "down"

	elif target in ("max", "maximum", "highest", "most"):
		title = "Adjust resolution to maximum"
  		script = "max"

	elif target in ("min", "minimum", "lowest", "least"):
		title = "Adjust resolution to minimum"
  		script = "min"

  	elif target in ("default", "reset", "standard"):
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
	os.system("osascript scripts/{}.applescript".format(script))