import bluetooth

# تنظیمات بلوتوث
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)

print("Waiting for connection...")

client_socket, address = server_socket.accept()
print("Accepted connection from", address)

# وضعیت متغیر برای تعیین اینکه آیا حرکت در حال اجرا است یا خیر
movement_in_progress = False

# وضعیت متغیر برای تعیین اینکه آیا دوربین روشن است یا خیر
camera_on = False

# شبکه دوربین
camera_network = None

# تنظیمات دوربین
camera_settings = {
    "resolution": (640, 480),
    "framerate": 30
}

# اطلاعات مکانی (مثالی)
gps_coordinates = "Latitude: 35.6895° N, Longitude: 139.6917° E"

# اتصال به دوربین
def connect_camera():
    global camera_network
    # کد اتصال به دوربین
    # در اینجا مثالی از اتصال به دوربین ارائه شده است

# ارسال تصویر لایو به فرستنده
def send_live_feed():
    global camera_on
    if camera_on:
        # کد ارسال تصویر لایو
        # در اینجا مثالی از ارسال تصویر به فرستنده ارائه شده است
        pass

# توقف اتصال دوربین
def disconnect_camera():
    global camera_on, camera_network
    if camera_on and camera_network:
        # کد قطع اتصال دوربین
        # در اینجا مثالی از قطع اتصال دوربین ارائه شده است
        camera_network = None
        camera_on = False
        # ارسال پاسخ به فرستنده
        client_socket.send("Camera disconnected.".encode())
    else:
        # اگر دوربین قبلاً قطع شده باشد، پیام خطا ارسال شود
        client_socket.send("Camera already disconnected.".encode())


# بررسی مانع
def check_obstacle():
    # مثالی از بررسی مانع با استفاده از سنسورها
    obstacle_detected = False  # جایگزین کنید
    if obstacle_detected:
        return True
    else:
        return False

# ارسال اطلاعات مکانی
def send_gps_coordinates():
    global gps_coordinates
    client_socket.send(f"GPS Coordinates: {gps_coordinates}".encode())

while True:
    try:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        
        # بررسی آیا حرکت در حال اجرا است
        if movement_in_progress:
            # اگر حرکت در حال اجرا بود، هیچ دستوری را قبول نکن
            client_socket.send("Movement already in progress. Please wait.".encode())
            continue
        
        # در صورتی که حرکت در حال اجرا نباشد، دستور جدید را بررسی کن
        if data == "forward":
            print("Moving forward...")
            # کد حرکت به جلو
            if check_obstacle():
                client_socket.send("Obstacle detected. Movement halted.".encode())
            else:
                movement_in_progress = True
                # ارسال پاسخ به فرستنده
                client_socket.send("ACK".encode())
        
        elif data == "backward":
            print("Moving backward...")
            # کد حرکت به عقب
            if check_obstacle():
                client_socket.send("Obstacle detected. Movement halted.".encode())
            else:
                movement_in_progress = True
                # ارسال پاسخ به فرستنده
                client_socket.send("ACK".encode())
        
        elif data == "stop":
            print("Stopping...")
            # کد توقف کامل
            movement_in_progress = False
            # ارسال پاسخ به فرستنده
            client_socket.send("ACK".encode())
        
        elif data == "camera":
            print("Activating camera...")
            # در صورتی که دوربین فعال نباشد، آن را فعال کن
            if not camera_on:
                connect_camera()
                camera_on = True
                # ارسال پاسخ به فرستنده
                client_socket.send("Camera activated.".encode())
            else:
                # اگر دوربین قبلاً فعال بود، پیام خطا ارسال شود
                client_socket.send("Camera already activated.".encode())
        
        elif data == "disconnect_camera":
            print("Disconnecting camera...")
            # قطع اتصال دوربین
            disconnect_camera()
        
        elif data == "live_feed":
            print("Sending live feed...")
            # ارسال تصویر لایو به فرستنده
            send_live_feed()
        
        elif data == "gps":
            print("Sending GPS coordinates...")
            # ارسال اطلاعات مکانی
            send_gps_coordinates()
        
        else:
            # در صورتی که دستور معتبر نباشد، پیام خطا ارسال شود
            client_socket.send("Invalid command.".encode())
        
    except bluetooth.btcommon.BluetoothError as e:
        print("Bluetooth error:", e)
        break

# بستن اتصالات
client_socket.close()
server_socket.close()
