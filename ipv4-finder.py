import subprocess
import pyperclip


def get_wifi_ip():
    command = "powershell \"Get-NetIPAddress -InterfaceAlias Wi-Fi | Where-Object {$_.AddressFamily -eq 'IPv4'} | Select-Object -ExpandProperty IPAddress\""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip()


if __name__ == "__main__":
    ip_address = get_wifi_ip()
    print(ip_address)

    while True:
        user_input = input("Press 'C' to copy, or 'Q' to quit: ").strip().upper()
        if user_input == "C":
            pyperclip.copy(ip_address)
            print("IP address copied to clipboard.")
        elif user_input == "Q":
            break
