import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    # 每次记得把配置文件的nc改为15
    model = RTDETR('ultralytics/cfg/models/rt-detr/rtdetr-RGCSPELAN.yaml')
    # model.load('weights/rtdetr-r18.pt')  # loading pretrain weights
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=500,
                batch=32,
                workers=8,
                device='0',
                # resume='', # last.pt path  # 断点续训
                project='runs/train',
                name='RGCSPELAN',
                )

