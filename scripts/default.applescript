#!/usr/bin/osascript
tell application "System Preferences"
	set current pane to pane "Displays"
end tell

tell application "System Events"
	tell process "System Preferences"
		tell window "Built-in Retina Display"
			tell tab group 1 
				tell radio group 1
					-- check if selected in "Resolution" selection
					-- TODO: this may be redundant
					set atDef to value of radio button "Default for display"
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
						-- check if selected in "Scaled" selection
						-- TODO: check if universal
						if accessibility description of radio button selectedButton is "best quality" then
							set atDef to 1
						end if
					end tell
				end tell
				tell radio group 1
					-- final display
					if atDef is 1 then
						display dialog "Already at default resolution."
					else
						click radio button "Default for display"
					end if
				end tell
			end tell
		end tell
	end tell 
end tell