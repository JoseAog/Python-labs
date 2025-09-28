import subprocess

print("Haciendo ping a google.com ...")
resultado = subprocess.run(["ping", "-n", "2", "google.com"], capture_output=True, text=True)
print(resultado.stdout)
