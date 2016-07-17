#!/usr/bin/osascript
tell application "System Preferences"
	set current pane to pane "Displays"
end tell

tell application "System Events"
	tell process "System Preferences"
		tell window "Built-in Retina Display"
			tell tab group 1 
				tell radio group 1
					if value of radio button "Default for display" is 1 then
						display dialog "Already at default resolution."
					else
						click radio button "Default for display"
					end if
				end tell
			end tell
		end tell
	end tell 
end tell