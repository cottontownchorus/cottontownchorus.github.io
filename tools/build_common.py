import subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
def encrypt(pw, src, outdir):
    subprocess.run(["staticrypt", "-p", pw, "--short", "--remember", "365", "-c", ".staticrypt.json",
        "--template-title", "Cottontown rehearsals", "--template-instructions", "Enter the chorus password.",
        "--template-button", "Open", "--template-color-primary", "#b3122e", "--template-color-secondary", "#f6eef0",
        "--template-placeholder", "Password", "--template-remember", "Remember me on this device",
        str(src), "-d", str(outdir)], check=True, cwd=ROOT)
