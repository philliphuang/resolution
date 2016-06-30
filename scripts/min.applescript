#!/usr/bin/osascript
tell application "System Preferences"
	set current pane to pane "Displays"
end tell

tell application "System Events"
	tell process "System Preferences"
		tell window "Built-in Retina Display"
			tell tab group 1 
				tell radio group 1
					click radio button "Scaled"
				end tell
				tell group 2 
					tell radio group 1
						click radio button 1
					end tell
				end tell
			end tell
			-- confirm dialog warning
			tell sheet 1 
				click button "OK"
			end tell
		end tell
	end tell 
end tell