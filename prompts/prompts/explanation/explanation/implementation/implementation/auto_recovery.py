import subprocess

def system_healthy():
    result = subprocess.run(
        ["systemctl", "is-system-running"],
        stdout=subprocess.PIPE
    )
    return "running" in result.stdout.decode()

if not system_healthy():
    subprocess.run(["systemctl", "restart", "nginx"])
