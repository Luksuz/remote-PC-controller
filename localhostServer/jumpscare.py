from flask import Flask, request, jsonify
from time import sleep as delay
from flask_cors import CORS
import os
import subprocess

app = Flask(__name__)
CORS(app)
scare_video_path = "C:/Users/Luksuz/PycharmProjects/twitter_bot/jumpscare-use.mp4"

relative_apps = {
    "Roblox": "RobloxPlayerBeta.exe",
    "World of Tanks": "WorldOfTanks.exe",
    "Spotify": "Spotify.exe"
}

running_apps = {}

@app.route("/scare", methods=["POST"])
def display_scare_video():
    os.system(f"start wmplayer.exe /fullscreen {scare_video_path}")
    delay(2)
    os.system(f"taskkill /IM wmplayer.exe /F")
    return "User jumpscared"

@app.route("/displayApps", methods=["POST"])
def display_apps():
    try:
        processes = [process[:29].strip() for process in subprocess.check_output("tasklist", shell=True, text=True).splitlines()[2:]]
        processes = set(processes)
        running_apps.clear()  # Clear the dictionary to refresh the data
        for index, process in enumerate(processes):
            running_apps[str(index)] = process
        return jsonify(running_apps)  # Return the running_apps dictionary as JSON
    except subprocess.CalledProcessError:
        return "Error running the tasklist command"

@app.route("/killApp", methods=["POST"])
def kill_process():
    process_name = None
    req = request.json["app"]
    for key, value in running_apps.items():
        if req.lower() == key.lower():
            process_name = value
    if process_name is None:
        return "Invalid input"

    try:
        subprocess.run(['taskkill', '/F', '/IM', process_name], check=True)
        return f"Successfully killed {process_name}"
    except subprocess.CalledProcessError as e:
        return f"Error killing {process_name}: {e}"

@app.route("/shutdown", methods=["POST"])
def shutdown():
    os.system("shutdown /s /t 1")
    return "shutting down"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
