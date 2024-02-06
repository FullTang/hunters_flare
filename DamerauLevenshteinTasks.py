import csv
import subprocess

def damerau_levenshtein_distance(A, B):
    N, M = len(A), len(B)
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for j in range(M + 1):
        dp[0][j] = j
    for i in range(N + 1):
        dp[i][0] = i

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Insertion
                    dp[i][j - 1],      # Deletion
                    dp[i - 1][j - 1]   # Replacement
                )

                if i > 1 and j > 1 and A[i - 1] == B[j - 2] and A[i - 2] == B[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)  # Transposition

    return dp[N][M]

# Save a list of current running tasks on the Windows system as a CSV file.
with open("Tasks.csv", "w") as output_file:
    subprocess.run(["tasklist", "/FO", "CSV", "/NH"], stdout=output_file)

if __name__ == '__main__':
    try:
        # List of good tasks
        good_processes = [
            "AppHelperCap.exe",
            "AppleMobileDeviceService.exe",
            "ApplicationFrameHost.exe",
            "AppVShNotify.exe",
            "armsvc.exe",
            "aswidsagent.exe",
            "aswToolsSvc.exe",
            "audiodg.exe",
            "AvastSvc.exe",
            "AvastUI.exe",
            "backgroundTaskHost.exe",
            "bcc.exe",
            "bccavsvc.exe",
            "bcmHostControlService.exe",
            "bcmHostStorageService.exe",
            "bcmUshUpgradeService.exe",
            "BemSvc.exe",
            "BrConsole.exe",
            "BrHostHelper.exe",
            "BrHostSvr.exe",
            "BridgeCommunication.exe",
            "BrService.exe",
            "chrome.exe",
            "cmd.exe",
            "CodeMeter.exe",
            "CompPkgSrv.exe",
            "conhost.exe",
            "ctfmon.exe",
            "dasHost.exe",
            "DDVCollectorSvcApi.exe",
            "DDVDataCollector.exe",
            "DDVRulesProcessor.exe",
            "Dell.D3.WinSvc.exe",
            "Dell.DCF.UA.Bradbury.API.SubAgent.exe",
            "Dell.TechHub.Analytics.SubAgent.exe",
            "Dell.TechHub.DataManager.SubAgent.exe",
            "Dell.TechHub.Diagnostics.SubAgent.exe",
            "Dell.TechHub.exe",
            "Dell.TechHub.Instrumentation.SubAgent.exe",
            "Dell.TechHub.Instrumentation.UserProcess.exe",
            "DellOptimizer.exe",
            "DellSupportAssistRemedationService.exe",
            "DiagsCap.exe",
            "Discord.exe",
            "dllhost.exe",
            "dwm.exe",
            "ECDBWM.exe",
            "ECDBWMService.exe",
            "esif_uf.exe",
            "explorer.exe",
            "ExpressConnect.exe",
            "ExpressConnectNetworkService.exe",
            "ExpressConnectService.exe",
            "FileCoAuth.exe",
            "FileSyncHelper.exe",
            "firefox.exe",
            "FNPLicensingService64.exe",
            "fontdrvhost.exe",
            "GoogleCrashHandler.exe",
            "GoogleCrashHandler64.exe",
            "hasplms.exe",
            "hasplmv.exe",
            "HotKeyServiceUWP.exe",
            "HP.ClientSecurityManager.exe",
            "HPAudioAnalytics.exe",
            "HPCommRecovery.exe",
            "HPNotifications.exe",
            "hpqwmiex.exe",
            "HpSfuService.exe",
            "hpsvcsscan.exe",
            "ICPS.exe",
            "ICS.exe",
            "IDBWM.exe",
            "IDBWMService.exe",
            "IGCC.exe",
            "IGCCTray.exe",
            "igfxCUIService.exe",
            "igfxEM.exe",
            "IntelAnalyticsService.exe",
            "IntelAudioService.exe",
            "IntelConnect.exe",
            "IntelConnectivityNetworkService.exe",
            "IntelConnectService.exe",
            "IntelCpHDCPSvc.exe",
            "IntelCpHeciSvc.exe",
            "ipf_helper.exe",
            "ipf_uf.exe",
            "ipfsvc.exe",
            "java.exe",
            "jhi_service.exe",
            "jucheck.exe",
            "jusched.exe",
            "LanWlanWwanSwitchingServiceUWP.exe",
            "LMS.exe",
            "LockApp.exe",
            "mDNSResponder.exe",
            "Memory Compression",
            "mksSandbox.exe",
            "MoUsoCoreWorker.exe",
            "MpDefenderCoreService.exe",
            "mpv.exe",
            "mqsvc.exe",
            "msdtc.exe",
            "msedge.exe",
            "MsMpEng.exe",
            "mysqld.exe",
            "NetworkCap.exe",
            "NisSrv.exe",
            "notepad++.exe",
            "nssm_64.exe",
            "NVDisplay.Container.exe",
            "nvWmi64.exe",
            "OfficeClickToRun.exe",
            "OneApp.IGCC.WinService.exe",
            "OneDrive.exe",
            "OpenConsole.exe",
            "PhoneExperienceHost.exe",
            "powershell.exe",
            "PresentationFontCache.exe",
            "python.exe",
            "python3.12.exe",
            "QtWebEngineProcess.exe",
            "RstMwService.exe",
            "RtkAudUService64.exe",
            "RuntimeBroker.exe",
            "SamsungPortableSSDMon.exe",
            "SDXHelper.exe",
            "SearchApp.exe",
            "SearchFilterHost.exe",
            "SearchHost.exe",
            "SearchIndexer.exe",
            "SearchProtocolHost.exe",
            "SECOCL64.exe",
            "SECOMN64.exe",
            "SecurityHealthService.exe",
            "SecurityHealthSystray.exe",
            "SecurityUpdateService.exe",
            "server.exe",
            "ServiceShell.exe",
            "SgrmBroker.exe",
            "ShellExperienceHost.exe",
            "sihost.exe",
            "smartscreen.exe",
            "spoolsv.exe",
            "sqlwriter.exe",
            "StartMenuExperienceHost.exe",
            "steam.exe",
            "steamservice.exe",
            "steamwebhelper.exe",
            "SupportAssistAgent.exe",
            "SysInfoCap.exe",
            "SystemSettings.exe",
            "SystemSettingsBroker.exe",
            "taskhostw.exe",
            "tasklist.exe",
            "TbtP2pShortcutService.exe",
            "TextInputHost.exe",
            "ThunderboltService.exe",
            "TouchpointAnalyticsClientService.exe",
            "uhssvc.exe",
            "unsecapp.exe",
            "UserOOBEBroker.exe",
            "VGAuthService.exe",
            "vm3dservice.exe",
            "vmcompute.exe",
            "vmnat.exe",
            "vmnetdhcp.exe",
            "vmtoolsd.exe",
            "vmware.exe",
            "vmware-authd.exe",
            "vmware-tray.exe",
            "vmware-unity-helper.exe",
            "vmware-usbarbitrator64.exe",
            "vmware-vmx.exe",
            "WavesSvc64.exe",
            "WavesSysSvc64.exe",
            "WebEx.Uccm.exe",
            "Webex.Utils.WatchDog.exe",
            "WindowsPackageManagerServer.exe",
            "WindowsTerminal.exe",
            "WINWORD.EXE",
            "wlanext.exe",
            "WmiPrvSE.exe",
            "WMIRegistrationService.exe",
            "wsc_proxy.exe",
            "wslservice.exe",
            "WUDFHost.exe",
            "XboxGameBarWidgets.exe",
            "XboxPcAppFT.exe",
            "XtuService.exe",
        ]

        with open('Tasks.csv', 'r') as file_B:
            csv_reader = csv.reader(file_B)
            # Read the first two columns from the CSV file
            lines_B = [(row[0], row[1]) for row in csv_reader]
        
        sus_procs = 0

        with open('StealthyTasks.txt', 'w', encoding='utf-8') as output_file:
            for A in good_processes:
                for B in lines_B:
                    distance = damerau_levenshtein_distance(A, B[0])  # Comparing with the first column
                    if distance == 1 and B[0] not in good_processes:
                        sus_procs =+ 1
                        output_file.write(f"Stealthy task similar to {A} : {B[0]}            PID: {B[1]}\n")
            if sus_procs == 0:
                output_file.write("No stealthy tasks were found running on this system.")        
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
