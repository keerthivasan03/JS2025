import shutil
import psutil

def check_disk_uage(disk):
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    return free>10
def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    return usage<25
if not check_disk_uage("/") or not check_cpu_usage():
    print("Error")
else:
    print("E OK")