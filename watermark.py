import os,traceback
from PIL import Image

dirname, filename = os.path.split(os.path.abspath(__file__))
realPath=os.path.realpath(__file__)


def get_folder(fpath,wm_file,save_path):
    try:
        img_suffix_list = ['png', 'jpg', 'bmp']
        for i in os.listdir(fpath):
            if i.split('.')[-1] in img_suffix_list:
                img_path = fpath + '/' + i
                img_water_mark(img_file=img_path,wm_file=wm_file,save_path=save_path)
    except Exception as e:
        print(traceback.print_exc())

def img_water_mark(img_file, wm_file,save_path):
    img = Image.open(img_file)   
    watermark = Image.open(wm_file)   
    img_size = img.size
    wm_size = watermark.size
        
    if(img_size[0]>img_size[1]):
        proportion=(img_size[0])/wm_size[0]*1.5
    else:
        proportion=(img_size[1])/wm_size[1]*1.5
      

    wm_newSize=tuple([int(wm_size[0]*proportion),int(wm_size[1]*proportion)])
    watermark=watermark.resize(wm_newSize,resample=Image.BICUBIC,box=None,reducing_gap=None)
    wm_position = (int(img.size[0]/2-watermark.size[0]/2),int(img.size[1]/2-watermark.size[1]/2))
    
    print('-'*10)
    print('img.size：',img.size)
    print('proportion',proportion)
    print('watermark.size：',watermark.size)

    layer = Image.new('RGBA', img.size) 
    layer.paste(watermark, wm_position) 
    mark_img = Image.composite(layer, img, layer)
    new_file_name = '/new_'+img_file.split('/')[-1]
    print(save_path + new_file_name)
    mark_img.save(save_path + new_file_name)


if __name__ == "__main__":
    print('input:\t\t',dirname+'/pic\noutput:\t\t',dirname+'/save\nwatermark:\t',dirname+'/watermark.png' )
    if not os.path.exists(dirname+'/pic'):
        print('找不到pic文件夹，请将需要添加水印的图片，放到pic文件夹')
    else:
        if not os.path.exists(dirname+'/save'):
            os.mkdir(dirname+'/save')
        if not os.path.exists(dirname+'/watermark.png'):
            print('找不到watermark.png文件，请将水印文件命名为watermark.png')
        else:
            get_folder(dirname+'/pic',dirname+'/watermark.png',dirname+'/save')
