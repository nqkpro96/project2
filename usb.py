
import pyudev
from time import strftime

current_devices={}
info = None

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb', device_type='usb_device')




def print_device_event(device):
    
    global current_devices
    
    if device.action == 'add':
        print("Device {0[ID_VENDOR]} {0[ID_MODEL]} with serial number {0[ID_SERIAL]} was plugged in. ----- {0[DEVNAME]}".format(device))
        
        observer.send_stop()
        return {device['DEVNAME'],device['ID_VENDOR'], device['ID_SERIAL']}
        # print device['ID_VENDOR']
    if device.action == 'remove':
        print("device removed")
    
    
    
def process_device_event(device):

    global current_devices, observer, info
    
    info = print_device_event(device)
    # observer.stop()
    # print info
    
observer = pyudev.MonitorObserver(monitor, callback=process_device_event, name='monitor-observer')
observer.daemon = False



def main():
    

    observer.start()
    
    
main()
