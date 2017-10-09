# Creator: byStarTW # My telegram: @byStarTW_TW
# 程式預設語系: zh_TW, 本程式僅支援 Windows 系統。
# 如何編譯本程式以防止被竊取程式碼： python -m py_compile Installer.py
# 程式基礎設定
ProgramName = ""  # 程式名稱
ProgramVersion = ""  # 程式版本
InstallerTitle = "%s 安裝程序" % (ProgramName)  # 程式標題
InstallPath = '"%LocalAppData%\\"' + ProgramName  # 程式預設安裝位置
# 程式檔案位置 (從 InstallFileSave 複製到 InstallPath) #要雙斜線喔:-)
InstallFileSave = ".\\bin\\inst"
UserChangeIP = False  # 讓使用者更改安裝位置
InstallFinishedString = "%s 已經安裝完成。" % (ProgramName)  # 安裝完成後顯示文字
# 授權。 分行請輸入 \n
LicenseContent = "Python Installer 授權\n無特別授權 =P"
License = True  # 是否出現授權介面
# Prepare Program
import os
import sys
os.system("title " + InstallerTitle)
os.system("cls")


def InstallModule(IFS, IP):
    if os.path.exists('IP') == False:
        os.system("md " + IP)
    else:
        os.system("rd /s /q " + IP)
        os.system("md " + IP)
    os.system("xcopy /E /K /Y /Q " + IFS + " " + IP)


if len(sys.argv) > 1:
    if sys.argv[2] == "--slient":
        InstallModule(InstallFileSave, InstallPath)
# Main
if os.path.exists(InstallPath) == True:
    UninstallConfim = input("已經發現存在 %s 產品。\
是否要解除安裝？ ([Y]es/[N]o)： " % (ProgramName))
    if UninstallConfim == "Yes" or UninstallConfim == "Y":
        print("正在解除安裝 %s 產品..." % (ProgramName))
        os.system("rd /s /q " + InstallPath)
        print("解除安裝完成。")
        input("按下 Enter 完成安裝程序。")
        exit()
print("*" * 25)
# Format: 歡迎安裝 (程式名稱) (程式版本)
print("歡迎安裝 %s %s ！" % (ProgramName, ProgramVersion))
print("此程序會引導你安裝完成 %s 。" % (ProgramName))
input("按下 Enter 開始下個步驟， 按下 Ctrl - C 離開。")
# LICENSE
if License == True:
    os.system("cls")
    print("*" * 25)
    print("  *** 授權 ***  ")
    print(LicenseContent)
    print("*" * 25)
    input("按下 Enter 繼續下個步驟， 按下 Ctrl - C 離開。")
# ConfimInstall
os.system("cls")
if UserChangeIP == True:
    print("預設安裝位置： " + InstallPath)
    print("(!) 更換安裝位置將會導致本程式的解除安裝程序失效，\
未來如果你想移除本程式，僅能手動移除該程序資料夾。")
    newChangeIP = input("更換安裝位置至 (若想保持預設值，按下 Enter)： ")
    if not newChangeIP == "":
        InstallPath = newChangeIP
        print("已變更安裝位置。")
        os.system("cls")
    else:
        print("不變更安裝位置。")
        os.system("cls")
print("!" * 25)
print("安裝位置： " + InstallPath)
print("未來若要移除程序，請重新打開本程序即可解除安裝。")
inputConfim = input("請問要繼續安裝嗎？ ([Y]es/[N]o): ")
if inputConfim == "Y" or inputConfim == "Yes":
    print("正在安裝中... 請等待安裝完成。")
    InstallModule(InstallFileSave, InstallPath)
    print(InstallFinishedString)
    input("按下 Enter 完成安裝程序。")
    exit()
else:
    print("(!) 使用者不允許繼續安裝。 :-(")
    input("按下 Enter 離開安裝程序。")
    exit()
