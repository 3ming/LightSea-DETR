import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('ultralytics\cfg\models\\rt-detr\\rtdetr-r18.yaml')
    # model.load('weights/rtdetr-r18.pt')  # loading pretrain weights
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=5,
                batch=8,
                workers=8,
                device='0',
                # resume='', # last.pt path  # 断点续训
                project='runs/train_local',
                name='r-18',
                )

