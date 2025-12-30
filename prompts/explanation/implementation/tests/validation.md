- Simulated high CPU load
- Verified monitoring script output
- Simulated service failure
- Confirmed auto-recovery execution
### Test Case: Simulating High CPU
- Use `stress` tool
- Run `cpu_monitor.sh`
- Verify top output

### Test Case: Unresponsive VM
- Stop a critical service
- Run `auto_recovery.py`
- Expect the script to restart the service
