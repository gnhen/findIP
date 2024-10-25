import subprocess


def get_wifi_ip():
    command = "powershell \"Get-NetIPAddress -InterfaceAlias Wi-Fi | Where-Object {$_.AddressFamily -eq 'IPv4'} | Select-Object -ExpandProperty IPAddress\""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout.strip())


if __name__ == "__main__":
    get_wifi_ip()

    while True:
        user_input = input("Press 'Q' to quit: ").strip().upper()
        if user_input == "Q":
            break
