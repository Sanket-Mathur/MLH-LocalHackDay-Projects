import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import webbrowser

# Set system volume
class SetUpSystem:
    def set_volume(self, volume_level):
        """
        Sets the system volume according to personal preference
        """
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        volume.SetMasterVolumeLevel(volume_level, None)
    
    def open_geeksforgeeks(self, category, difficulty, status='unsolved', type='functional'):
        """
        Opens the geeksforgeeks page with given query parameters
        Parameter Values:
            difficulty: school=-2, basic=-1, easy=0, medium=1, hard=2
            status: solved, unsolved
            type: functional, full
        """
        category = category.title().replace(' ', '%20')

        webbrowser.open(f'https://practice.geeksforgeeks.org/explore/?category%5B%5D={category}&problemStatus={status}&problemType={type}&difficulty%5B%5D={difficulty}&page=1&sortBy=submissions&category%5B%5D={category}')
        
    def open_email(self):
        """
        Opens the default gmail account in the web browser
        """
        webbrowser.open('https://mail.google.com/mail/u/0/')
    
    def open_spotify(self):
        """
        Opens spotify GUI using the installed applications interface in the operating system
        """
        os.system('spotify')
    
if __name__ == "__main__":
    setup = SetUpSystem()
    setup.set_volume(-40.0)
    setup.open_geeksforgeeks('dynamic programming', 1)
    setup.open_email()
    setup.open_spotify()