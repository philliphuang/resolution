#!/usr/bin/osascript
tell application "System Preferences"
	set current pane to pane "Displays"
end tell

tell application "System Events"
	tell process "System Preferences"
		tell window "Built-in Retina Display"
			tell tab group 1 
				tell radio group 1
					click radio button "Default for display"
				end tell
			end tell
		end tell
	end tell 
end tell