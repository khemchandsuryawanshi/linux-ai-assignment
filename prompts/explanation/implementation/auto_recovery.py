import subprocess

def is_healthy():
    result = subprocess.run(
        ["systemctl", "is-system-running"],
        stdout=subprocess.PIPE
    )
    return "running" in result.stdout.decode()

if not is_healthy():
    subprocess.run(["systemctl", "restart", "nginx"])
