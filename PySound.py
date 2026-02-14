from just_playback import Playback
import threading
import os
import time

class PySound:
    def __init__(self):
        self.Playback = Playback()
        self.Path = ""

    # --- Play Music ---
    def Play(self, FilePath, Background=False):
        self.Playback.load_file(FilePath)
        self.Path = FilePath
        if Background:
            thread = threading.Thread(target=self.Playback.play)
            thread.start()
        else:
            self.Playback.play()

    # --- Pause / Resume / Stop ---
    def Pause(self):
        self.Playback.pause()

    def Resume(self):
        self.Playback.resume()

    def Stop(self):
        self.Playback.stop()

    # --- Volume Control ---
    def SetVolume(self, Volume, Unit="%"):
        if Unit == "%":
            Volume = Volume / 100.0
        elif Unit == "float":
            Volume = float(Volume)
        else:
            raise ValueError("Unit must be '%' or 'float'")
        Volume = max(0.0, min(1.0, Volume))
        self.Playback.set_volume(volume=Volume)

    # --- Fade In / Fade Out ---
    def FadeIn(self, Duration=2000, TargetVolume=1.0, Steps=20, freezeProcess=False):
        def _fade_in():
            step_time = Duration / Steps / 1000.0
            for i in range(Steps + 1):
                vol = (i / Steps) * TargetVolume
                self.Playback.set_volume(volume=vol)
                time.sleep(step_time)

        if freezeProcess:
            _fade_in()   
        else:
            thread = threading.Thread(target=_fade_in)
            thread.start()

    def FadeOut(self, Duration=2000, Steps=20, freezeProcess=False):
        def _fade_out():
            start_vol = self.Playback.volume
            step_time = Duration / Steps / 1000.0
            for i in range(Steps + 1):
                vol = start_vol * (1 - i / Steps)
                self.Playback.set_volume(volume=vol)
                time.sleep(step_time)
            self.Stop()

        if freezeProcess:
            _fade_out()   
        else:
            thread = threading.Thread(target=_fade_out)
            thread.start()

    def Mute(self):
        self.Playback.set_volume(0.0)

    def Unmute(self, volume=1.0):
        self.Playback.set_volume(volume)
    
    def Seek(self, seconds):
        self.Playback.seek(seconds)
    
    def Loop(self, entity, restart=False):
        # Start initial playback
        if restart:
            self.Playback.play()
        else:
            self.Playback.resume()

        # Define a background task so the main program doesn't freeze
        def playback_watcher():
            i = 0
            limit = float('inf') if entity == "inf" else entity
            
            while i < limit:
                # We only act if the playback has stopped/finished
                if not self.Playback.active: 
                    self.Playback.play()
                    if entity != "inf":
                        i += 1
                
                # Sleep briefly to keep CPU usage near 0%
                time.sleep(0.1)

        # Launch the watcher as a daemon thread
        threading.Thread(target=playback_watcher, daemon=True).start()

    # --- Info ---
    def Info(self):
        if self.Path:
            return {
                "Playing": self.Playback.playing,
                "Paused": self.Playback.paused,
                "Duration": self.Playback.duration,
                "CurrentPos": self.Playback.curr_pos,
                "Volume": self.Playback.volume,
                "Path": self.Path,
                "Filename": os.path.basename(self.Path)
            }

        return {}
