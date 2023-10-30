from RumblePy import RumbleBot
import sys
import time

# Definisi karakter loading yang berputar
loading_chars = ["-", "/", "|", "\\"]

# Buat list untuk menyimpan pasangan username dan password
credentials_list = []

# Baca file teks dengan daftar pasangan username dan password
with open('credentials.txt', 'r') as file:
    for line in file:
        username, password = line.strip().split(',')
        credentials_list.append({"username": username, "password": password})

# Buat list untuk menyimpan pasangan channel_id dan video_name
data_list = []

# Baca file teks dengan daftar pasangan channel_id dan video_name
with open('data.txt', 'r') as file:
    for line in file:
        channel_id, video_name = line.strip().split(',')
        data_list.append({"channel_id": channel_id, "video_name": video_name})

# Loop melalui setiap pasangan username, password, channel_id, dan video_name
for credentials in credentials_list:
    username = credentials["username"]
    password = credentials["password"]

    for data in data_list:
        channel_id = data["channel_id"]
        video_name = data["video_name"]

        # Inisialisasi karakter loading
        loading_index = 0

        rumble = RumbleBot(username=username, password=password, opts={"verbose": False})

        rumble.login()

        # Simulasi loading
        sys.stdout.write("Loading... ")
        sys.stdout.flush()

        # Melakukan simulasi loading
        for _ in range(5):  # Ganti angka ini sesuai dengan kebutuhan Anda
            time.sleep(1)  # Jeda 1 detik
            sys.stdout.write(loading_chars[loading_index])
            sys.stdout.flush()
            sys.stdout.write('\b')  # Kembali ke karakter sebelumnya
            loading_index = (loading_index + 1) % len(loading_chars)

        result = rumble.subscribe(channel_id, video_name)
        following_value = result['data']['following']

        status = "Sukses" if following_value else "Gagal"
        print(f"\n{status:<8} ({username:<15}) ({video_name})")
