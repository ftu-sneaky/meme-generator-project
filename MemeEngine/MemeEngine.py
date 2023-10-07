import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Class to generate meme file."""
    def __init__(self, meme_dir: str):
        """Initiate meme engine with the directory storing meme files."""
        self.mem_dir = meme_dir

    def make_meme(self, img: str, body: str, author: str) -> str:
        """Create meme with desired img, text and author."""

        out_path = f"{self.mem_dir}/{random.randint(0,1000000)}.png"
        content = f'{body} - {author}'

        with Image.open(img) as meme:
            old_width, old_height = meme.size
            ratio = 500/old_width
            new_size = new_width, new_height = 500, int(ratio*old_height)
            meme = meme.resize(new_size)

            draw = ImageDraw.Draw(meme)
            x, y = 10, random.randint(20, new_height-20)
            font = ImageFont.truetype(font='./_data/arial.ttf', size=20)
            draw.text((x, y), content, fill='white', font=font)
            meme.save(out_path)

        return out_path
