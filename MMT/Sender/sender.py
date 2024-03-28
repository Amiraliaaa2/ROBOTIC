import bluetooth
import time

# آدرس گیرنده
receiver_address = "00:00:00:00:00:00"  # جایگزین کنید با آدرس گیرنده‌ی واقعی

# اتصال به گیرنده
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((receiver_address, 1))

# ارسال دستورات به گیرنده
def send_command(command):
    sock.send(command)
    print("Command sent:", command)
    time.sleep(1)  # منتظر بمانید تا فرستنده آماده شود

# ارسال دستور حرکت به جلو
def move_forward():
    send_command("forward")

# ارسال دستور حرکت به عقب
def move_backward():
    send_command("backward")

# ارسال دستور توقف
def stop_movement():
    send_command("stop")

# بستن اتصال
sock.close()
