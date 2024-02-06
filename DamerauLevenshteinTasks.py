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
            "System Idle Process",
            "System",
            "Secure System",
            "Registry",
            "smss.exe",
            "csrss.exe",
            "wininit.exe",
            "services.exe",
            "LsaIso.exe",
            "lsass.exe",
            "fontdrvhost.exe",
            "WUDFHost.exe",
            "winlogon.exe",
            "dwm.exe",
            "svchost.exe",
            "IntelCpHDCPSvc.exe",
            "IntelCpHeciSvc.exe",
            "bcmUshUpgradeService.exe",
            "NVDisplay.Container.exe",
            "Memory Compression",
            "igfxCUIService.exe",
            "WmiPrvSE.exe",
            "spoolsv.exe",
            "bcmHostStorageService.exe",
            "bcmHostControlService.exe",
            "wlanext.exe",
            "conhost.exe",
            "AppleMobileDeviceService.exe",
            "armsvc.exe",
            "mDNSResponder.exe",
            "FNPLicensingService64.exe",
            "hasplms.exe",
            "OneApp.IGCC.WinService.exe",
            "IntelAudioService.exe",
            "jhi_service.exe",
            "LMS.exe",
            "nvWmi64.exe",
            "mysqld.exe",
            "RtkAudUService64.exe",
            "RstMwService.exe",
            "mqsvc.exe",
            "sqlwriter.exe",
            "esif_uf.exe",
            "ThunderboltService.exe",
            "TbtP2pShortcutService.exe",
            "nssm_64.exe",
            "Webex.Utils.WatchDog.exe",
            "WebEx.Uccm.exe",
            "WavesSysSvc64.exe",
            "MsMpEng.exe",
            "WMIRegistrationService.exe",
            "wslservice.exe",
            "cmd.exe",
            "java.exe",
            "server.exe",
            "dasHost.exe",
            "AggregatorHost.exe",
            "hasplmv.exe",
            "sihost.exe",
            "taskhostw.exe",
            "NisSrv.exe",
            "PresentationFontCache.exe",
            "explorer.exe",
            "igfxEM.exe",
            "StartMenuExperienceHost.exe",
            "RuntimeBroker.exe",
            "dllhost.exe",
            "ctfmon.exe",
            "LockApp.exe",
            "WavesSvc64.exe",
            "SecurityHealthSystray.exe",
            "SecurityHealthService.exe",
            "unsecapp.exe",
            "TextInputHost.exe",
            "steam.exe",
            "IGCCTray.exe",
            "IGCC.exe",
            "steamwebhelper.exe",
            "steamservice.exe",
            "firefox.exe",
            "CodeMeter.exe",
            "DDVRulesProcessor.exe",
            "Dell.D3.WinSvc.exe",
            "DellSupportAssistRemedationService.exe",
            "ServiceShell.exe",
            "DellOptimizer.exe",
            "msdtc.exe",
            "ExpressConnectNetworkService.exe",
            "ExpressConnectService.exe",
            "ExpressConnect.exe",
            "ECDBWMService.exe",
            "ECDBWM.exe",
            "Dell.TechHub.exe",
            "SupportAssistAgent.exe",
            "uhssvc.exe",
            "DDVDataCollector.exe",
            "DDVCollectorSvcApi.exe",
            "Dell.TechHub.Diagnostics.SubAgent.exe",
            "Dell.TechHub.Analytics.SubAgent.exe",
            "Dell.DCF.UA.Bradbury.API.SubAgent.exe",
            "Dell.TechHub.DataManager.SubAgent.exe",
            "Dell.TechHub.Instrumentation.SubAgent.exe",
            "Dell.TechHub.Instrumentation.UserProcess.exe",
            "ShellExperienceHost.exe",
            "PhoneExperienceHost.exe",
            "backgroundTaskHost.exe",
            "XboxGameBarWidgets.exe",
            "XboxPcAppFT.exe",
            "ApplicationFrameHost.exe",
            "UserOOBEBroker.exe",
            "Agent.exe",
            "vmcompute.exe",
            "SystemSettingsBroker.exe",
            "SearchHost.exe",
            "Discord.exe",
            "OneDrive.exe",
            "FileSyncHelper.exe",
            "FileCoAuth.exe",
            "mpv.exe",
            "QtWebEngineProcess.exe",
            "OfficeClickToRun.exe",
            "AppVShNotify.exe",
            "SearchIndexer.exe",
            "SDXHelper.exe",
            "GoogleCrashHandler.exe",
            "GoogleCrashHandler64.exe",
            "SystemSettings.exe",
            "msedge.exe",
            "audiodg.exe",
            "OpenConsole.exe",
            "WindowsTerminal.exe",
            "powershell.exe",
            "python.exe",
            "tasklist.exe",
            "chrome.exe"
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