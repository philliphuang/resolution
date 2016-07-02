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
						-- get current resolution level
						set selectedList to value of every radio button
						repeat with i from 1 to the count of selectedList
							if item i of selectedList is true then 
								set selectedButton to i
							end if
						end repeat
						-- switch to one level higher, if not at max
						if selectedButton is not count of selectedlist then 
							click radio button (selectedButton + 1)
						else
							display dialog "At maximum resolution."
						end if
					end tell
				end tell
			end tell
		end tell
	end tell 
end tell


