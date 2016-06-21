import os

def results(parsed, original_query):
  	target = parsed.values()[0]

  	# target cases
	if target in ("increase", "up"):
  		title = "Adjust resolution one step higher"
  		cmd = "osascript -e 'display dialog \"TODO: AppleScript for increasing resolution one step\"'"

	elif target in ("decrease", "down"):
		title = "Adjust resolution one step lower"
  		cmd = "osascript -e 'display dialog \"TODO: AppleScript for decreasing resolution one step\"'"

	elif target in ("maximum", "max"):
		title = "Adjust resolution to maximum"
  		cmd = "osascript -e 'display dialog \"TODO: AppleScript for setting resolution to maximum\"'"

	elif target in ("minimum", "min"):
		title = "Adjust resolution to minimum"
  		cmd = "osascript -e 'display dialog \"TODO: AppleScript for setting resolution to minimum\"'"

  	elif target == "default":
  		title = "Adjust resolution to default"
  		cmd = "osascript -e 'display dialog \"TODO: AppleScript for setting resolution to default\"'"

  	else: 
  		title = "Invalid target resolution"
  		cmd = "osascript -e 'display dialog \"Invalid target resolution\"'"

	return {
		"title": title,
		"run_args": [cmd],
		"html": "<h1 style='font-family: sans-serif; padding: 2em'>{0}</h1>".format(title)
	}

def run(cmd):
	os.system(cmd)