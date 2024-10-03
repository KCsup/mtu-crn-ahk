#Include JSON.ahk

+n::
FileRead jsonString, crns.json
Data := JSON.load(jsonString)
Crns := Data.crns
for each, Crn in Crns
	Send %Crn%{Tab}
Send {enter}
return
