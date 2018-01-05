ControlFocus("选择要加载的文件", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("选择要加载的文件", "", "Edit1", $CmdLine[1])
Sleep(2000)
ControlClick("选择要加载的文件", "","Button1");