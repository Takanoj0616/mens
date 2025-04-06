from PIL import Image, ImageDraw
import os

def create_circular_image(input_path, output_path, size=(32, 32)):
    # 画像を開く
    img = Image.open(input_path)
    
    # 指定されたサイズにリサイズ
    img = img.resize(size)
    
    # 同じサイズの新しい画像（透明）を作成
    mask = Image.new('L', size, 0)
    
    # 円を描画
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    
    # アルファチャンネルを設定
    output = Image.new('RGBA', size, (0, 0, 0, 0))
    output.paste(img, (0, 0))
    output.putalpha(mask)
    
    # 保存
    output.save(output_path, 'PNG')

if __name__ == '__main__':
    input_path = 'static/images/new.png'
    output_path = 'static/images/new-round.png'
    create_circular_image(input_path, output_path)
    print(f'Created circular icon: {output_path}') 