import os
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageOps, ImageFilter

from cfg import Config
from viewmodel import ViewModel

class JarvisView(tk.Label):

    def __init__(self, cfg: Config, view_model: ViewModel):

        super().__init__(bg='black')
        
        self.cfg = cfg
        self.viewmodel = view_model

        self._jarvis_img_path = os.path.join(self.cfg.root_path, "assets", "jarvis.png")
        self._center_image_path = os.path.join(self.cfg.root_path, "assets", "jarvis_center.png")
        
        # pack
        self.pack(pady=(250, 0))

        # size setting
        self._outer_radius, self._inner_radius = 92, 61
        self._sensitivity = 20
        self._output_size = (300, 300)
        self._center_size = (130, 130)

        # color setting
        self._tech_blue = (0, 191, 255)

        # image setting
        self._jarvis_img = self.create_circle_image(self._jarvis_img_path, self._output_size)
        self._center_image = Image.open(self._center_image_path).convert("RGBA")
        self._center_image_resized = self._center_image.resize(self._center_size, Image.Resampling.LANCZOS)

    def create_circle_image(self, path, output_size):
        img = Image.open(path).convert("RGBA")
        background = Image.new('RGBA', output_size, (0, 0, 0, 255))
        mask = Image.new('L', output_size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, output_size[0], output_size[1]), fill=255)
        img = img.resize(output_size, Image.Resampling.LANCZOS)  
        circle_img = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
        circle_img.putalpha(mask)
        background.paste(circle_img, (0, 0), circle_img)
        return background

    def update_jarvis(self):
        
        _jarvis_img_copy = self._jarvis_img.copy()
        draw = ImageDraw.Draw(_jarvis_img_copy)

        width, height = _jarvis_img_copy.size
        center = (width // 2, height // 2)

        _update_radius = self.viewmodel.update_jarvis_radius(self._outer_radius, self._inner_radius, self._sensitivity)

        # draw lighting effect
        self._draw_lighting(_jarvis_img_copy, center, _update_radius)

        # draw voice circle flow
        self._draw_circle_flow(draw, center, _update_radius)

        _jarvis_img_copy.paste(self._center_image_resized, (center[0]-self._center_size[0]//2, center[1]-self._center_size[1]//2), self._center_image_resized)

        jarvis_photo = ImageTk.PhotoImage(image=_jarvis_img_copy)

        self.config(image=jarvis_photo)
        self.image = jarvis_photo
    
    def _draw_lighting(self, _jarvis_img_copy, center, _update_radius):

        glow_radius = int(_update_radius * 1.1)
        glow = Image.new('RGBA', _jarvis_img_copy.size, (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow)
        glow_draw.ellipse([center[0]-glow_radius, center[1]-glow_radius, center[0]+glow_radius, center[1]+glow_radius], fill=self._tech_blue)
        glow = glow.filter(ImageFilter.GaussianBlur(radius=10))
        _jarvis_img_copy.paste(glow, (0, 0), glow)

    def _draw_circle_flow(self, draw: ImageDraw, center, _update_radius):
        draw.ellipse([center[0]-_update_radius, center[1]-_update_radius, center[0]+_update_radius, center[1]+_update_radius], fill='white', outline=self._tech_blue)
        