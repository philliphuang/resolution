import os
from centered_text import centered_text

def results(parsed, original_query):
  	target = parsed.values()[0]

  	# target cases
	if target in ("up", "increase", "incr", "higher"):
  		title = "Adjust resolution a step higher"
  		script = "up"

	elif target in ("down", "decrease", "decr", "lower"):
		title = "Adjust resolution a step lower"
  		script = "down"

	elif target in ("max", "maximum", "maximize", "highest", "most"):
		title = "Adjust resolution to maximum"
  		script = "max"

	elif target in ("min", "minimum", "minimize", "lowest", "least"):
		title = "Adjust resolution to minimum"
  		script = "min"

  	elif target in ("default", "def", "reset", "standard"):
  		title = "Adjust resolution to default"
  		script = "default"

  	else: 
  		title = "Invalid target resolution"
  		script = "invalid"

	return {
		"title": title,
		"run_args": [script],
		"html": centered_text(title, hint_text="Press enter to apply."),
		"webview_transparent_background": True
	}

def run(script):
	os.system("osascript scripts/{}.applescript".format(script))