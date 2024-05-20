from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import time
import cv2
import numpy as np

# Set window properties (color and size)
Window.clearcolor = (1, 1, 1, 1)
Window.size = (400, 600)

# Define the screen classes
class HomePage(Screen):
    pass

class CameraClick(Screen):
    hue_value = NumericProperty(0)
    lightness_value = NumericProperty(0)
    saturation_value = NumericProperty(0)

    def __init__(self, **kwargs):
        super(CameraClick, self).__init__(**kwargs)
        self.display_image = Texture.create(size=(1,1))
        self.cap = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def _convert_image(self, image):
        if isinstance(image, np.ndarray):
            buf = cv2.flip(image, 0).tobytes()
            texture = Texture.create(size=(image.shape[1], image.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            return texture
        else:
            print(f"Error converting image: Invalid Image type {type(image)}")
            default_texture = Texture.create(size=(1, 1))
            return default_texture

    def update(self, dt):
        ret, frame = self.cap.read()
        hls_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

        # Apply Hue, Lightness, and Saturation adjustments
        hls_image[:, :, 0] = np.clip(hls_image[:, :, 0] + self.hue_value, 0, 255).astype(np.uint8)
        hls_image[:, :, 1] = np.clip(hls_image[:, :, 1] + self.lightness_value, 0, 255).astype(np.uint8)
        hls_image[:, :, 2] = np.clip(hls_image[:, :, 2] + self.saturation_value, 0, 255).astype(np.uint8)

        modified_image = cv2.cvtColor(hls_image, cv2.COLOR_HLS2BGR)
        self.display_image = self._convert_image(modified_image)

        if self.display_image:
            try:
                self.ids.camera_image.texture = self.display_image
            except AttributeError:
                print("Error: camera image not found in ids")

    def capture(self):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        filename = f"IMG_{timestr}.png"

        # Convert Texture to numpy array
        image_array = np.frombuffer(self.display_image.pixels, dtype=np.uint8)
        image_array = image_array.reshape(self.display_image.height, self.display_image.width, 4)

        # OpenCV expects BGR format, so convert RGBA to BGR
        bgr_image = cv2.cvtColor(image_array, cv2.COLOR_RGBA2BGR)

        # Save the image using OpenCV
        cv2.imwrite(filename, bgr_image)

        return filename
    

    def color(self):
        
        # self.screen= Screen()
        self.cap=cv2.VideoCapture(0)
        
        
        while True:
            _,frame=self.cap.read()
            hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            height, width,_=frame.shape

            cx=int(width /2)
            cy=int(height /2)

            pixel_center=hsv_frame[cy, cx]
            hue_value=pixel_center[0]

            color="undefined"

            if hue_value<5:
                color="RED"
            elif hue_value<22:
                color="ORANGE"   
            elif hue_value<33:
                color="YELLOW"  
            elif hue_value<78:
                color="GREEN"  
            elif hue_value<131:
                color="BLUE"   
            elif hue_value<170:
                color="VIOLET"   
            else:
                color="RED"           

            pixel_center_bgr=frame[cy, cx]
            b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
            cv2.putText(frame,color,(10,70),0,1.5,(b,g,r),2)

            cv2.circle(frame, (cy, cx),5,(25,25,25),3)

            cv2.imshow("frame",frame)
            key=cv2.waitKey(1)
            if key==27:
                break
        # self.cap.release()
        return self.screen


class WindowManager(ScreenManager):
    pass

# Load the KV file
kv = Builder.load_file('pic.kv')

# Define the main application class
class MyApp(App):
    def build(self):
        self.title = "New Vision"  # Set application title
        return kv  # Return the root widget defined in KV file

# Run the application
if __name__ == '__main__':
    MyApp().run()
